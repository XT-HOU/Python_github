# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
    flask_siwadoc插件常用方法
    flask方式注册路由
"""

from flask import Flask
from flask_siwadoc import SiwaDoc

app = Flask("__name__")

# region 初始化API文档
# 设置API文档模板， 路径添加 ?ui=swagger，支持 "redoc", "swagger", "rapidoc"
siwa = SiwaDoc(app, ui='swagger')

# or
# siwa = SiwaDoc()
# siwa.init_app(app)
# endregion



# region api分类案例
@app.route("/api/hello", methods=["GET"])
@siwa.doc(tags=["user"])
def user():
    """
        api分类案例,使用tag标签分类
    :return:
    """
    return "api分类案例，tag标签"


@app.route("/api/test", methods=["GET"])
@siwa.doc(tags=["test"])
def hello():
    return "hello siwadoc"


# endregion

# region 指定查询参数
from pydantic import BaseModel, Field


class QueryModel(BaseModel):
    page: int = Field(default=1, title="current page number")
    size: int = Field(default=20, title="size of page", ge=10, le=100)


class RespModel(BaseModel):
    id: int
    username: str


@app.route("/users/users_query", methods=["GET"])
@siwa.doc(query=QueryModel, tags=["user"])
def users_query(query: QueryModel):
    """
        对于大部分接口来说，我们要对请求参数进行校验，参数来源于url的查询参数。
        我们只需要基于Pydantic定义好对应的Model数据结构，该结构一方面可以用来做数据校验，另一方面可用于生成openapi所需的schema。
    :param query:
    :return:
    """
    print(query)
    return query.json()


@app.route("/users/users_body", methods=["POST"])
@siwa.doc(body=QueryModel, tags=['user'])
def users_body(body: QueryModel):
    """
        对于大部分接口来说，我们要对请求参数进行校验，以application/json格式作为请求体的参数。
        我们只需要基于Pydantic定义好对应的Model数据结构，该结构一方面可以用来做数据校验，另一方面可用于生成openapi所需的schema。
    :return:
    """
    return body.json()


# endregion

# region 指定返回结构
@app.route("/users/users_resp", methods=["POST"])
@siwa.doc(resp=QueryModel, tags=['user'])
def users_resp():
    """
        对于接口文档来说，除了要告诉前端需要传什么参数之外，还需要告诉他们返回的结构是什么，同样也只需要定义一个Model，写明有什么字段，
        字段对应的类型是什么即可。在doc装饰器中赋值给resp变量
    :return:
    """
    return "resp.json()"


@app.route("/users/users_all", methods=["POST"])
@siwa.doc(resp=RespModel, query=RespModel, body=QueryModel, tags=['user'])
def users_all(query: RespModel):
    """
        对于接口文档来说，除了要告诉前端需要传什么参数之外，还需要告诉他们返回的结构是什么，同样也只需要定义一个Model，写明有什么字段，
        字段对应的类型是什么即可。在doc装饰器中赋值给resp变量
    :return:
    """
    return "uery.json()"


# endregion


if __name__ == '__main__':
    print('---------------------API地址：http://127.0.0.1:5000/docs')
    print(app.url_map)  # 打印路由信息
    app.run(host="0.0.0.0", port=5000, debug=True)
