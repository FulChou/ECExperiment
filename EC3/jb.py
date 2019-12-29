import jieba
string = open('paper','r',encoding='UTF-8').read()
result = jieba.lcut(string)
print(len(result), '/'.join(result))

