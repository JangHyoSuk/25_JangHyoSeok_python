def gugudan(a, b):
    for i in range(1, 10):
        for n in range(a, b):
            print(f'{n} x {i} = {n*i}', end='\t')
        print()

gugudan(2, 6)
print()
gugudan(6,10)
