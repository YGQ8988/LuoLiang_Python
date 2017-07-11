x = (int(input("请输入开始值（整数）：")),int(input("请输入一个结束值：")))

x1 = min(x)
x2 = max(x)
for n in range(x1,x2):
    for i in range(2,n-1):
        if n % i == 0:
            break
    else:
        print(n,"是素数")
