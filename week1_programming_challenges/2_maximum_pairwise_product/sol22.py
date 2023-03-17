def max_product():
    n = int(input())
    values = list(map(int,input().split()))
    max1,max2,index = 0,0,0
    for i in range(n):
        if values[i]>max1:
            max1 = values[i]
            index = i
    values.pop(index)

    for i in range(n-1):
        if values[i]>max2:
            max2 = values[i]      
    return max1*max2


if __name__ == '__main__':
    print(max_product())

