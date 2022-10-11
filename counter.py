# python
f = open("datas.txt", "r")
data = f.read()
f.close()
data = data.split("\n")
num = 0
for data in data:
    print(num)
    num += 1
print(num)
