# HuoServer
## 1.0版本
## 支持GET请求
#### 请求文件仿照主流的Apache的功能实现，可以作为服务器本地文件的索引功能以供搭建如个人博客、官方网站、资源平台等形式的网站
#### JSON类型后端数据交互仿照主流的springboot的部分功能进行实现
####
####
####
### 使用文档：
#### 服务器配置修改：
##### 在Counstant.py修改PORT可以修改默认的Web服务端口，默认的服务端口为80;
##### 在Counstant.py修改DEFAULT_INDEX可以修改默认的主页html的路径，默认的的主页路径为/www/index.html;
##### 在welcome.txt中可以修改其中内容供服务启动时显示在控制台上;
####
#### 文件访问设置：
##### 将所需被访问的文件放在以框架中HuoServer.py的目录为根目录的可选路径中，在请求URL中加入对应的Path即可进行GET文件访问;
####
#### JSON后端撰写：
##### 1.首先创建一个模板函数，参数为一个字典值，用于接收从URL中解析的参数，返回值也为一个字典值或者0，字典值需仿照javascript中的JSON格式进行创建，必须带有code状态码这个值，如果不提供该路径的服务则返回0;
##### 2.在框架中的JsonServerFuncEdit.py文件中引入自己所创建的模板函数，并在transfer中转站函数中的switch方法下建立一个case(),将自己创建的模板函数与对应路径关联起来，即可完成单个JSON类型请求的创建。
####
#### *具体使用方法参照demo目录的下的测试文件使用。
