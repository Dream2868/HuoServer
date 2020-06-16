#用户导入自己写的py文件
#import
#import
#import
#

#方便选择设置的switch类
#引自 http://code.activestate.com/recipes/410692/
class switch(object):

    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

#中转站函数，目前只适用于GET类型请求，不支持POST带请求体的类型请求
def transfer(path,parameters):

    #创建参数字典
    dic = {}

    #如果参数不为空则按照格式分割写入字典
    if parameters != "":
        paras = parameters.split('&')
        for i in range(0,len(paras)):
            tempItem = paras.split('=')
            dic[tempItem[0]] = tempItem[1]

    for case in switch(path):
        #中转站示例代码，根据路径选择操作函数，传入参数字典
        #if case('/pathA/pathB'):
        #    return testFunc(dic)

        #未查找到对应的路径
        if case():
            return 0
    return 0
