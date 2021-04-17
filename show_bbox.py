import os
import xml.etree.cElementTree as et
import cv2
import numpy as np

if __name__ == "__main__":
    path = "./images/"

    for file in os.listdir(path):

        if ".jpg" in file:# 过滤 xml 文件

            path_img = path + file # 图片路径

            path_xml = path_img.replace('.jpg','.xml').replace('.png','.xml') # 标注文件路径

            tree=et.parse(path_xml) # 读取标注文件
            root=tree.getroot()

            img = cv2.imread(path_img) # 读取图片

            for Object in root.findall('object'):
                label = Object.find('name').text

                bndbox=Object.find('bndbox') # 解析标注文件的矩形框的左上坐标（xmin,ymin）,右下坐标（xmax,ymax）
                xmin= np.float32((bndbox.find('xmin').text))
                ymin= np.float32((bndbox.find('ymin').text))
                xmax= np.float32((bndbox.find('xmax').text))
                ymax= np.float32((bndbox.find('ymax').text))

                cv2.rectangle(img, (int(xmin),int(ymin)), (int(xmax),int(ymax)), (255,0,0), 2) # 绘制矩形框
                cv2.putText(img, label, (int(xmin),int(ymin)),cv2.FONT_HERSHEY_DUPLEX, 0.85, (5, 160, 250),2)# 绘制标签

            cv2.namedWindow("image",0)
            cv2.imshow("image",img)
            if cv2.waitKey(0) == 27:
                break
        cv2.destroyAllWindows()
