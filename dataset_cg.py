import os
import shutil

# 获取分割好的train\test\valid名称
img_txt_cg_train = []
img_txt_cg_test = []
img_txt_cg_valid = []
label_txt_cg_train = []
label_txt_cg_test = []
label_txt_cg_valid = []

path = 'dataset/voc/ImageSets/Main/'

for line in open(path+"img_train.txt"):
    line=line.strip('\n')
    img_txt_cg_train.append(line)
for line1 in open(path+"img_test.txt"):
    line1=line1.strip('\n')
    img_txt_cg_test.append(line1)
for line2 in open(path+"img_valid.txt"):
    line2=line2.strip('\n')
    img_txt_cg_valid.append(line2)

for line3 in open(path+"train.txt"):
    line3=line3.strip('\n')
    label_txt_cg_train.append(line3)
for line4 in open(path+"test.txt"):
    line4=line4.strip('\n')
    label_txt_cg_test.append(line4)
for line5 in open(path+"valid.txt"):
    line5=line5.strip('\n')
    label_txt_cg_valid.append(line5)

# 建立cg数据的文件夹
new_dataset_train = 'dataset/voc/data/train/images/'
new_dataset_test = 'dataset/voc/data/test/images/'
new_dataset_valid = 'dataset/voc/data/valid/images/'

new_dataset_trainl = 'dataset/voc/data/train/labels/'
new_dataset_testl = 'dataset/voc/data/test/labels/'
new_dataset_validl = 'dataset/voc/data/valid/labels/'

if not os.path.exists(new_dataset_train):
    os.makedirs(new_dataset_train)
if not os.path.exists(new_dataset_test):
    os.makedirs(new_dataset_test)
if not os.path.exists(new_dataset_valid):
    os.makedirs(new_dataset_valid)
if not os.path.exists(new_dataset_trainl):
    os.makedirs(new_dataset_trainl)
if not os.path.exists(new_dataset_testl):
    os.makedirs(new_dataset_testl)
if not os.path.exists(new_dataset_validl):
    os.makedirs(new_dataset_validl)

# cg移动
fimg = 'dataset/voc/JPEGImages/'
flable = 'dataset/voc/worktxt/'

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
        
