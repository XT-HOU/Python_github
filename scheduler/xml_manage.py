# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    评估流程编排xml处理
"""
__author__ = "HOU"

import json

from lxml import objectify, etree

from globals import app_list, app_xml, hosts
from default import Default, AppState


def app_xml_obj(app_xml):
    """方法注释：
        编排xml转对象
    """
    xml = objectify.fromstring(app_xml)
    app = WorkflowApp()
    app.id = xml.attrib['id']
    app.name = xml.attrib['name']
    app.type = xml.attrib['type']
    app.path = xml.attrib['path']
    app.state = xml.attrib['state']
    app.start = xml.start.attrib
    action = get_actions(xml)
    app.action = action
    return app


def get_actions(xml):
    """方法注释：
        构建评估模型集合
    :param xml: 编排xml
    :return: 返回评估模型集合
    """
    action_list = []
    for item in xml.action:
        action = Action()
        action.name = item.attrib['name']
        action.level = item.attrib['level']
        action.shell_path = item.shell.attrib['path']
        action.shell_type = item.shell.attrib['type']
        action.shell_nameNode = item.shell.nameNode
        action.shell_exec = item.shell.exec
        action.shell_argument = item.shell.argument
        action_list.append(action)
    return action_list


class WorkflowApp(object):
    """
        编排xml对象
    """
    # __slots__ = ('__id', '__name', '__type', '__path', '__state', '__start', '__action')

    @property
    def id(self):
        """ 编排id"""
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        """ 编排名"""
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        """ 个人空间/公共空间 """
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def path(self):
        """ 编排路径"""
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def state(self):
        """ 开始节点"""
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
        
    @property
    def start(self):
        """ 开始节点"""
        return self.__start

    @start.setter
    def start(self, value):
        self.__start = value

    @property
    def action(self):
        """ 指标模型列表"""
        return self.__action

    @action.setter
    def action(self, value):
        self.__action = value


class Action(object):
    """
        指标模型对象
    """
    @property
    def name(self):
        """ 指标模型名"""
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def level(self):
        """ 指标模型执行等级"""
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value


def app_judge(pb_model):
    """方法注释：
        判断编排 App 是否符合提交条件
    """
    # 判断是否重复提交
    exist_app = [item for item in app_list if item.name == pb_model.name]
    if len(app_list) < Default.APP_LIST_LEN.value and len(exist_app) == 0:
        return True
    else:
        return False


def set_app_state(app_id, app_state):
    """方法注释：
        更改编排 App 计算状态
    """
    # 判断是否存在
    exit_app = [one for one in app_list if one.id == app_id]
    if len(exit_app) == 1:
        exit_app[0].state = app_state
    else:
        return "编排：%s 不存在%d" % (app_id, len(exit_app))


class Config(object):
    pass


def get_config():
    """方法注释：
        读取配置文件
    """
    cfg = etree.parse("scheduler.cfg")
    result = etree.tostring(cfg, pretty_print=True)
    xml = objectify.fromstring(result)

    for item in xml.hosts.host:
        host = Config()
        host.type = item.attrib['type']
        host.ip = item
        hosts.append(host)


if __name__ == '__main__':
    # app = app_xml_obj(app_xml)
    # app_list.append(app)
    # print(str(app.__dict__))
    get_config()
