https://www.zhihu.com/search?type=content&q=xDeepFM

广告领域模型发展梳理以及最新模型xDeepFM解读


# Part-1 模型发展梳理

随着业务的持续迭代，手动交叉特征被视为脏活累活

2016年出现wide&deep、fnn和pnn等工作

wide&deep模型
- wide手动特征交叉，负责memorization
- deep部分MLP进行高阶特征交叉

2017年出现DeepFM、Deep&Cross和NFM等工作。
- DeeFM 作为Deep&wide结构的扩展
  - 一个是相对于Wide&Deep不再需要手工构建wide部分，
  - 另一个相对于FNN把FM的隐向量参数直接作为网络参数学习
  

# PART2--xDeepFm介绍

对于Deep&Cross模型的进阶

最终的输出包含三个部分
- 原始特征部分
- CIN模块
- MLP

核心的部分就是CIN模块，DeepFM中怎为FM的模块
- CIN模块的功能就是捕捉特征的高阶交叉

the field embedding is really important
- field like gender：one-hot embedding
- field like interests：multi-hot 