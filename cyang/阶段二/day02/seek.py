f= open("file","w+")

f.write("world")
print("文件偏移量",f.tell())

f.seek(0,2)

data = f.read()
print(data)

f.close()