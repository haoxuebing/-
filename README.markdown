
这是一个项目使用seq2seq模型来玩对联（对对联）。这个项目是用Tensorflow编写的。您可以在https://ai.binwang.me/couplet上试用该演示。

前要求
--------------

* Tensorflow
* Python 3.6
* Dataset


Dataset
-----------

您将需要一些数据来运行此程序，可以从此项目下载数据集。

**注意：如果您使用自己的数据集，则需要在vocabs文件中添加<s>并<\s>作为前两行。**

用法
------------

### 培养

打开couplet.py并配置文件位置和hyperparams。然后跑去python couplet.py训练模型。你可以在Tensorbloard看到训练损失和蓝色分数。learning_rate当您发现丢失停止时，您可能需要重新配置。以下是损失图的示例：

![loss graph](https://user-images.githubusercontent.com/1906051/36624881-50586e54-1950-11e8-8383-232763831cbc.png)

如果你停止训练并想继续训练它。您可以设置restore_model到True和使用的m.train(<epoches>, start=<start>)，这start是你已经运行的步骤。

我在Nivida GTX-1080 GPU上训练模型大约4天。


### 运行训练的模型

打开server.py并配置vocab_file和model_dirparams。然后运行python server.py将启动可以播放联接的Web服务。

例子
-------------

以下是此模型生成的一些示例：

| 上联                        | 下联                |
|-----------------------------|--------------------|
| 殷勤怕负三春意                | 潇洒难书一字愁        |
| 如此清秋何吝酒                | 这般明月不须钱        |
| 天朗气清风和畅                | 云蒸霞蔚日光辉        |
| 梦里不知身是客                | 醉时已觉酒为朋        |
| 千秋月色君长看                | 一夜风声我自怜        |
