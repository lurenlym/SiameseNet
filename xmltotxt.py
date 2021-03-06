import os
import sys
import xml.etree.ElementTree as ET
import glob

def xml_to_txt(indir,outdir):

    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')

    for i, file in enumerate(annotations):

        file_save = file.split('.')[0]+'.txt'
        file_txt=os.path.join(outdir,file_save)
        f_w = open(file_txt,'w',encoding='gbk')

        # actual parsing
        in_file = open(file)
        tree=ET.parse(in_file)
        root = tree.getroot()

        for obj in root.iter('object'):
                current = list()
                name = obj.find('name').text

                xmlbox = obj.find('bndbox')
                xn = xmlbox.find('xmin').text
                xx = xmlbox.find('xmax').text
                yn = xmlbox.find('ymin').text
                yx = xmlbox.find('ymax').text
                #print xn
                f_w.write(xn+' '+yn+' '+xx+' '+yx+' ')
                f_w.write(name+'\n')
root = 'E:\\liuyuming\\SiameseNet\\DATA\\WH180605\\L\\'
dataset = 'VAL5'

indir=root+'gtxml\\'+dataset
outdir=root+'gttxt\\'+dataset  #txt目录

xml_to_txt(indir,outdir)
