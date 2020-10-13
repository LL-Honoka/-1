import jieba

input_file_name = '外卖评论.csv'
data = []

def read_csv(input_file_name):
    """
    读取外卖评论.csv的数据
    """
    with open(input_file_name) as csv_file:
       for line in csv_file.readlines():
            seg_list = jieba.cut(line)
            data.append("/".join(seg_list))
       csv_file.close()

read_csv(input_file_name)
output_file_name = open('csv_test.csv','w')

def save_csv(data, output_file_name):
    """
    将数据写入csv文件
    """
    output_file_name.writelines(data)
    output_file_name.close()

save_csv(data, output_file_name)
