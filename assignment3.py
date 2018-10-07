"""
统计字符串中的字符个数
定义函数countchar()按字母表顺序统计字符串中所有出现的字母的个数（允许输入大写字符，并且计数时不区分大小写）
输入字符串
输出列表
"""

def countchar(string):
    b=[0]*26
    string.lower()
    string.strip()
    for c in string:
        if ord(c)<=ord('z') and ord(c)>=ord('a'):
            b[ord(c)-ord('a')]+=1
        elif ord(c)<=ord('Z') and ord(c)>=ord('A'):
            b[ord(c)-ord('A')]+=1
    return b






if __name__=='__main__':
    string=input()
    print(countchar(string))