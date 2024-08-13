## [Introduction to Pattern Matching](https://rosalind.info/problems/trie/)

### 背景知识


**Trie树**

又称单词查找树, 是一种用于高效存储和搜索字符串的树结构。它是一种树形结构，是一种哈希树的变种。
典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。
它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。

其形成过程如下。 对于字符串中每一个唯一的第一个符号，都会形成一条连接根与新顶点的边。如果已经存在的公共前缀只有一条路径。

根节点不包含字符，除根节点外每一个节点都只包含一个字符； 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串； 
每个节点的所有子节点包含的字符都不相同。

<a href="https://rosalind.info/media/problems/trie/trie.png" target="_blank"><img src="https://rosalind.info/media/problems/trie/trie.png" /></a>

### 问题

给定：由最多100个长度不超过100bp的DNA字符串组成的列表，其中没有一个字符串是另一个字符串的前缀。

输出：对应的邻接表格式的三元组，首先对节点编号，根结点标记为1，然后把其他结点用从2到n的整数标记。三元组第一个元素为父节点编号，第二个元素为当前节点
编号，第三个元素为边对应的字符。


示例输入: 

    ATAGA
    ATC
    GAT

示例出: 

    1 2 A
    2 3 T
    3 4 A
    4 5 G
    5 6 A
    3 7 C
    1 8 G
    8 9 A
    9 10 T

### 解决

首先要构造Trie树，和网上找到的Trie的实现不同的是，这里我们需要记录节点编号，如何和示例保持一致，就要用深度优先的方式建树和遍历。

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

    trie = Trie()
    with open("input.txt") as f:
        for eachline in f:
            line = eachline.strip()
            trie.insert(line)

之后就是按照深度优先遍历树并输出。

    def dfs_trie(trdict, result=[]):
        rootnum = trdict["vertex"]
        for key in trdict:
            if key!="vertex":
                result.append("%s %s %s" % (str(rootnum), str(trdict[key]["vertex"]), key))
                #print("%s %s %s" % (str(rootnum), str(trdict[key]["vertex"]), key))
    
                dfs_trie(trdict[key], result=result)
        return result

    result = dfs_trie(trie.root)
    for eachline in result:
        print(eachline)

### 扩展

在["Finding a Motif in DNA"](https://rosalind.info/problems/subs/)中介绍了在基因串中寻找motif的问题。 更常见的情况是，
我们希望在一个更大的字符串中找到一组motif，例如在基因组中搜索一组已知基因时。

本问题提出了模式匹配的算法问题，即在一个大字符串（称为文本）中搜索一组较小字符串（称为图案）的实例。 要在文本中找到精确的模式，最明显的方法是对
每个模式采用简单的 "滑动窗口 "算法。 但是，如果我们需要考虑大量的模式（在处理基因数据库时通常会出现这种情况），这种方法就会非常耗时。 如果我们能
以某种方式只遍历一次基因组，而不是为每个模式遍历基因组，那就更好了。 为此，需要一种能有效组织模式集合的数据结构。