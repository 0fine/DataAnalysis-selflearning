# "r"：表示读取文件，只读
# print()  ————自带换行作用
'''文件读取  方法一'''
"""
f = open("此处放入文件地址")

print(f.read())  # 会读全部的文件内容，并打印  ————此时会记录文件的读取位置
print(f.read())  # 会空字符串，并打印  ————从上次文件记录的位置，开始后续内容的读取

readline()  # 每次读一行的内行
readlines()  # 读取全部全部内容，并把每行作为列表元素返回

f.close()  # 关闭文件，释放资源
"""


'''文件读取  方法二'''
"""
with open("文件地址") as f:
    print(f.read())    # 对文件的操作
该方法执行完所有文件操作后，文件会自动关闭
"""


f = open("F:\AAAAAAAAAAAAAAAAAAAAA\slef-learning\DataAnalysis\data.txt", 'r', encoding="utf-8")
content = f.read()
print(content)
f.close()
