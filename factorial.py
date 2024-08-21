def iterative(n):
    resultado = 1
    
    for i in range(1, n+1):
        resultado *= i
    return resultado


def recursive(n):
    if n == 0:
        return 1
    else:
        return n * recursive(n - 1)

def main():
    n = 4
    print(recursive(n), iterative(n))
    return

if __name__ == "__main__":
    main()




    