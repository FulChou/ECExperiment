import numpy as np
import operator

def createDataset():
    #四组二维特征
    group = np.array([[7,7],[7,4],[3,4],[1,4]])
    #四组对应标签
    labels = ('坏','坏','好','好')
    return group,labels

def classify(intX,dataSet,labels,k):
    '''
    KNN算法
    '''
    #numpy中shape[0]返回数组的行数，shape[1]返回列数
    dataSetSize = dataSet.shape[0]
    #将intX在横向重复dataSetSize次，纵向重复1次
    #例如intX=([1,2])--->([[1,2],[1,2],[1,2],[1,2]])便于后面计算
    diffMat = np.tile(intX,(dataSetSize,1))-dataSet
    #二维特征相减后乘方
    sqdifMax = diffMat**2
    #计算距离
    seqDistances = sqdifMax.sum(axis=1)
    distances = seqDistances**0.5
    print ("待测样本与各已知样本距离:",distances)
    #返回distance中元素从小到大排序后的索引
    sortDistance = distances.argsort()
    print ("各元素距离由小到大排序后索引:",sortDistance)
    classCount = {}
    for i in range(k):
        #取出前k个元素的类别
        voteLabel = labels[sortDistance[i]]
        print ("第%d个近邻样本品质为:%s" % (i+1,voteLabel))
        classCount[voteLabel] = classCount.get(voteLabel,0)+1
    #dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
    #计算类别次数

    #key=operator.itemgetter(1)根据字典的值进行排序
    #key=operator.itemgetter(0)根据字典的键进行排序
    #reverse降序排序字典
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    print ("结果统计:",sortedClassCount)
    return ("该样本品质：%s" % sortedClassCount[0][0])

if __name__ == '__main__':
    group,labels = createDataset()
    test = [3,7]
    test_class = classify(test,group,labels,3)
    print (test_class)
