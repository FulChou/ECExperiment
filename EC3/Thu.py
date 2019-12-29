import thulac

string = open('paper','r',encoding='UTF-8').read()

t = thulac.thulac()
result = t.cut(string)
print(len(result),result)
