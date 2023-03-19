def fibonacci(n):
    values = [1,1]
    for i in range(2,n):
        values.append(values[i-1] + values[i-2])
        
    digit = values[n-1] % 10 
    return digit

if __name__ == '__main__':
    print(fibonacci(int(input())))
