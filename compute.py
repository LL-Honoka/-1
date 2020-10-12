import jieba
import csv

input_file_name = '外卖评论.csv'
data = []

def read_csv(input_file_name):
    """
    读取外卖评论.csv的数据
    """
    with open(input_file_name,'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       for line in csv_reader:
            seg_list = jieba.lcut(line)
            data.append(seg_list)
       csv_file.close()

read_csv(input_file_name)
output_file_name = open('csv_test.csv','w')

def save_csv(data, output_file_name):
    """
    将数据写入csv文件
    """
    writer = csv.writer(output_file_name)
    writer.writerows(data)
    output_file_name.close()

save_csv(data, output_file_name)
