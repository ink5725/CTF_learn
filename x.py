"""
17.学科竞赛
现有六门功课 (语文、数学、物理、化学、政治、历史) 的成绩， 现在需要从中选拔优秀同学参加如下学科竞赛： 生物竞赛 (B) 选拔化学和数学总分最高的同学， 信息学竞赛 (I) 选拔物理和数学总分最高的同学，
 党史竞赛 (H) 选拔政治和历史总分最高的同学， 现在给出N名同学的各科成绩， 请编写程序帮忙选出适合参加相应竞赛的同学。
输入说明：
第一行包括一个整数N和一个字符C， N表示参与选拔的同学人数， C表示选择的竞赛类型。
输出说明：
适合指定竞赛类型的学生学号。如果有多个符合条件的学生， 按学号从小到大分行输出学号， 每行一个。
输入样例：

8 I
2021001 90 90 85 90 80 80
2021002 95 96 82 90 85 83
2021003 90 95 85 90 80 82
2021004 90 89 90 90 70 80
2022001 90 95 80 90 82 70
2022004 90 90 80 90 77 80
2022002 90 89 80 90 80 83
2022003 90 90 80 90 79 80
输出样例：
2101003
"""


"""
input_data=list(input().split())
m,c=int(input_data[0]),input_data[1]
stu=[]
lists=[]
for i in range(m):
    temp=input()
    lists.append((temp.split()[0],temp.split()[1],temp.split()[2],temp.split()[3],temp.split()[4],temp.split()[5],temp.split()[6]))
pl=[]
for i in lists:
    if c=='B':
        pl.append((int(i[0]),int(i[4])+int(i[2])))
    if c=='I':
        pl.append((int(i[0]),int(i[2])+int(i[3])))
    if c=='H':
        pl.append((int(i[0]),int(i[5])+int(i[6])))
pl.sort(key=lambda x: x[1],reverse=True)
print(pl[0][0],end='')
"""
"""
19.产品质量抽查
自动化流水线生产， 产品质量通过对每批N件产品中的连续M件进行抽查完成， 其中每个产品评测K个指标， 每个指标的检测结果为“优秀” (用1表示) 或“合格” (用0表示) ，例如一个产品有6个指标，
检测结果为” 110011”， 表示该产品4项指标检测优秀， 2项指标检测合格。现在给出一批N件产品的检测结果，
求任意被抽查的连续M件产品 (如1~M、2 ~(M+1)、3~(M+2),(N-M+1)~N)，
使得优秀指标总项数最多， 并输出该最多项数的值。
输入说明：
第一行是三个正整数， 分别为N， M和K；
之后N行是每个产品的检测结果， 为长度K的01字符串。
输出说明：
优秀指标总项数的最大值。
输入样例：
10 2 6
101111
111111
111111
101010
111011
111110
111111
111110
111011
111111
输出样例：
12
"""
"""
def sta(z):
    sum=0
    for i in z:
        if i=='1':
            sum+=1
    return sum
n,m,k=map(int,input().split())
ll=[]
for i in range(n):
    z=input()
    ll.append((z,sta(z)))
max=ll[0][1]+ll[1][1]
for i in range(len(ll)-1):
    if(ll[i][1]+ll[i+1][1]>max):
        max=ll[i][1]+ll[i+1][1]
print(max)

"""
"""
18.集合位置
多个机器人分布在M*N(1<=M,N <= 1000))的方格中， 每个机器人分布在不同的方格里。规定每个机器人只能向上下左右的相邻方格移动， 每移动一个方格需要消耗1个单位能量。
现在要求所有机器人集合， 集合点只能是某个机器人初始所在方格。
现在请找一个集合点， 使得所有机器人到达该点消耗的总能量最低。
输入说明：
第一行是一个整数K(0<K≤100),表示机器人的总数。
之后K行是每个机器人所在方格的位置， 用x， y表示， 以空格隔开。
输出说明：
输出最低的总能量消耗。
输入样例：
4
4 5
3 3
2 2
4 4
输出样例： 7
"""
"""
k=int(input())
pos=[]
d=[]
for i in range(k):
    z=input()
    pos.append((int(z.split()[0]),int(z.split()[1])))
for i in pos:
    e=0
    for j in pos:
        if(i!=j):
            e+=abs(i[0]-j[0])+abs(i[1]-j[1])
    d.append(e)
min=d[0]
for i in range(len(d)):
    if d[i]<min:
        min=d[i]
print(min)
"""
"""
a=[190,38,75,20,47,85,34,56,90,42,44,54,23,78,68,58,91,36,38,77,56,79,82,45,56,67,65,34,87,30]
b=[9.8,8.8,5.5,31.5,18,34 25,11,6.5,5.5,4,4,3.5,2.5,10,5,2.9 ,4.8,3.6,4,5,3,2.6,4.7 8.9,3.7 2.6,5.7,5,4.7]
"""
"""
题目描述
小明在玩进阶版大富翁， 进阶版大富翁有特殊的步数计算方法。小明每次可以走的步数由一个公式决定。公式每个部分可以是一个整数或者一次数字抽奖 nds 。nds 表示， 在1到 s 中的整数中， 可以抽取 n 次，
结果是你 n 次结果的和。总步数就是整个式子的结果。
如1+2d3,代表的就是1+2次在1到3之间抽取数字的结果。
结果最小值为三， 最大值为七。
现在题目中会给你一个字符串 s 表示步数的计算公式， 请你编写代码， 帮小明计算一下， 他可以走的步数的期望值是多少? (结果如果不是整数， 那么保留一位小数)。
输入输出格式
输入格式
一个字符串 s。
输出格式
一个整数。
输入输出样例1
输入
1+2d3
输出
"""
"""
x=0
y=0
z=0
s=list(input().split('+'))
for i in range(len(s)):
    try:
        x+=int(s[i])

    except ValueError:
        y+=int(s[i][0])*int(s[i][2])
        z+=int(s[i][0])
sum=x+(y+z)//2
print(sum)
"""
"""
给定两个字符串 text1 和text2,返回这两个字符串的最长公共子序列的长度。如果不存在公共子序列， 返回0。一个字符串的子序列是指这样一个新的字符串： 它是由原字符串在不改变字符的相对顺序的情况下删除某些字符 
(也可以不删除任何字符) 后组成的新字符串。
例如, ace 是 abcde 的子序列, 但 aec 不是 abcde 
的子序列。
两个字符串的公共子序列是这两个字符串所共同拥有的子序列。
输入格式
字符串。
输出格式
字符串。
输入/输出样例
输入1
lijiji. jjj
输出1
4
说明/提示
· text1 和 text2 仅由小写英文字符组成。
"""
"""
from itertools import combinations
def getn(s):
    m=[]
    for i in range(len(s)+1):
        coms=list(combinations(s,i))
        for com in coms:
            m.append(''.join(com))
    return m
input_data=input().split(',')
s1=input_data[0]
s2=input_data[1]
str1=getn(s1)
str2=getn(s2)
num=[]
for st in str1:
    if st in str2:
        num.append(len(st))
if num:
    numx=sorted(num)
    print(numx[-1])
else:
    print(0)
"""
"""
题目描述
左截断素数是不包含0 位的素数， 当连续删除第一个数字时， 结果始终为素数。
可右截断的素数是不包含 0位的素数， 当连续删除最后一位时， 结果始终为素数。
创建一个将整数作为参数的函数， 并且：
如果整数只是一个可左截断的素数， 则返回“left”。
如果整数只是一个可右截断的素数， 则返回“right”。
如果整数是两者， 则返回“both”。
否则, 返回 False。
输入输出格式
输入格式
输入一个整数；
输出格式
输出一个字符串， 表示输入整数的素数类型。
输入输出样例1
输入
9137
输出
left
解释 (可选)
因为 9137 137 37 7 都是质数。
输入输出样例2
输入
5939
输出
right
解释 (可选)
因为5939 593 59和5都是素数。
说明提示
输入整数不会超过10⁶,
"""

"""
def is_prime(n):

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def left_truncatable_prime(n):
    
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):  # 从第i位开始截断
            return False
    return True


def right_truncatable_prime(n):

    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:len(str_n) - i])):  # 从第i位结束截断
            return False
    return True


def truncatable_prime_type(n):
   
    is_left = left_truncatable_prime(n)
    is_right = right_truncatable_prime(n)

    if is_left and is_right:
        return "both"
    elif is_left:
        return "left"
    elif is_right:
        return "right"
    else:
        return False


# 输入处理
num = int(input("请输入一个整数: "))
result = truncatable_prime_type(num)
print(result)
"""

"""
最近， 小明去了一个古老的国家。在之前很长的时间里， 它都是世界上最富有、最强大的王国。因此， 这个国家的人民仍然非常自豪， 即使当他们的国家不再那么富有。
这个国家的商人每个人只卖一件商品， 
每件商品具有一定价值， 但如果你的钱低于一定金额， 他们会拒绝与你进行交易。
如果小明有一定单位的钱， 小明能得到的最大商品价值是多少?
输入输出格式
输入格式
第一行包含两个整数 N，M， 分别表示商品的数量和初始总金额。
接下来输入 N 行， 每行包含三个数字 P，Q，V， 分别表示每件商品的价格， 交易底线金额和商品的价值。
数字之间以空格间隔。
输出格式
针对输入， 打印出能得到的最大商品价值。
输入输出样例1
输入
2 10
10 15 10
5 10 5
输出
5
"""
# 读取输入数据
input_data = list(map(int, input().split()))
n = input_data[0]  # 物品数量
m = input_data[1]  # 背包容量

# 初始化 p 和 f 数组
p = [[0] * 4 for _ in range(n + 1)]  # 假设每个项目有4个属性
f = [[0] * (m + 1) for _ in range(n + 1)]  # 动态规划数组

# 读取每个项目的数据
for i in range(1, n + 1):
    p[i] = list(map(int, input().split()))  # 输入项目的属性

# 填充动态规划数组
for i in range(1, n + 1):
    for j in range(0, m + 1):  # j 从 0 到 m
        if j < p[i][0]:  # 如果当前容量小于物品重量
            f[i][j] = f[i - 1][j]  # 不能放当前物品
        elif j>p[i][0]:
            # 选择放或不放当前物品
            f[i][j] = max(f[i - 1][j], f[i - 1][j - p[i][0]] + p[i][2])
        else:
            f[i][j]=f[i-1][j]
# 输出结果
print(f[n][m])



