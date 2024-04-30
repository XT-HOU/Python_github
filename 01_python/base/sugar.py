# 处理多个条件语句
size = "lg"
color = "blue"
price = 50
conditions = [
    size == "lg",
    color == "blue",
    price < 100,
]
if all(conditions):
    print("Yes, I want to but the product.")

if any(conditions):
    print("Yes, I want to but the product.")

# 元组拆包，站位符“-”
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for country, _ in traveler_ids:
    print(country)
# 元组拆包，用*处理 剩下的元素
a, b, *rest = range(5)
print(a, b, rest)
# 符号 +=，*=
l = [1, 2, 3]
print(id(l))
l *= 2
print(id(l))
l += [9]
print(id(l))
