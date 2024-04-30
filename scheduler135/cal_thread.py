# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    计算线程
"""
__author__ = "HOU"

import time
import threading

from globals import app_list, logger
from default import Default, AppState
import app_ssh


def app_thread():
    """ 方法注释：
        启动计算线程,
    """
    t = threading.Thread(target=start_fun)
    t.start()
    logger.info("启动计算线程......")


def start_fun():
    while True:
        time.sleep(1)
        # 公共空间 app
        public_app = [item for item in app_list if item.type == Default.PUBLIC_APP.value
                      and item.state == AppState.APP_STATE0.value]
        # 个人空间 app
        private_app = [item for item in app_list if item.type == Default.PRIVATE_APP.value
                       and item.state == AppState.APP_STATE0.value]
        try:
            if len(public_app) > 0:
                apps_deal(public_app)
            else:
                if len(private_app) > 0:
                    apps_deal(private_app)
        except Exception as e:
            logger.error(e)


def apps_deal(apps):
    """方法注释：
        计算编排流程 app
    :param apps:编排流程
    """
    for app in apps:
        try:
            actions = app.action
            # 确定执行顺序
            actions.sort(key=lambda x: x.level)
            # 指标模型计算
            actions_deal(app, actions)
            # 发送完后移除编排
            if len(actions) == 0:
                apps_remove(app, apps)
        except Exception as e:
            # 移除错误 app
            apps_remove(app, apps)
            logger.error(e)


def apps_remove(app, apps):
    """
        发送完后移除编排,移除有问题编排
    """
    apps.remove(app)
    app_list.remove(app)


def actions_deal(app, actions):
    """
        指标模型分布式计算
    """
    remove_actions = []
    if app.state == AppState.APP_STATE0.value:
        for action in actions:
            path = action.shell_path
            type = action.shell_type
            name = action.shell_nameNode
            # 发送 shell 命令
            res = app_ssh.send_cmd(type, path, name)
            if res == Default.OK.value:
                # 移除指标模型
                remove_actions.append(action)
            else:
                break

    for action in remove_actions:
        actions.remove(action)


if __name__ == '__main__':
    app_thread()
