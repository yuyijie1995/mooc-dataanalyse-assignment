"""
寻找n以内亲密数对,fac(x)计算包括1但不包括本身的所有因子和并返回,一个数的因子是可以整除这个数的数，但不包括本身
"""
def fac(n):
    sum = 0
    for i in range(1,int(n / 2 + 1)):
        if n % i == 0:
            sum += i
    return sum




if __name__=='__main__':
    n=int(input())
    for i in range(1,n):
        if i==fac(fac(i)) and i < fac(i):
            print('{0}-{1}'.format(i,fac(i)))





