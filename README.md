# Tianchi-PANDA-rank13
PANDA大场景多对象检测跟踪（初赛检测）开源代码，初赛排名13

# 本文禁止转载！
作者的其他主页：
> B站：[https://space.bilibili.com/470550823](https://space.bilibili.com/470550823)

> CSDN：[https://blog.csdn.net/weixin_44936889](https://blog.csdn.net/weixin_44936889)

> AI Studio：[https://aistudio.baidu.com/aistudio/personalcenter/thirdview/67156](https://aistudio.baidu.com/aistudio/personalcenter/thirdview/67156)

> Github：[https://github.com/Sharpiless](https://github.com/Sharpiless)

# 比赛地址：
比赛地址：[https://tianchi.aliyun.com/competition/entrance/531855/rankingList](https://tianchi.aliyun.com/competition/entrance/531855/rankingList)

# 排名截图：
![enter image description here](https://img-blog.csdnimg.cn/img_convert/485fa695e82276c7c11b54db4c842799.png)
周周星就是：在每个赛道的初赛阶段，设立周周星奖励：从初赛第三周开始，以每周一中午12点的排行榜为准，取前两名参赛队伍发放周周星纪念礼物；对于前面已经获得周周星的队伍，不重复发放，名额按名次顺延。

白嫖了一个耳机和一个手环：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210316071408990.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20210316071459253.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDkzNjg4OQ==,size_16,color_FFFFFF,t_70)


# 使用算法：

这里我使用 Yolov5


# 数据预处理：

## 图像分割：
由于原图很大，我们首先对数据集进行分割，按照两个比例：1/4和1/16切割原图，并过滤掉较小的目标（实际过滤掉长或者宽<5像素的目标）。

注意到 full body 切割后应修正为 visible body 对提高分数有很大的帮助。


## 有重叠的滑窗：
由于直接切割会导致很多目标被分离，因此我们使用overlap为0.2的滑窗采样：
![enter image description here](https://img-blog.csdnimg.cn/img_convert/9fd3566c89496bf3d9ca2b91a4929aef.png)
![enter image description here](https://img-blog.csdnimg.cn/img_convert/dd568fb744289e1f20c9a9c8888bccad.png)
![enter image description here](https://img-blog.csdnimg.cn/img_convert/846807e379965802ba4bce0ddfba7b9b.png)
![enter image description here](https://img-blog.csdnimg.cn/img_convert/2c2d87c15ec7bcc8236a50880fbe6721.png)
## 多模型预测：
由于visible body跟full body在大多数情况下是重合的，他们的IOU也很大，导致一个模型检测效果较差，因此我们训练了两个模型，一个用于检测vehicle+visible body，一个用于检测full body+head：
![enter image description here](https://img-blog.csdnimg.cn/img_convert/21d67bd02341b231a8d6d1bc4c0c1ae3.png)
![enter image description here](https://img-blog.csdnimg.cn/img_convert/e857b611633169c24ac9753938e9ff97.png)

# 数据增强：
数据增强我们主要使用了 imgaug 这个库：
![enter image description here](https://img-blog.csdnimg.cn/img_convert/fc35ae93443281cebd3b8564d12f2d09.png)
# 预训练模型：
我们使用了在COCO目标检测训练的权重作为预训练模型。

# 后续思路：
- 1. 可以尝试知识蒸馏的方法，并可以通过模型量化剪枝等操作加快推理速度，融合更多模型。
- 2. 可以将滑窗预测改成批处理，加快推理速度。

# 联系作者：
微信号：Sharpiless

# 我的公众号：

![](https://img-blog.csdnimg.cn/img_convert/246d5540ce9ebe63f6a25c5e8ab5bc6e.png)
