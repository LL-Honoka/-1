import jieba
import jieba.analyse
from pmi import *
import re
input_file_name = '外卖评论.csv'
documents = []

def read_csv(input_file_name):
    """
    读取外卖评论.csv的数据,并计算pmi
    """
    f = open(input_file_name, 'r')
    data = f.readlines()
    if data is not None:
        for sentence in data:
            extractwords = []
            re.sub('\[.*?\]', '', sentence) #去掉标点符号
            words = jieba.cut(sentence)
            wordlist = []
            for word in words:
                wordlist.append(word)
            sentence = ','.join(wordlist)
            words = jieba.analyse.extract_tags(sentence, 5)
            for word in words:
                extractwords.append(word)
            documents.append(set(extractwords))
    pm = PMI(documents)
    pmi = pm.get_pmi()
    return pmi
    f.close()
pmi_document = read_csv(input_file_name)
pmi_document.items()
pmi_list = list(pmi_document.items())
pmi_list.sort(key=lambda x:x[1],reverse=True)
print("最具有正向情感的50词:")
for i in range(50):
    print(str(pmi_list[i]))
print("最具有负向情感的词:")
for i in range(50):
    print(str(pmi_list[len(pmi_list) - i - 1]))


