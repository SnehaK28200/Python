# python function


def fectorial(n):
    if n < 1:
        return 1
    else:
        return (n * fectorial(n-1))


num = int(input("enter the number "))
print("the fectorial of", num, "is", fectorial(num))
