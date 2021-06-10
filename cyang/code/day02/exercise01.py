# 练习一
L = int(input("请输入："))
J = str(L // 16)
l = str(L % 16)
print("一共" + J + "斤" + l + "两")
# 练习二 加速度=2（距离-初速度*时间）/时间^2

length = float(input("请输入距离："))
initial_velocity = float(input("请输入初速度："))
time = float(input("请输入时间："))
accelerated_velocity = 2 * (length - initial_velocity * time) / time ** 2
print("加速度" + str(accelerated_velocity))

# 练习三
second = int(input("请输入时间："))
hour = second // 3600
minute = second // 60 % 60
miao = second % 60
print("时间为：" + str(hour) + "小时零" + str(minute) + "分钟零" + str(miao) + "秒")

# 练习4
A = int(input("输入一个四位整数："))
gw = A % 10
sw = A // 10 % 10
bw = A // 100 % 10
qw = A // 1000
H = gw + sw + bw + qw
print("和为：" + str(H))
