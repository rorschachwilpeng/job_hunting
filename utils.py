#!/usr/bin/env python3
"""
公共工具模块
提供配置读取、LLM调用等通用功能
"""
import os
import yaml
from pathlib import Path
from typing import Dict, Optional
from openai import OpenAI


def load_config(config_path: str = "config.yaml") -> Dict:
    """加载配置文件"""
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_path}")
    
    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # 从环境变量读取API Key（如果配置文件中为空）
    if not config.get('llm', {}).get('api_key'):
        api_key = os.getenv('LLM_API_KEY')
        if api_key:
            config['llm']['api_key'] = api_key
    
    return config


def get_llm_client(config: Dict) -> OpenAI:
    """创建LLM客户端"""
    llm_config = config.get('llm', {})
    api_key = llm_config.get('api_key')
    
    if not api_key:
        raise ValueError("LLM API Key未配置，请在config.yaml中填写或设置环境变量LLM_API_KEY")
    
    provider = llm_config.get('provider', 'openai')
    base_url = llm_config.get('base_url')
    
    if provider == 'openai' or not base_url:
        # 默认使用OpenAI API
        client = OpenAI(api_key=api_key)
    else:
        # 自定义API（兼容OpenAI格式）
        client = OpenAI(api_key=api_key, base_url=base_url)
    
    return client


def call_llm(client: OpenAI, prompt: str, model: Optional[str] = None, config: Optional[Dict] = None) -> str:
    """调用LLM生成内容"""
    if config is None:
        config = load_config()
    
    model_name = model or config.get('llm', {}).get('model', 'gpt-4')
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"LLM调用失败: {str(e)}")


def get_next_jd_id(jd_folder: str) -> int:
    """获取下一个JD ID"""
    jd_path = Path(jd_folder)
    if not jd_path.exists():
        return 1
    
    # 查找所有JD文件
    jd_files = list(jd_path.glob("JD*.md"))
    if not jd_files:
        return 1
    
    # 提取所有JD ID
    jd_ids = []
    for jd_file in jd_files:
        # 从文件名提取ID，如 JD001_xxx.md -> 1
        name = jd_file.stem
        if name.startswith('JD'):
            try:
                id_str = name[2:5]  # 提取JD后的3位数字
                jd_ids.append(int(id_str))
            except ValueError:
                continue
    
    if not jd_ids:
        return 1
    
    return max(jd_ids) + 1


def get_path(config: Dict, key: str) -> Path:
    """获取配置中的路径，返回Path对象"""
    path_str = config.get('paths', {}).get(key)
    if not path_str:
        raise ValueError(f"配置中缺少路径: {key}")
    
    return Path(path_str)


def ensure_dir(path: Path):
    """确保目录存在"""
    if path.is_dir():
        path.mkdir(parents=True, exist_ok=True)
    else:
        path.parent.mkdir(parents=True, exist_ok=True)

