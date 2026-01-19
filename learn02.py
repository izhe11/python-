#文件读写操作

with open('test_read.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
