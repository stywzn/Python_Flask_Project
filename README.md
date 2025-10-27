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

方法 (Method)

路由 (Route)


GET

/api/messages

<img src="https://github.com/user-attachments/assets/cc9f0e04-651c-4363-8d23-964c625d2799" width="500" />

{

  "messages": [

    {

      "content": "stywzn",

      "id": 3

    },

    {

      "content": "This is the NEW, UPDATED content.",

      "id": 2

    },

    {

      "content": "hello",

      "id": 1

    }

  ]

}





POST

/api/messages/

<img src="https://github.com/user-attachments/assets/6c1e14ef-64d8-4831-ba8b-c7b4b817a3b0" width="500" />

{

    "messages": [

        {

            "content": "stywzn",

            "id": 4

        },

        {

            "content": "stywzn",

            "id": 3

        },

        {

            "content": "This is the NEW, UPDATED content.",

            "id": 2

        },

        {

            "content": "hello",

            "id": 1

        }

    ]

}



PUT

/api/messages/update/4

<img src="https://github.com/user-attachments/assets/55562eea-aa0e-49a5-8585-dea5c5f269a7" width="500" />



{"content": "Updated"}

{

    "message": "Message 4 has been updated.",

    "success": true,

    "updated_message": {

        "content": "whoami",

        "id": 4

    }

}



DELETE

/api/messages/delete/4



<img src="https://github.com/user-attachments/assets/9af17b2e-228f-42c1-adc0-5cc3305f9668" width="500" />


如何本地运行 (How to Run Locally)


Clone 仓库 (或下载文件)

git clone ...
cd ...


创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate


安装依赖包

(venv)...$ pip install Flask FlaskSQLAlchemy


创建数据库文件

python3
>>> from hello import app,db
>>> with app.app_context():
...  db.create_all()
...
... exit()

运行 Flask 应用

(vnev)..$ python3 hello.py


访问应用

Web 界面: 访问 http://127.0.0.1:5000

API 接口: 访问 http://127.0.0.1:5000/api/messages
