"""
如果一个n位数刚好包含了1至n中所有数字各一次则称它们是全数字（pandigital）的，
例如四位数1324就是1至4全数字的。从键盘上输入一组整数，输出其中的全数字，若找不到则输出“not found”。
输入样例：
1243,322,321,1212,2354
输出样例：
1243
321
"""
def pandigital(nums):
    num_list = []
    for num in nums:
        num=str(num)
        num_len=len(num)
        count=0

        for i in range(1,num_len+1):
            for j in num:
                if int(j)==i:
                    count+=1
                    break
        if count==num_len:
            num_list.append(num)
    return num_list








if __name__=='__main__':
    lst=pandigital(eval(input()))
    if lst==None:
        print('not found')
    else:
        for i in lst:
            print(i)