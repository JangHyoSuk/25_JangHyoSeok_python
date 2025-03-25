def get_fixed_price(price, discount) :
    result = int(price/(1-discount/100))
    return result

d = int(input('할인율은? '))
a = int(input('A 상품의 할인된 가격은? '))
b = int(input('B 상품의 할인된 가격은? '))
A = get_fixed_price(a, d)
B = get_fixed_price(b, d)
print('A 상품의 정가는', A, '원')
print('B 상품의 정가는', B, '원')
