def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def main():
    pass


if __name__ == "__main__":
    print(fibo(10))
    main()
