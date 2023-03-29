def lcm(x,y):
    product = x*y
    while y!=0:
        x,y = y,x%y
    
    return product//x


if __name__ == '__main__':
    a,b = map(int, input().split())
    print(lcm(a,b))

