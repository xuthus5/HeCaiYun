# -*- coding: UTF-8 -*-
# Desc: 和彩云自动打卡签到 gen: SCF-GENERATE
# Time: 2020/02/20 12:53:28
# Auth: xuthus
# SIG: QQ Group(824187964)

import json
from urllib import parse

import requests

Skey = ""       # 酷推 skey
Cookie = ""     # 抓包Cookie 存在引号时 请使用 \ 转义
Referer = ""    # 抓包referer
UA = "Mozilla/5.0 (Linux; Android 10; M2007J3SC Build/QKQ1.191222.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 MCloudApp/7.6.0"


def push(title, content):
    url = "https://push.xuthus.cc/send/" + Skey
    data = title + "\n" + content
    # 发送请求
    res = requests.post(url=url, data=data.encode('utf-8')).text
    # 输出发送结果
    print(res)


def getEncryptTime():
    target = "http://caiyun.feixin.10086.cn:7070/portal/ajax/tools/opRequest.action"
    headers = {
        "Host": "caiyun.feixin.10086.cn:7070",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": UA,
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://caiyun.feixin.10086.cn:7070",
        "Referer": Referer,
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": Cookie,
    }
    payload = parse.urlencode({
        "op": "currentTimeMillis"
    })
    resp = json.loads(requests.post(target, headers=headers, data=payload).text)
    if resp['code'] != 10000:
        print('获取时间戳失败: ', resp['msg'])
        return 0
    return resp['result']


def getTicket():
    target = "https://hecaiyun.vercel.app/api/calc_sign"
    payload = {
        "sourceId": 1003,
        "type": 1,
        "encryptTime": getEncryptTime()
    }
    resp = json.loads(requests.post(target, data=payload).text)
    if resp['code'] != 200:
        print('加密失败: ', resp['msg'])
    return resp['data']


# key 参数是推送的 key 可能是酷推的也可能是Server酱的 这里通过输入框由平台自动填入
def run():
    target = "http://caiyun.feixin.10086.cn:7070/portal/ajax/common/caiYunSignIn.action"
    headers = {
        "Host": "caiyun.feixin.10086.cn:7070",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": UA,
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://caiyun.feixin.10086.cn:7070",
        "Referer": Referer,
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": Cookie,
    }

    ticket = getTicket()
    print('ticket: ', ticket)
    payload = parse.urlencode({
        "op": "receive",
        "data": ticket,
    })

    print('raw payload: ', payload)

    resp = json.loads(requests.post(target, headers=headers, data=payload).text)
    if resp['code'] != 10000:
        push('和彩云签到', '失败:' + resp['msg'])
    else:
        push('和彩云签到', '签到成功\n月签到天数:' +
             str(resp['result']['monthDays']) + '\n总积分:' + str(resp['result']['totalPoints']))


def main_handler(event, context):
    run()


# 本地测试
if __name__ == '__main__':
    run()
