# -*- coding:utf-8 -*-
import copy
from collections import deque
class Trie:
    def __init__(self):
        self.num = 1
        self.root = {'vertex':self.num} # 定义根节点，把结点号1赋给根节点

    def insert(self, word):
        curNode = self.root # 当前结点初始化为根节点
        for c in word: # 依次取出读入序列中的每一个字符
            if not c in curNode: # 如果当前结点下面没有这个字符
                self.num += 1 # 结点号加1
                curNode[c] = {'vertex': self.num} # 给当前结点下面增加一个字典，并记录结点号
            curNode = curNode[c] # 把新增的结点设为当前结点

class Trie_bfs:
    def __init__(self):
        self.num = 1
        self.root = {'vertex':self.num} # 定义根节点，把结点号1赋给根节点

    def insert(self, words):
        curNode = {"root":self.root} # 当前结点初始化为根节点
        lenlist = [len(w) for w in words]
        minl = min(lenlist)
        maxl = max(lenlist)
        curNode_new = {}
        for i in range(maxl):
            for w in words:
                if i<len(w):
                    c = w[i]
                    if i!=0:
                        c_last = w[i-1]
                        for cn in curNode:
                            if c_last == cn:
                                parent_node = curNode[cn]
                    else:
                        parent_node = self.root

                    if not c in parent_node:
                        self.num += 1
                        parent_node[c] = {'vertex': self.num}
                    curNode_new[c] = parent_node[c]
            curNode = curNode_new


def dfs_trie(trdict, result=[]):

    rootnum = trdict["vertex"]
    for key in trdict:
        if key!="vertex":
            result.append("%s %s %s" % (str(rootnum), str(trdict[key]["vertex"]), key))
            #print("%s %s %s" % (str(rootnum), str(trdict[key]["vertex"]), key))

            dfs_trie(trdict[key], result=result)
    return result

def bfs_trie(root):
    result = []
    queue = deque([root])

    while queue:
        nodedict = queue.popleft()
        rootnum = nodedict["vertex"]
        for key in nodedict:
            if key!="vertex":
                result.append("%s %s %s" % (str(rootnum), str(nodedict[key]["vertex"]), key))
                #print("%s %s %s" % (str(rootnum), str(nodedict[key]["vertex"]), key))
                queue.extend([nodedict[key]])
    return result


def main():
    trie = Trie()
    with open("input.txt") as f:
        for eachline in f:
            line = eachline.strip()
            trie.insert(line)

    result = dfs_trie(trie.root)
    for eachline in result:
        print(eachline)

def main_bfs():
    trie = Trie_bfs()
    content = []
    with open("input.txt") as f:
        for eachline in f:
            line = eachline.strip()
            content.append(line)
    trie.insert(content)

    result = bfs_trie(trie.root)
    for eachline in result:
        print(eachline)


if __name__ == "__main__":
    main()