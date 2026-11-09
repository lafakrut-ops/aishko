"""my_list = [1, 2, 3]

interator = iter(my_list)

for elem in interator:
    print(elem)

for elem in interator:
    print(elem)"""

"""class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i >= self.max_number:
            raise StopIteration
        return self.i
count = Counter(5)
for elem in count:
    print(elem)

print(count.__next__)
print(count.__iter__)
print(next(count))
print(iter(count))
print(next(count))"""

"""def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number**i
        i += 1
res = raise_to_the_degrees(123, 500)
print(res)
for _ in res:
    print(_)"""
def helper(work):
    work_in_memory = work
    def helper(work):
        return f'i will help you of memories'

    return helper
help = helper("homework")
print(helper('clining'))
print(helper('driving'))


