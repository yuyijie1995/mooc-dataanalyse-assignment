# """
# 寻找第n个默尼森数
# P是素数且M也是素数，并且满足等式M=2^P-1,则称M为默尼森数。例如P=5，M=2^P-1=31,5和31都是素数，因此31是默尼森数
# """
# from math import sqrt
# def prime(num):
#     #求素数
#     if num==1:
#         return 1
#
#     for i in range(2,int(sqrt(num))+1):
#         if num%i == 0:
#             return 0
#     # 跟循环对齐，没有进入循环的时候素数为真,因为range（2，2）不进入循环
#     return 1#
#
# def monisen(n):
#     #输入n，默尼森数的index
#     monisen_count=0
#     prime_num=1
#     while monisen_count!=n:
#         prime_num+=1
#         is_prime_num=prime(prime_num)
#         if is_prime_num==1:
#             monisen_num=pow(2,prime_num)-1
#             monisen_count+=1
#             if monisen_count==n:
#                 return monisen_num


def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        #break
    else:
        return True


def monisen(no):
    TempInt = 0
    P = 1
    while TempInt < no:
        P += 1
        M = 2 ** P - 1
        if prime(P) == True and prime(M) == True:
            TempInt += 1
    return M


print(monisen(int(input())))




if __name__=='__main__':
    print(monisen(int(input())))