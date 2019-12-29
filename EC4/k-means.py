import numpy as np
import matplotlib.pyplot as plt

'''标志位统计递归运行次数'''
flag = 0

'''欧式距离'''
def ecludDist(x, y):
    return np.sqrt(sum(np.square(np.array(x) - np.array(y))))

'''计算簇的均值点'''
def clusterMean(dataset):
    return sum(np.array(dataset)) / len(dataset)

'''生成随机均值点'''
def randCenter(dataset, k):
    temp = []
    while len(temp) < k:
        index = np.random.randint(0, len(dataset)-1)
        if  index not in temp:
            temp.append(index)
    return np.array([dataset[i] for i in temp])

'''以前k个点为均值点'''
def orderCenter(dataset, k):
    return np.array([dataset[i] for i in range(k)])

'''聚类'''
def kMeans(dataset, dist, center, k):
    global flag
    #all_kinds用于存放中间计算结果
    all_kinds = []
    for _ in range(k):
        temp = []
        all_kinds.append(temp)
    #计算每个点到各均值点的距离
    for i in dataset:
        temp = []
        for j in center:
            temp.append(dist(i, j))
        all_kinds[temp.index(min(temp))].append(i)
    #打印中间结果
    for i in range(k):
        print('第'+ str(i) +'组:', all_kinds[i], end='\n')
    flag += 1
    print('************************迭代'+str(flag)+'次***************************')
    #更新均值点
    center_ = np.array([clusterMean(i) for i in all_kinds])
    if (center_ == center).all():
        print('结束')
        for i in range(k):
            print('第'+str(i)+'组均值点：', center_[i], end='\n')
            plt.scatter([j[0] for j in all_kinds[i]], [j[1] for j in all_kinds[i]], marker='*')
        plt.grid()
        plt.show()
    else:
        #递归调用kMeans函数
        center = center_
        kMeans(dataset, dist, center, k)

def main(k):
    '''随机生成100个坐标点'''
    x = [np.random.randint(0, 50) for _ in range(100)]
    y = [np.random.randint(0, 50) for _ in range(100)]
    points = [[i,j] for i, j in zip(x, y)]
    plt.plot(x, y, 'b.')
    plt.show()
    initial_center = randCenter(dataset=points, k=k)
    kMeans(dataset=points, dist=ecludDist, center=initial_center, k=k)

if __name__ == '__main__':
    main(5)
