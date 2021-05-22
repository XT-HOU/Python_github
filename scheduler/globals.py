# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    全局对象
"""
__author__ = "HOU"

from flask import Flask
import platform

app = Flask(__name__)
# app.debug = True
# 系统类型
os_type = platform.system()
os_name = platform.node()
# 提交的编排App集合
app_list = []
ssh_list = []
# 编排AppxmlDemo
app_xml = """<workflowApp path="/usr/local/code" name="任务单_编排名_time" type="0" state="0">
	<start to="start-node"/>
	<action name="start-node" level="2" >
		<shell path="/usr/python" type = "python3" >
			<nameNode>spark_python_test.py</nameNode>
			<configuration>
				<property>
				<name>mapred.job.queue.name</name>
				<value>${queueName}</value>
				</property>
			</configuration>
			<exec>执行</exec>
			<argument>结论</argument>
		</shell>
	<ok to="end"/>
	<error to="fail"/>
	</action>
	<action name="app1Node" level ="1">
		<shell path="/usr/local/code/app1Node" type = "python3">
		<jobTracker>${jobTracker}</jobTracker>
		<nameNode>app1_名称</nameNode>
			<configuration>
				<property>
				<name>mapred.job.queue.name</name>
				<value>${queueName}</value>
				</property>
			</configuration>
		<exec>echo</exec>
		<argument>hi shell in oozie</argument>
		</shell>
	<ok to="end"/>
	<error to="fail"/>
	</action>
	<action name="endNode" level ="888">
		<shell path="/usr/local/code/endNode" type = "python3" >
			<jobTracker>任务跟踪</jobTracker>
			<nameNode>app888_名称</nameNode>
			<configuration>
				<property>
				<name>mapred.job.queue.name</name>
				<value>${queueName}</value>
				</property>
			</configuration>
			<exec>执行</exec>
			<argument>结论</argument>
		</shell>
	<ok to="end"/>
	<error to="fail"/>
	</action>
<kill name="fail">
<message>Map/Reduce failed, error message[${wf:errorMessage(wf:lastErrorNode())}]</message>
</kill>
<end name="end"> end </end>
</workflowApp>
"""
