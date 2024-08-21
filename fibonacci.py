def fibonacci(n):
    if n==0:
        return 1
    if n==1:
        return 1
    
    num_1= 1
    num_2 = 1
    
    for i in range(2, n + 1):
        num = num_1 + num_2
        num_1 = num_2
        num_2 = num
    
    return num_2

def main():
    print(fibonacci(1000))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    return


if __name__ == "__main__":
    main()