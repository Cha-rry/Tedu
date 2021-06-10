f = open("fileru","wb",5) 设置缓冲区大小


while True:
    data = input(">>")
    if not data:
        break
    f.write(data)
f.close()
