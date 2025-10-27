Flask 留言板 (Message Board) API 项目

这是一个使用 Flask 构建的、功能完整的 Web 应用和 RESTful API。

本项目从一个简单的 "Hello World" 网站开始，逐步构建了一个包含模板、样式、表单交互、数据库连接以及全功能 CRUD API 的留言板。

技术栈 (Technology Stack)

Python 3

Flask: 核心 Web 框架

Flask-SQLAlchemy: 用于数据库交互 (ORM)

SQLite: 本地数据库文件

Postman: 用于 API 测试

包含的功能

[x] 面向用户的网站 (Web)

[x] 使用 Jinja2 模板继承 (base.html)

[x] 动态数据传递 (主页的技能列表)

[x] 静态 CSS 文件加载 (style.css)

[x] 共享导航栏

[x] 面向程序的 API (API)

[x] 完整的 CRUD 功能 (创建, 读取, 更新, 删除)

[x] GET / POST / PUT / DELETE 方法

[x] JSON 数据的请求和响应

[x] 数据库 (Database)

[x] 使用 SQLAlchemy (ORM) 定义数据模型 (Message)

[x] 数据库持久化存储 (database.db)

API 接口文档 (API Endpoints)

你需要用 Postman 测试以下所有接口，并把你自己的截图放在这里。

方法 (Method)

路由 (Route)

功能描述

请求体 (Body) (JSON)

成功响应 (Success Response) (JSON)

API 接口文档 (API Endpoints)

方法 (Method)

路由 (Route)

功能描述

请求体 (Body) (JSON)

成功响应 (Success Response) (截图)

GET

/api/messages

获取所有消息的列表。

(无)

<img src="https://github.com/user-attachments/assets/cc9f0e04-651c-4363-8d23-964c625d2799" width="500" />

POST

/api/messages/create

创建一条新消息。







如何本地运行 (How to Run Locally)

Clone 仓库 (或下载文件)

git clone ...
cd ...


创建并激活虚拟环境
python3 venv venv

# [你自己填写创建 venv 的命令]
# [你自己填写激活 venv 的命令]


安装依赖包

# [你自己填写安装 Flask 和 Flask-SQLAlchemy 的命令]


创建数据库文件

这是一个一次性步骤。

# [你自己填写进入 Python 交互式 shell 的命令]

# [你自己填写 Python shell 里的命令 (导入 app, db)]
# [你自己填写 Python shell 里的命令 (with app.app_context()...)]
# [你自己填写 Python shell 里的命令 (db.create_all())]
# [你自己填写 Python shell 里的命令 (退出)]


运行 Flask 应用

(vnev)..$ python3 hello.py


访问应用

Web 界面: 访问 http://127.0.0.1:5000

API 接口: 访问 http://127.0.0.1:5000/api/messages
