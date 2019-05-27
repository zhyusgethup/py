import os

cmd = 'cd G:'
result = os.popen(cmd).readlines()
list = []
for line in result:
    list.append(line)
print(list)
