#默认WEB服务端口
PORT = 80
#服务启动时的txt
WELCOME_PATH = "\welcome.txt"
#默认主页路径
DEFAULT_INDEX = "\www\index.html"
#网页提示语
ERROR_TIP = "Not Impletment"
#错误页面html模板
ERROR_PAGE = """
<!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>HuoServer-404-Page</title>
        </head>
    <body>
        <h1>404-PAGE NOT FOUND</h1>
        <p>We are sorry,but the page you requested was not found.</p>
        <a>Reason:Error accessing ({path}),{msg}</a>
        <p>***  Service provided by HuoServer  ***</p>
    </body>
</html>
"""
#默认主页失效html模板
NO_INDEX = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>No Index Page</title>
	</head>
	<body>
		<h3>The index page was not found</h3>
		<p>We are sorry,but the index page was not found.</p>
		<p>Server owner maybe No settings</p>
		<a href="https://github.com/Dream2868/HuoServer">Click to HuoServer's Github address</a>
		<p>***  Service provided by HuoServer  ***</p>
	</body>
</html>
"""
