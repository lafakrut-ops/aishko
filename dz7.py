def create_sum():
    total = [0]

    def add(number):
        total[0] += number
        return total[0]

    return add


summa = create_sum()

print(summa(5))
print(summa(10))
print(summa(3))
