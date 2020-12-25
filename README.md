# 数据集标注软件

- [labelImg](https://github.com/tzutalin/labelImg/)
- [labelMe](https://github.com/wkentaro/labelme)
- [精灵标注助手](http://www.jinglingbiaozhu.com/)

更多的标注工具你可以去看：[深度学习图像标注工具汇总](https://zhangxu.blog.csdn.net/article/details/79036312?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.compare&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.compare) 、 [十个最常用深度学习图像/视频数据标注工具](https://blog.csdn.net/PAN_Andy/article/details/99283490?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.compare&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.compare) 、 [百度一下](https://baidu.com)

> 在这里我选择使用**labelImg**

> 数据集大小重置工具：`Image_tool.exe` [百度网盘下载（提取码：2tmv）](https://pan.baidu.com/s/1I9RDnfClspl4iZhBPp_0lw )


# 数据集标注

1. 下载[labelImg](https://github.com/tzutalin/labelImg/releases)
2. 解压，直接打开`labelimg.exe`
3. [labelImg标注数据](https://blog.csdn.net/shuiyixin/article/details/82623613)

> 标注完成后即可获得`VOC`格式（*生成.xml文件*）的数据

```html
dataset
│
├─Annotations
│      train_29635.xml
│      train_29641.xml
│      train_30090.xml
│	   ...
│
└─JPEGImages
        train_29635.jpg
        train_29641.jpg
        train_30090.jpg
        ...

```

# yolov5数据集制作

## 1.voc格式数据集转化yolov5格式数据集

运行`voc_to_yoloV5.py`【该脚本实现将`voc`格式的数据转化为`yoloV5`需要的`.txt`标注文件,运行该脚本，会在`dataset/voc/`目录下生成 `worktxt/`目录(`yolo`需要的格式)】

> 运行代码之前，修改里面相关文件路径。

```html
dataset
│
├─Annotations
│      train_29635.xml
│      train_29641.xml
│      train_30090.xml
│	   ...
│
├─JPEGImages
│       train_29635.jpg
│       train_29641.jpg
│       train_30090.jpg
│       ...
│
└─worktxt
       train_29635.txt
       train_29641.txt
       train_30090.txt
 	   ...
```

## 2.数据集划分训练、测试、验证

运行`voc_split_trainValTest.py`【该脚本用于生成voc/目录下的ImageSets/..目录,分割了训练和验证集】

```html
dataset
│
├─Annotations
│      train_29635.xml
│      train_29641.xml
│      train_30090.xml
│	   ...
│
├─ImageSets
│	└─Main
│      train.txt
│      test.txt
│      valid.txt
│      img_train.txt
│      img_test.txt
│      img_valid.txt
│
├─JPEGImages
│       train_29635.jpg
│       train_29641.jpg
│       train_30090.jpg
│       ...
│
└─worktxt
       train_29635.txt
       train_29641.txt
       train_30090.txt
 	   ...
```

## 3.重构数据集

运行`dataset_cg.py`【该脚本将会生成yolov5可以训练的数据布局】

主要进行一个`copy`或者`move`的操作：
```python
# 小数据建议：copy 大数据建议：move
for i in range(len(img_txt_cg_train)):
    shutil.copy(fimg+str(img_txt_cg_train[i]),new_dataset_train)
    shutil.copy(flable+str(label_txt_cg_train[i]),new_dataset_trainl)
for j in range(len(img_txt_cg_test)):
    shutil.copy(fimg+str(img_txt_cg_test[j]),new_dataset_test)
    shutil.copy(flable+str(label_txt_cg_test[j]),new_dataset_testl)
for q in range(len(img_txt_cg_valid)):
    shutil.copy(fimg+str(img_txt_cg_valid[q]),new_dataset_valid)
    shutil.copy(flable+str(label_txt_cg_valid[q]),new_dataset_validl)
```

```html
dataset
│
├─Annotations
│      train_29635.xml
│      train_29641.xml
│      train_30090.xml
│	   ...
│
├─ImageSets
│	└─Main
│      train.txt
│      test.txt
│      valid.txt
│      img_train.txt
│      img_test.txt
│      img_valid.txt
│
├─data
│   ├─train
│   ├─test
│   └─valid
│
├─JPEGImages
│       train_29635.jpg
│       train_29641.jpg
│       train_30090.jpg
│       ...
│
└─worktxt
       train_29635.txt
       train_29641.txt
       train_30090.txt
 	   ...
```

## 4.开始利用yolov5训练你的数据

```git
git clone https://github.com/ultralytics/yolov5.git
```

# 参考

- https://github.com/DLLXW/objectDetectionDatasets

