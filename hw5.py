# 사용자 정의 함수
def read_number(n):
    # 일의 자리수 얻기
    d1 = n % 10

    # n에서 일의 자리 숫자 버리기
    n //= 10

    # n에서 십의 자리수 얻기
    d10 = n % 10

    # n에서 십의 자리 숫자 버리고 백의 자리수 남기기
    n //= 10

    read_single_digit(n)
    read_single_digit(d10)
    read_single_digit(d1)


def read_single_digit(n):
    if n == 0: print('영', end='')
    elif n == 1: print('일', end='')
    elif n == 2: print('이', end='')
    elif n == 3: print('삼', end='')
    elif n == 4: print('사', end='')
    elif n == 5: print('오', end='')
    elif n == 6: print('육', end='')
    elif n == 7: print('칠', end='')
    elif n == 8: print('팔', end='')
    elif n == 9: print('구', end='')

# 주 프로그램부
num = int(input('세 자리 점수 입력: '))
read_number(num)
