import os
class g:
    @staticmethod
    def ff(cmd):
        result = os.popen(cmd).readlines()
        list = []
        for line in result:
            list.append(line)
            # print(isinstance(line, str))
        return list

cmd1 = 'cd G:'
cmd2 = 'G:\\GitAndSvn\\servers\\v4-server\\server\\'
result1 = g.ff(cmd1)
if(result1[0] == u'G:\\\n'):
    print('ok')
