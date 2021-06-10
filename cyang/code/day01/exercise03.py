#1
r = input("请输入圆形半径：")
mj = 3.14*float(r)**2
print("圆形面积是：" + str(mj))
#2
minute = float(input("请输入分钟："))
hour = float(input("请输入小时："))
day = float(input("请输入天数："))
result = minute * 60 + hour * 60 * 60 + day * 60 * 60 *24
print("秒数是：" + str(result))

