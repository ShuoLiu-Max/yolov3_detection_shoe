import os
import shutil
import random 

def split_data(yolo_data_path):
    """
        copy document that in yolo_data_path to new_path
    """
    list_names = os.listdir(yolo_data_path)
    cwd = os.getcwd()
    print(cwd)
    for i in list_names:
        random_num = random.randint(1,10)
        if (random_num==1) | (random_num==2):
            if i.endswith('JPEG'):
                shutil.copy(cwd+"\\"+yolo_data_path+"\\"+i,"data\\shoe\\images\\val")
                shutil.copy(cwd+"\\"+yolo_data_path+"\\"+i.replace('JPEG','txt'),"data\\shoe\\labels\\val")
        else:
            if i.endswith('JPEG'):
                shutil.copy(cwd+"\\"+yolo_data_path+"\\"+i,"data\\shoe\\images\\train")
                shutil.copy(cwd+"\\"+yolo_data_path+"\\"+i.replace('JPEG','txt'),"data\\shoe\\labels\\train")


def create_document_path(path,dest_path):
    list_names = os.listdir(path)
    with open(dest_path,'a+',encoding='utf-8') as f:
        for i in list_names:
            f.write("C:/Users/DELL/Desktop/yolov3-shoedec"+"/"+path+"/"+i+'\n')




# create_document_path(path="data/shoe/images/train",dest_path="data/shoe/trainvalno5k.txt")

# split_data("shoe_yolo_dataset")

