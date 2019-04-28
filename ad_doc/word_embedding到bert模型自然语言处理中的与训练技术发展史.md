从Word Embedding到Bert模型—自然语言处理中的预训练技术发展史

https://zhuanlan.zhihu.com/p/49271699

从word embedding到bert模型，NLP中的预训练发展技术史

预训练在图像领域中的应用和NLP的任务类似

那么传统的word embedding方案有什么问题呢？
- 多义词问题
- 不论什么上下文的句子经过word2vec，都是预测相同的单词bank，而同一个单词占的是同一行的参数空间，这导致两种不同的上下文信息都会编码到相同的word embedding空间里去。所以word embedding无法区分多义词的不同语义，这就是它的一个比较严重的问题。

那么有没有优雅的解决方案呢？

神奇的ELMO

# 从Word Embedding到ELMO

ELMO是“Embedding from Language Models”的简称，其实这个名字并没有反应它的本质思想，提出ELMO的论文题目：“Deep contextualized word representation”

核心在于 deep contextualized 这个短语上，deep和context，

之前的word_embedding

事先用语言模型学好一个单词的Word Embedding，此时多义词无法区分，不过这没关系。在我实际使用Word Embedding的时候，单词已经具备了特定的上下文了，这个时候我可以根据上下文单词的语义去调整单词的Word Embedding表示，这样经过调整后的Word Embedding更能表达在这个上下文中的具体含义，自然也就解决了多义词的问题了。

此时对于问句X，我们可以先将句子X作为预训练好的ELMO网络的输入，这样句子X中每个单词在ELMO网络中都能获得对应的三个Embedding，之后给予这三个Embedding中的每一个Embedding一个权重a，这个权重可以学习得来，根据各自权重累加求和，将三个Embedding整合成一个。然后将整合后的这个Embedding作为X句在自己任务的那个网络结构中对应单词的输入，以此作为补充的新特征给下游任务使用。

“Feature-based Pre-Training” 从而解决了区分多义词的问题

那么有没有其它的有关工作吗？

**TagLM**
taglm可以看做是一个前导工作

ULMFiT使用的是三阶段模式，在通用语言模型训练之后，加入了一个领域语言模型预训练过程，而且论文重点工作在这块，方法还相对比较繁杂，这并不是一个特别好的主意，因为领域语言模型的限制是它的规模往往不可能特别大，精力放在这里不太合适，放在通用语言模型上感觉更合理；再者，尽管ULFMiT实验做了6个任务，但是都集中在分类问题相对比较窄，不如ELMO验证的问题领域广，我觉得这就是因为第二步那个领域语言模型带来的限制。

ELMO的核心在于引入了上下文动态调整单词的embedding后的多义词问题解决

那么ELMO有什么缺点吗？
- ELMO使用了LSTM而不是transformer作为特征提取器
- ELMO采用了双向拼接融合特征的能力比Bert一体化的特征融合


transformer
- 本质上是self-attention的叠加结构
- 作为一个效果很好的特征抽取器


## GPT
Generative Pre-Training

### 生成式的预训练方法
两阶段
- 利用语言模型进行预训练
- 通过Fine-tuning的模式解决下游任务

和ELMO的不同之处
- 特征抽取器不是用的RNN，而是用的Transformer
- GPT的预训练虽然仍然是以语言模型作为目标任务，但是采用的是单向的语言模型，所谓“单向”的含义是指：语言模型训练的任务目标是根据 W_i 单词的上下文去正确预测单词 W_i ， W_i 之前的单词序列Context-before称为上文，之后的单词序列Context-after称为下文。
- 

和Bert出来之后进行对比
- 要是把语言模型改造成双向就好
- 不太会炒作，GPT也是非常重要的工作




# Bert的诞生

相同的两阶段模型
- 语言模型预训练
- Fine-Tuning模式解决下游任务

同样面临夏有任务的网络结构改造的问题


对于种类如此繁多而且各具特点的下游NLP任务，Bert如何改造输入输出部分使得大部分NLP任务都可以使用Bert预训练好的模型参数呢？上图给

encoder的部分作为一个深度的transformer结构，decoder的部分同样对应一个transformer结构






# 图像中的预训练

预训练本身有关的问题
- 训练数据小，不够处理复杂网络
- 加快训练速度
- 参数初始化，找到好的参数初始化点，有利于优化

首先的阶段
- 可以先用某个训练集合比如训练集合A或者训练集合B对这个网络进行预先训练，在A任务上或者B任务上学会网络参数，然后存起来以备后用。

接着面临第三个任务C
- 网络结构采取相同的网络结构，在比较浅的几层CNN结构，网络参数初始化的时候可以加载A任务或者B任务学习好的参数，其它CNN高层参数仍然随机初始化。

两种随后的思路
- 浅层加载的参数在训练C任务过程中不动，这种方法被称为“Frozen”
- 底层网络参数尽管被初始化了，在C任务训练过程中仍然随着训练的进程不断改变，这种一般叫“Fine-Tuning”

那么为什么预训练这件事在图像领域中是可行的呢？
- 正因为此，所以预训练好的网络参数，尤其是底层的网络参数抽取出特征跟具体任务越无关，越具备任务的通用性，所以这是为何一般用底层预训练好的参数初始化新任务网络参数的原因。
- 高层特征跟任务关联较大，实际可以不用使用，或者采用Fine-tuning用新数据集合清洗掉高层无关的特征抽取器。



# 来自Word Embedding的考古史

## 语言模型
核心函数P的思想是根据句子里面前面的一系列前导单词预测后面跟哪个单词的概率大小（理论上除了上文之外，也可以引入单词的下文联合起来预测单词出现概率）。

NNLM的网络思路，得到具体的Word embedding值


Word2Vec
- CBOW:核心思想是从一个句子里面把一个词抠掉，用这个词的上文和下文去预测被抠掉的这个词
- Skip-gram:入某个单词，要求网络预测它的上下文单词

对于NNLM：输入一个单词的上文，去预测这个单词

区别在于
- NNLM的主要任务是要学习一个解决语言模型任务的网络结构，语言模型就是要看到上文预测下文，而word embedding只是无心插柳的一个副产品。
- Word2Vec目标不一样，它单纯就是要word embedding的，这是主产品，所以它完全可以随性地这么去训练网络

## word embedding的使用方式
句子中每个单词以Onehot形式作为输入，然后乘以学好的Word Embedding矩阵Q，就直接取出单词对应的Word Embedding了

类似于look-up查表操作

同样的NLP任务早使用word embedding时候也有两种不同的做法
- frozen
- fine-tuning

关键问题是word embedding存在一些问题：多义词问题


# 从Word Embedding到ELMO

Deep contextualized word representation

之前的word embedding本质上是一种静态方式，ELMO本质上为动态的过程，ELMO本身是个根据当前上下文对Word Embedding动态调整的思路。

两阶段的过程
- 第一个阶段是利用语言模型进行预训练；
- 第二个阶段是在做下游任务时，从预训练网络中提取对应单词的网络各层的Word Embedding作为新特征补充到下游任务中。

## ELMO的结构进一步探索
ELMO的预训练过程不仅仅学会单词的Word Embedding，还学会了一个双层双向的LSTM网络结构

会得到三阶段的embedding的表征
- 最底层是单词的Word Embedding
- 第一层双向LSTM中对应单词位置的Embedding：更多的句法信息
- 第二层LSTM中对应单词位置的Embedding：更多的语义信息

下游任务使用的word embedding有上述三种embedding结合在一起
- 每个部分对应一个权重
- ELMO给下游提供的是每个单词的特征形式，所以这一类预训练的方法被称为“Feature-based Pre-Training”
- 