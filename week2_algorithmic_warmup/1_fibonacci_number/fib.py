def fibonacci(n):
    if n<=0:
        return 0
    else: 
        a,b=0,1
        for i in range(2,n+1):
            a,b = b, a+b 
        return b

if __name__ == '__main__':
    print(fibonacci(int(input())))
