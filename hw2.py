def get_integer(prompt) :
    a = int(input(prompt))
    return a
def exchange(A) :
    n500 = A // 500
    A %= 500

    n100 = A // 100
    A %= 100

    n50 = A // 50
    A %= 50

    n10 = A // 10

    print('500원 동전의 개수:', n500)
    print('100원 동전의 개수:', n100)
    print('50원 동전의 개수:', n50)
    print('10원 동전의 개수:', n10)
A = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(A)

