# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
json 应用
"""

import json


class JSON2Object(object):
    def __init__(self, d):
        self.__dict__ = d


def json2obj(s, class_name):
    return json.loads(s, object_hook=class_name)


def obj2json(a):
    return json.dumps(a, default=lambda obj: obj.__dict__, sort_keys=True, ensure_ascii=False)


# --------------------------------------------
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


if __name__ == '__main__':
    a = {"status": 1, "info": "发布成功", "data": {"id": "52", "feed_id": "70"}}
    b = json2obj(json.dumps(a), JSON2Object)
    print(b.info)
    print(obj2json(a))
    # --------------------------------------------
    # '{"name": "Bob", "age": 20, "score": 88}'
    student = Student("侯", 23, 99)
    json_str = json.dumps(obj=student.__dict__, ensure_ascii=False)
    print(type(json_str))
    student = json.loads(json_str, object_hook=dict2student)
    print(type(student))
    print(student.name)
