Year = int(input("请输入一个年份："))
result = Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0
print(result)