shopping_bag = {}

def buy(shopping_bag):
    item = input("상품명? ")
    if item == "":
        return False
    amount = int(input("수량은? "))
    shopping_bag[item] = shopping_bag.get(item, 0) + amount
    print(f"장바구니에 {item} {amount}개가 담겼습니다.\n")
    return True

def show(shopping_bag):
    print(">>> 장바구니 보기:", shopping_bag)
    print()

def find(shopping_bag):
    item = input("장바구니에서 확인하고자 하는 상품은? ")
    if item in shopping_bag:
        print(f"{item}(은)는 {shopping_bag[item]}개 담겨 있습니다.\n")
    else:
        print(f"장바구니에 {item}(은)는 없습니다.\n")

while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)
