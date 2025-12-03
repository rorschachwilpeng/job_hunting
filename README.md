# 求职自动化管理系统

一个帮助自动化求职流程、提高追溯效率的系统。

## 系统架构

系统按照求职流程划分为5个模块：

1. **个人信息** - 管理简历和项目经历
2. **目标岗位** - 收集和标准化岗位描述（JD）
3. **岗位投递** - 生成简历调整建议
4. **投递信息管理** - 追踪投递状态（使用Excel）
5. **面试准备** - 生成面试问题和答案

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

或者使用虚拟环境：

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 配置系统

编辑 `config.yaml` 文件，填写你的LLM API Key：

```yaml
llm:
  api_key: "your-api-key-here"
  provider: "openai"  # 或 "claude", "custom"
  model: "gpt-4"
```

或者设置环境变量：

```bash
export LLM_API_KEY="your-api-key-here"
```

### 3. 初始化Excel数据库

运行以下命令创建投递信息Excel模板：

```bash
python3 投递信息管理/scripts/create_excel_template.py
```

这会在 `投递信息管理/applications.xlsx` 创建一个包含三个工作表的Excel文件：
- **applications**: 主表，记录所有投递信息
- **timeline**: 时间线表（可选使用）
- **interviews**: 面试记录表（可选使用）

### 4. 准备个人信息

- 将PDF简历放在 `个人信息/resume.pdf`
- 创建 `个人信息/resume_base.md`（简历的Markdown版本）
- 创建 `个人信息/projects.md`（详细项目经历）

## 使用流程

### 步骤1: 收集岗位信息

使用JD标准化脚本将网页上的岗位描述转换为统一格式：

```bash
python3 目标岗位/scripts/normalize_jd.py
```

脚本会：
- 自动分配JD ID（JD001, JD002...）
- 调用LLM标准化JD格式
- 保存到 `目标岗位/` 文件夹

### 步骤2: 生成简历调整建议

针对特定JD生成简历调整建议：

```bash
python3 岗位投递/scripts/generate_suggestions.py
```

输入JD ID后，脚本会：
- 读取JD和简历
- 调用LLM生成调整建议
- 保存对比表格到 `岗位投递/suggestions/`

### 步骤3: 管理投递信息

**方式1: 直接在Excel中编辑**

打开 `投递信息管理/applications.xlsx`，直接添加和更新投递记录。

**方式2: 使用脚本查询**

```bash
python3 投递信息管理/scripts/track_applications.py
```

脚本提供交互式菜单，可以：
- 查看不同状态的岗位
- 添加新的投递记录
- 更新投递状态

### 步骤4: 准备面试

针对特定JD生成完整的面试准备材料：

```bash
python3 面试准备/scripts/prepare_interview.py
```

输入JD ID后，脚本会生成：
- 最重要的3个职责
- 自我介绍（过去-现在-未来框架）
- 10个常见面试问题
- CAR格式的答案

## 文件夹结构

```
job_hunting/
├── config.yaml                    # 配置文件
├── requirements.txt               # Python依赖
├── 个人信息/
│   ├── resume.pdf                 # 原始简历
│   ├── resume_base.md             # 基础简历
│   ├── resume_versions/           # 定制简历版本
│   └── projects.md                # 项目经历
├── 目标岗位/
│   ├── JD001_公司名_岗位名.md
│   └── templates/                 # JD模板
├── 岗位投递/
│   ├── templates/                 # Prompt模板
│   ├── suggestions/               # 调整建议
│   └── scripts/                   # 脚本
├── 投递信息管理/
│   ├── applications.xlsx          # Excel数据库
│   └── scripts/                   # 管理脚本
└── 面试准备/
    ├── templates/                 # Prompt模板
    ├── materials/                 # 面试材料
    └── scripts/                   # 准备脚本
```

## 数据关联说明

- **JD可以独立存在**：即使不投递，也可以保存JD用于参考
- **投递记录可选关联JD**：`jd_id`字段可以为空
- **简历版本管理**：针对每个JD可以创建定制简历版本
- **面试准备**：可以针对任何JD生成面试材料，不要求已投递

## 注意事项

1. **Excel文件**：建议使用脚本进行查询，但可以直接在Excel中编辑数据
2. **API Key安全**：不要将包含API Key的config.yaml提交到Git
3. **数据备份**：定期备份Excel文件和重要文档
4. **版本控制**：简历版本会自动管理，但建议定期检查

## 开发计划

- [x] 项目结构搭建
- [x] 配置文件设计
- [x] Excel模板创建
- [ ] JD标准化脚本
- [ ] 简历调整建议脚本
- [ ] 投递信息管理脚本
- [ ] 面试准备脚本

## 贡献

欢迎提出建议和反馈！
