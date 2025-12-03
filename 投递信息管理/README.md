# 投递信息管理模块

## 文件说明

- `applications.xlsx`: 投递信息Excel数据库
- `scripts/`: 脚本文件
  - `track_applications.py`: 投递状态查询和管理脚本

## Excel表格结构

### 主表：applications

包含以下列：
- **id**: 投递记录ID（APP001, APP002...）
- **jd_id**: 关联的JD ID（可选，如果不从JD投递则为空）
- **company_name**: 公司名称
- **position_name**: 岗位名称
- **application_date**: 投递日期
- **channel_source**: 投递渠道/链接
- **status**: 投递状态（未投递、已投递、面试中、被拒、拿到Offer）
- **work_location**: 工作地点
- **salary_expectations**: 薪资待遇
- **next_action_date**: 下次跟进日期
- **notes**: 备注信息
- **created_at**: 创建时间
- **updated_at**: 更新时间

### 时间线表：timeline（可选，或使用单独Sheet）

- **application_id**: 关联的投递记录ID
- **date**: 事件日期
- **event**: 事件类型（投递、简历筛选、笔试、面试、被拒等）
- **notes**: 事件备注

### 面试记录表：interviews（可选，或使用单独Sheet）

- **application_id**: 关联的投递记录ID
- **round**: 面试轮次
- **date**: 面试日期
- **type**: 面试类型（技术面、HR面等）
- **interview_notes**: 面经内容
- **questions**: 面试问题（可用分隔符分隔）
- **feedback**: 面试反馈
- **result**: 面试结果

## 使用说明

1. 可以直接在Excel中打开`applications.xlsx`进行编辑和更新
2. 使用`scripts/track_applications.py`脚本进行状态查询：
   - 查看不同状态的岗位
   - 添加新的投递记录
   - 更新投递状态
3. 脚本会读取Excel文件并显示统计信息

