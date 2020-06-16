import demo

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

def transfer(path,parameters):

    dic = {}

    if parameters != "":
        paras = parameters.split('&')
        for i in range(0,len(paras)):
            tempItem = paras.split('=')
            dic[tempItem[0]] = tempItem[1]

    for case in switch(path):
        if case('/testA/testB'):
            return demo.testFunc(dic)

        if case():
            return 0
    return 0
