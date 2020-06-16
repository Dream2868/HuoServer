#导入必要的基础库
from http.server import BaseHTTPRequestHandler,HTTPServer
import os
import subprocess

#导入常量包
import Constant

#导入返回JSON类型的函数中转包
import JsonServerFuncEdit

# 自定义内部异常类
class HuoServerException(Exception):
    """HuoServer服务器内部错误"""
    pass

#HuoServer请求处理的模板类
class HuoServerCaseBase(object):
    def handle_file(self,handler):
        try:
            with open(handler.full_path,'rb') as reader:
                # 打开对应路径的文件
                content=reader.read()
            handler.send_content(content)
            # 将内容送入返回数据体
        except IOError as msg:
            # 打开文件读入失败的异常
            msg = "'{0}' cannot be read: {1}".format(handler.full_path, msg)
            handler.handle_error(msg)

    def judgeFlag(self, handler):
        # 判断方法
        assert False,Constant.ERROR_TIP

    def performFunc(self, handler):
        # 执行方法
        assert False,Constant.ERROR_TIP

# 不存在该路径，检测是否为JSON类型的请求
class notExitPath(HuoServerCaseBase):

    #是否为JSON类型请求标志量
    isJsonGet = False

    #返回数据体的内容
    jsonData = 0
    def judgeFlag(self,handler):
        #当路径不存在是则可能是JSON请求
        if not os.path.exists(handler.full_path):
            #对路径进行分割
            temp = handler.path.split('?')
            if len(temp) == 1:
                self.jsonData = JsonServerFuncEdit.transfer(temp[0],"")
            elif len(temp) == 2:
                self.jsonData = JsonServerFuncEdit.transfer(temp[0],temp[1])
            else:
                return True
            if self.jsonData == 0:
                return True
            else:
                self.isJsonGet = True
                return True
        return False

    # 命令行检验路径的存在性
    def performFunc(self,handler):
        #如果不是JSON请求则抛出异常
        if not self.isJsonGet:
            raise Exception("{0} not found".format(handler.path))
        #否则完成JSON数据的返回
        else:
            #字典转换为字符串写入数据体，并返回相应的状态码
            handler.send_content(str(self.jsonData),self.jsonData.code,"json")


#该路径是一个文件
class isAFile(HuoServerCaseBase):

    #命令行判断是否为文件
    def judgeFlag(self,handler):
        return os.path.isfile(handler.full_path)

    # 读文件并返回
    def performFunc(self,handler):
        self.handle_file(handler)


#该路径不是一个文件
class notAFile(HuoServerCaseBase):

    #最终判断不为文件
    def judgeFlag(self,handler):
        return True

    #抛出未知对象的异常
    def performFunc(self,handler):
        raise Exception("{0} unknown object".format(handler.path))

#访问根url的时候默认的主页html
class defaultIndexFile(HuoServerCaseBase):

    #处理默认页路径
    def judgeFlag(self,handler):
        handler.full_path = handler.full_path + Constant.DEFAULT_INDEX
        return True

    #针对不同情况的处理方式
    def performFunc(self,handler):
        #如果默认文件存在
        if os.path.isfile(handler.full_path):
            return self.handle_file(handler)
        else:
            handler.send_content(Constant.NO_INDEX.encode('utf-8'),404)

#利用cgi协议处理外部文件
class cgiFile(HuoServerCaseBase):

    #cgi协议对外部文件进行判定
    def judgeFlag(self,handler):
        return os.path.isfile(handler.full_path) and handler.full_path.endswith(".py")

    #运行cgi处理函数
    def performFunc(self,handler):
        self.cgiRunner(handler)

    #cgi协议运行
    def cgiRunner(self,handler):
        data = subprocess.check_output(["python",handler.full_path],shell=False)
        handler.send_content(data)

#继承自HTTPRequestHandler基类的HuoServer处理类
class HuoServerRequestHandler(BaseHTTPRequestHandler):
    #请求判别的处理优先级数组
    cases = [notExitPath(),cgiFile(),isAFile(),defaultIndexFile(),notAFile()]

    #GET请求的函数重写
    def do_GET(self):
        try:
            self.full_path = os.getcwd()+self.path
            for case in self.cases:
                if(case.judgeFlag(self)):
                    case.performFunc(self)
                    break
        #处理异常
        except Exception as msg:
            #写入错误处理函数并执行相关操作
            self.handle_error(msg)

    #错误显示页面html
    Error_Page = Constant.ERROR_PAGE

    #错误请求处理
    def handle_error(self,msg):
        content=self.Error_Page.format(path=self.path,msg=msg)
        self.send_content(content.encode('utf-8'),404)

    #返回数据体拼接
    def send_content(self,page,status=200,type="html"):
        self.send_response(status)
        self.send_header("Content-Type","text/"+type)
        self.send_header("Content-Length",str(len(page)))
        self.end_headers()
        self.wfile.write(page)

class HuoServerClient(object):
    #获取默认端口
    port = Constant.PORT

    #创建WEB服务进程
    def createServer(self):
        #服务启动欢迎txt
        try:
            fp = open(os.getcwd() + Constant.WELCOME_PATH,"rb")
            while True:
                line = fp.readline()
                print(line)
                if not line:
                    break
                pass  # do something
        except IOError as msg:
            print("Can not open the welcome.txt!")

        print("HuoServer Running")
        serverAddress=('',self.port)
        server=HTTPServer(serverAddress,HuoServerRequestHandler)
        server.serve_forever()
