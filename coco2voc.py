'''
安装依赖：
!git clone https://gitee.com/yanxin_thomas/cocoapi.git
%cd cocoapi/PythonAPI/
!make
!python setup.py install
!pip install lxml
'''

'''
修改部分
# 转换后的VOC存放地址
CKimg_dir ='/home/aistudio/dataset/VOC/images'
CKanno_dir = '/home/aistudio/dataset/VOC/annotations'

def get_CK5(origin_anno_dir,origin_image_dir,verbose=False):
    dataTypes = ['train2017']   #需要根据COCO数据集作具体修改
    for dataType in dataTypes:
        annFile = 'train.json'
        annpath=os.path.join(origin_anno_dir,annFile)
        coco = COCO(annpath)
        classes = catid2name(coco)
        imgIds = coco.getImgIds()
        # imgIds=imgIds[0:1000]#测试用，抽取10张图片，看下存储效果
        for imgId in tqdm(imgIds):
            img = coco.loadImgs(imgId)[0]
            showbycv(coco, dataType, img, classes,origin_image_dir,verbose=False)
            
def main():
    base_dir='/home/aistudio/dataset/VOC'#step1 这里是一个新的文件夹，存放转换后的图片和标注
    image_dir=os.path.join(base_dir,'JPEGImages')#在上述文件夹中生成JPEGImages，Annotations两个子文件夹
    anno_dir=os.path.join(base_dir,'Annotations')
    mkr(image_dir)
    mkr(anno_dir)
    origin_image_dir='/home/aistudio/dataset/train/images'#step 2原始的coco的图像存放位置
    origin_anno_dir='/home/aistudio/dataset/train/annotations'#step 3 原始的coco的标注存放位置
    verbose=True #是否需要看下标记是否正确的开关标记，若是true,就会把标记展示到图片上
    get_CK5(origin_anno_dir,origin_image_dir,verbose)
'''

from pycocotools.coco import COCO #这个包可以从git上下载https://github.com/cocodataset/cocoapi/tree/master/PythonAPI，也可以直接用修改后的coco.py
import  os, cv2, shutil
from lxml import etree, objectify
from tqdm import tqdm
from PIL import Image
 
# 转换后的VOC存放地址
CKimg_dir ='/home/aistudio/dataset/VOC/images'
CKanno_dir = '/home/aistudio/dataset/VOC/annotations'

#若模型保存文件夹不存在，创建模型保存文件夹，若存在，删除重建
def mkr(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)
 
 
def save_annotations(filename, objs,filepath):
    annopath = CKanno_dir + "/" + filename[:-3] + "xml" #生成的xml文件保存路径
    dst_path = CKimg_dir + "/" + filename
    img_path=filepath
    img = cv2.imread(img_path)
    im = Image.open(img_path)
    if im.mode != "RGB":
        print(filename + " not a RGB image")
        im.close()
        return
    im.close()
    shutil.copy(img_path, dst_path)#把原始图像复制到目标文件夹
    E = objectify.ElementMaker(annotate=False)
    anno_tree = E.annotation(
        E.folder('1'),
        E.filename(filename),
        E.source(
            E.database('CKdemo'),
            E.annotation('VOC'),
            E.image('CK')
        ),
        E.size(
            E.width(img.shape[1]),
            E.height(img.shape[0]),
            E.depth(img.shape[2])
        ),
        E.segmented(0)
    )
    for obj in objs:
        E2 = objectify.ElementMaker(annotate=False)
        anno_tree2 = E2.object(
            E.name(obj[0]),
            E.pose(),
            E.truncated("0"),
            E.difficult(0),
            E.bndbox(
                E.xmin(obj[2]),
                E.ymin(obj[3]),
                E.xmax(obj[4]),
                E.ymax(obj[5])
            )
        )
        anno_tree.append(anno_tree2)
    etree.ElementTree(anno_tree).write(annopath, pretty_print=True)
 
 
def showbycv(coco, dataType, img, classes,origin_image_dir,verbose=False):
    filename = img['file_name']
    filepath=os.path.join(origin_image_dir,dataType,filename)
    I = cv2.imread(filepath)
    annIds = coco.getAnnIds(imgIds=img['id'],  iscrowd=None)
    anns = coco.loadAnns(annIds)
    objs = []
    for ann in anns:
        name = classes[ann['category_id']]
        if 'bbox' in ann:
            bbox = ann['bbox']
            xmin = (int)(bbox[0])
            ymin = (int)(bbox[1])
            xmax = (int)(bbox[2] + bbox[0])
            ymax = (int)(bbox[3] + bbox[1])
            obj = [name, 1.0, xmin, ymin, xmax, ymax]
            objs.append(obj)
            if verbose:
                cv2.rectangle(I, (xmin, ymin), (xmax, ymax), (255, 0, 0))
                cv2.putText(I, name, (xmin, ymin), 3, 1, (0, 0, 255))
    save_annotations(filename, objs,filepath)
    if verbose:
        cv2.imshow("img", I)
        cv2.waitKey(0)
 
 
def catid2name(coco):#将名字和id号建立一个字典
    classes = dict()
    for cat in coco.dataset['categories']:
        classes[cat['id']] = cat['name']
        # print(str(cat['id'])+":"+cat['name'])
    return classes
 
 
def get_CK5(origin_anno_dir,origin_image_dir,verbose=False):
    dataTypes = ['train2017']   #需要根据COCO数据集作具体修改
    for dataType in dataTypes:
        annFile = 'train.json'
        annpath=os.path.join(origin_anno_dir,annFile)
        coco = COCO(annpath)
        classes = catid2name(coco)
        imgIds = coco.getImgIds()
        # imgIds=imgIds[0:1000]#测试用，抽取10张图片，看下存储效果
        for imgId in tqdm(imgIds):
            img = coco.loadImgs(imgId)[0]
            showbycv(coco, dataType, img, classes,origin_image_dir,verbose=False)
 
def main():
    base_dir='/home/aistudio/dataset/VOC'#step1 这里是一个新的文件夹，存放转换后的图片和标注
    image_dir=os.path.join(base_dir,'JPEGImages')#在上述文件夹中生成JPEGImages，Annotations两个子文件夹
    anno_dir=os.path.join(base_dir,'Annotations')
    mkr(image_dir)
    mkr(anno_dir)
    origin_image_dir='/home/aistudio/dataset/train/images'#step 2原始的coco的图像存放位置
    origin_anno_dir='/home/aistudio/dataset/train/annotations'#step 3 原始的coco的标注存放位置
    verbose=True #是否需要看下标记是否正确的开关标记，若是true,就会把标记展示到图片上
    get_CK5(origin_anno_dir,origin_image_dir,verbose)
 
if __name__ == "__main__":
    main()