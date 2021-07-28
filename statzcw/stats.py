from statistics import variance
from typing import List
import math
def zcount(list: List[float]) -> float:
    return len(list)
    #print("stat test")
    #print("zcount should 5=="), zcount ([1.0,2.0,3.0,4.0,5.0]) 

def zmean(list: List[float]) -> float:
    return sum(list) / zcount(list)
    
def zmode(list: List[float]) -> float:
    return max(set(list) , key = list.count)
    
def zmedian(list: List[float]) -> float:
    sortedlst = sorted(list)
    lstlen = len(list)
    index = (lstlen - 1) //2
    if(lstlen %2):
        return sortedlst[index]
    else:
        return (sortedlst[index] + sortedlst[index +1])/2.0

def zvariance(list: List[float]) -> float:
    n = zcount(list) - 1
    mean = zmean(list)
    deviation = [abs(mean - xi) ** 2 for xi in list]
    variance = sum(deviation) / n


def zstddev(list: List[float]) -> float:

    var = zvariance(list)

    return math.sqrt(var)


def zstderr(list: List[float]) -> float:

    sd = zstddev(list)
    n = zcount(list)

    return sd / math.sqrt(n)


def zcov(listx: List[float], listy: List[float]) -> float:

    n = zcount(listx)
    sum_of_product = 0
    counter = 0

    while counter < len(listx):
        product = listx[counter] * listy[counter]
        sum_of_product += product
        counter += 1

    sums = (sum(listx) * sum(listy)) / n

    cov = (sum_of_product - sums) / (n - 1)
    return cov


def zcorr(listx: List[float], listy: List[float]) -> float:

    cov = zcov(listx, listy)
    sx = zstddev(listx)
    sy = zstddev(listy)

    return (cov) / (sx * sy)

def readDataSet(files):
#    print("in readDataSets...", files)
    data = {}
    for file in files:
        twoLists = readDataSet(file)
        data[file] = twoLists    
    return data

def readDataFile(fname):
    x,y =  ([],[])
    with open(file) as f:
        first_line = f.readline() #consume headers
        for l in f:
            row = l.split(',')
            print(row, type (row))
            x.append(float(row[0]))
            y.append(float(row[1]))
        return (x,y)