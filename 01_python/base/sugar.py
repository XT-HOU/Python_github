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