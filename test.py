import os
import re
import math
docwise={}
TFd={}
TFq={}
IDF={}
idfq={}
idfd={}
results={}
inlink={}
number_of_files=0
cntrlty=[]
#######
def tfquery(query):
    wordcount = {}
    totalword=0
    for word in query.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
        totalword+=1
    for c in wordcount:
        #print(c)
        TFq[c]=wordcount[c]/totalword
    #print(TFq)
def each_query(query):
    img_folder_path = "C:\\Users\\Aman Goyal\\PycharmProjects\\Web minning\\HTML"
    dirListing = os.listdir(img_folder_path)
    global number_of_files
    number_of_files = len(dirListing)
    totaloccur=0
    for word in query.split():
        if word not in TFd:
            TFd[word] = 1
        if word not in IDF:
            IDF[word] = 1

    for y in TFd:
        #print(y)
        firststep = {}
        idf=0
        totaloccur=0
        for i in range(number_of_files):
            file = "HTML\\" + dirListing[i]
            f = open(file, "r")
            x = f.read().lower()
            occur = 0;
            totalword = 0;
            wordcount = {}
            for word in x.split():
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
                totalword += 1
            for c in wordcount:
                if c == y:
                    occur = wordcount[c]
            if occur != 0:
                totaloccur += 1
            firststep[dirListing[i]] = occur / totalword
           ###############
        ##tf  done in TFd now idf in IDF

        if totaloccur != 0:
            idf = 1 + math.log(number_of_files / totaloccur)
        else:
            idf = 0
        IDF[y]=idf
        TFd[y]=firststep
    #print(IDF)
def TIDFq():
    for i in TFd:
        idfq[i]=IDF[i]*TFq[i]
    #print(idfq)
def TFIDd():
    for i in IDF:
        x = {}
        for j in TFd[i]:
            x[j]=TFd[i][j]*IDF[i]
        idfd[i] = x
    #print(idfd)
def finalprep():
    for i in idfq:#mining
        for j in idfd[i]:#doc_name mining
            if j not in docwise:
                docwise[j]={i:idfd[i][j]}
            else:
                docwise[j].update({i:idfd[i][j]})
    #print(docwise)
def finale():
    #print(idfq)
    #print(docwise)
    for i in docwise:
        x1 = 0
        x2 = 0
        x3 = 0
        for j in idfq:
            x1+=docwise[i][j]*idfq[j]
            x2+=docwise[i][j]*docwise[i][j]
            x3+=idfq[j]*idfq[j]
        results[i]=x1/(math.sqrt(x2)*math.sqrt(x3))

def prepnex():
    global inlink
    inlink={}
    q=results.__len__()
    temp=[]
    for i in results.keys():
        temp.append(i)
    for i in range(0,q):
        y=[]
        for j in range(0,q):
            x=0
            if i != j:
                print("link of",temp[i],"with",temp[j],"1 or 0")
                x=input()
            y.append(x)
        inlink[temp[i]]=y
   #print(inlink)
   #cntrlty.append(x)
   # print(cntrlty)


#start of code
use_entry="web mining"
each_query(use_entry.lower())#doc calculation make corrction
tfquery(use_entry)#make TF of query
#print(TFd)
#print(TFq)
#print(IDF)
TIDFq()#query * iDF
TFIDd()#doc* IDF
#print(idfd)
#print(idfq)
finalprep()
finale()
print(results)
#TF wala kam
#In link outlink
prepnex()
print(inlink)