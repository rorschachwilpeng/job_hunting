# 岗位投递模块

## 文件说明

- `templates/`: Prompt模板文件
  - `resume_tailoring_prompt.txt`: 简历调整建议的Few-Shot Prompt模板
- `suggestions/`: 生成的简历调整建议
  - `JD001_suggestions.md`: 针对JD001的简历调整建议
- `scripts/`: 脚本文件
  - `generate_suggestions.py`: 生成简历调整建议的脚本

## 使用说明

1. 运行`scripts/generate_suggestions.py`脚本
2. 输入JD ID（如JD001）
3. 脚本会读取对应的JD和简历，调用LLM生成调整建议
4. 建议会以表格形式保存到`suggestions/`文件夹
5. 可以基于建议创建新的简历版本

## 输出格式

建议文件包含：
- 最重要的3个职责
- 修改建议对比表（原内容 vs 建议修改）
- 详细修改说明

