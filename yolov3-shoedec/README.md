# 基于yolov3关于鞋的单目标检测

## 关于鞋的小数据集数已经配置，在文件中：
## train: data/shoe/images/train
## val: data/shoe/images/val

## 执行train.py 训练模型，每轮保存模型训练结果

## 在detct.py中可加载训练的模型，用于检测

## 在代码中添加了anchors的聚类代码，utils/anchors_kmeans.py：anchors/anchors9.txt