"""
统计句子中的词频
对于一个已分词的句子（可方便地扩展到统计文件中的词频）：

我/是/一个/测试/句子/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，
/大家/赶快/来/统计/我/吧/，/重要/事情/说/三遍/！

可以用collections模块中的Counter()函数方便地统计词频，例如可用如下代码

"""


def countfeq(s,word):
    word.lower()
    slist=s.split(' ')
    #slist=list(s)
    #slist=[slist.remove(item) for item in slist if item in  (',','.',' " ',' " ','!')]
    count=0
    for i in slist:
        if word == i:
            count+=1


    return count


if __name__ == "__main__":
    s = "Not clumsy person in this world, only lazy people, only people can not hold out until the last."
    word=input()
    s_dict = countfeq(s.lower(),word)
    print(s_dict)