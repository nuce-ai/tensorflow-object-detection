import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import argparse
import sys
# Initialize parser with a short description
parser = argparse.ArgumentParser(description='Compress a file using various algorithms')

# Add positional and optional arguments
parser.add_argument('input_file', help=' Đường dẫn thư mục chứa file *.xml')
# E:\nuce-ai\Tensorflow\workspace\training\images\test\root\xml

parser.add_argument('output_file', help='Đường dẫn lưu file *.csv')
# E:\nuce-ai\Tensorflow\workspace\training\images\train\root\csv\train.csv

# Parse argument
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file 

def xml_to_csv(path):

    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def main():
    xml_df = xml_to_csv(input_file)
    
    xml_df.to_csv(output_file, index=None)
    print('Successfully converted xml to csv.')
if __name__== "__main__":
    main()