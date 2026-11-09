result = []

def divider(a, b):
    if a < b:
        raise ValueError("Помилка значення")
    if b > 100:
        raise IndexError("Помилка індексу")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4, 200: 150}

for key in data:
    try:
        result.append(divider(key, data[key]))
    except Exception as e:
        print(type(e).__name__, e)

print(result)
