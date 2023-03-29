def fib_modulo(n,m):
    a,b= 0,1

    if n<=0:
            return 0
    else: 
        a,b=0,1
        for i in range(2,n+1):
            a,b = b, (a+b)%m 
        return b

if __name__ == '__main__':
    n,m = map(int,input().split())
    print(fib_modulo(n,m))