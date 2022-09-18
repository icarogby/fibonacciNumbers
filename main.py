import fibonacci as fib

def main():
    c = int(input("Case: "))

    match c:
        case 1:
            n = int(input("n: "))
            print(fib.iterativeFibonacci(n))

        case 2:
            n = int(input("n: "))
            print(fib.recursiveFibonacci(n))

        case 3:
            n = int(input("n: "))
            print(fib.optimizedFibonacci(n))

        case 4:
            seq = fib.infinityFibonacci()

            while True:
                b = int(input("next?"))
                
                if (b == 1):
                    print(next(seq))
                else:
                    break

if __name__ == "__main__":
    main()