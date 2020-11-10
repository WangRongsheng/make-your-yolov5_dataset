import os
import random
import sys


root_path = 'dataset/voc'
xmlfilepath = root_path + '/Annotations'
txtsavepath = root_path + '/ImageSets/Main'


if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

train_test_percent = 0.9  # (训练集+验证集)/(训练集+验证集+测试集)
train_valid_percent = 0.9  # 训练集/(训练集+验证集)

total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * train_test_percent)   # 训练集+验证集数量
ts = int(num-tv)   # 测试集数量
tr = int(tv * train_valid_percent)  # 验证集数量
tz = int(tv-tr)   # 训练集数量
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

print("train and valid size:", tv)
print("train size:", tz)
print("test size:", ts)
print("valid size:", tr)

# ftrainall = open(txtsavepath + '/ftrainall.txt', 'w')
ftest = open(txtsavepath + '/test.txt', 'w')
ftrain = open(txtsavepath + '/train.txt', 'w')
fvalid = open(txtsavepath + '/valid.txt', 'w')

ftestimg = open(txtsavepath + '/img_test.txt', 'w')
ftrainimg = open(txtsavepath + '/img_train.txt', 'w')
fvalidimg = open(txtsavepath + '/img_valid.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '.txt' + '\n'
    imgname = total_xml[i][:-4] + '.jpg' + '\n'
    if i in trainval:
        # ftrainall.write(name)
        if i in train:
            ftrain.write(name)
            ftrainimg.write(imgname)
        else:
            fvalid.write(name)
            fvalidimg.write(imgname)
    else:
        ftest.write(name)
        ftestimg.write(imgname)

# ftrainall.close()
ftrain.close()
fvalid.close()
ftest.close()

ftrainimg.close()
fvalidimg.close()
ftestimg.close()
