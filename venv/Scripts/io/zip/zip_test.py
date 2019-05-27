import os, zipfile
path = 'G:\\GitAndSvn\\servers\\v4-server\\server\\target\\server-2.0.war'
war1 = open(path, 'r')
war = zipfile.ZipFile(path, 'r')
tar = war.read('WEB-INF/classes/config.properties')
str = tar.decode()
# print (str)
print(str.startswith('#resource'))