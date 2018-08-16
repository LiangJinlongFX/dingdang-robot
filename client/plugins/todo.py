# -*- coding: utf-8 
"""
    备忘录插件(基于TaskWarrior)
    功能
        添加备忘
        查看备忘
"""

from __future__ import print_function
import time
import logging
import os
import subprocess

SLUG = "todo"
WORDS = ["BEIWANG"]

def handle(text, mic, profile, wxbot=None, pixels=None, oled=None):
    from app_utils import create_reminder
    logger = logging.getLogger(__name__)
    if any(word in text for word in [u'查看备忘',u'检查备忘']):
        p = subprocess.Popen('task status:pending count',stdout=subprocess.PIPE, shell=True)
        p.wait()
        pending_task_num = int(p.stdout.readline())
        p = subprocess.Popen('task list',stdout=subprocess.PIPE,shell=True)
        p.wait()
        lines = p.stdout.readlines()[3:(3 + pending_task_num)]
        print(lines)
    elif any(word in text for word in [u'添加备忘']):
        sentence = text.replace("添加备忘", "")
        if create_reminder(sentence,"20180803"):
            mic.say('添加备忘成功', cache=True)
        else:
            mic.say('添加备忘失败', cache=True)

def isValid(text):
    return any(word in text for word in [u'添加备忘',u'查看备忘',
        u'备忘'])