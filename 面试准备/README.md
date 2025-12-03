# 面试准备模块

## 文件说明

- `templates/`: Prompt模板文件
  - `prompt1_extract_responsibilities.txt`: 提取最重要的3个职责
  - `prompt2_tell_me_about_yourself.txt`: 生成自我介绍
  - `prompt3_common_questions.txt`: 识别常见面试问题
  - `prompt4_analyze_question.txt`: 分析问题意图
  - `prompt5_car_format.txt`: CAR格式答案生成
- `materials/`: 生成的面试准备材料
  - `JD001/`: 针对JD001的面试准备材料
    - `responsibilities.md`: 最重要的3个职责
    - `self_introduction.md`: 自我介绍
    - `common_questions.md`: 10个常见问题
    - `answers/`: CAR格式的答案文件
- `scripts/`: 脚本文件
  - `prepare_interview.py`: 面试准备脚本

## 使用说明

1. 运行`scripts/prepare_interview.py`脚本
2. 输入JD ID（如JD001）
3. 脚本会依次执行5个Prompt，生成完整的面试准备材料
4. 所有材料会保存在`materials/JD001/`文件夹中
5. 可以针对每个问题查看CAR格式的答案

## 生成内容

- **职责提取**: 基于JD提取最重要的3个职责
- **自我介绍**: 使用过去-现在-未来框架
- **常见问题**: 识别10个可能的面试问题
- **问题分析**: 理解问题意图和回答技巧
- **CAR答案**: 针对每个问题的具体答案

