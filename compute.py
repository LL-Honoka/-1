import jieba
import csv

input_file_name = '外卖评论.csv'

def read_csv(input_file_name):
    """
    读取外卖评论.csv的数据
    """
    with open(input_file_name,'r',encoding='utf-8') as csv_file:
       csv_reader = csv.reader(csv_file)
       csv_file.close()

def save_csv(target_list, output_file_name):
    """
    将数据写入csv文件
    """

