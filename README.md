# python_sipider_驾考宝典
## 分析:
1. 通过顺序练习，获取所有的题目id，采集所有题目的答案，并保存为本地json文件，目录中的answer_id.json。
2. 每一道题的答案顺序是可变的，答案只能通过识别正确的答案内容进行选择，不能只看选项。
3. 暂时没有设计地区问题，只能是默认的地区（北京）。
