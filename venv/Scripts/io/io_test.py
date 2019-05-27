f1 = open('/vmware-0.log', 'r')  ## 在windows中盘符根目录
f2 = open('test.txt', 'w')  ## 这个是相对路径,相对文件
f3 = open('./test.txt')  ## 同上
f4 = open('F://vmware-0.log')  ## ok
f2.write('你好')
f2.close()
f2 = open('test.txt', 'r')
str2 = f2.read()
print(str2)
