# -*- coding: UTF-8 -*-
# Desc: 和彩云自动打卡签到 gen: SCF-GENERATE
# Time: 2020/02/20 12:53:28
# Auth: xuthus
# SIG: QQ Group(824187964)

import json
from urllib import parse

import requests

OpenLuckDraw = False  # 是否开启自动幸运抽奖(首次免费, 第二次5积分/次) 不建议开启 否则会导致多次执行时消耗积分
Skey = "de767dd090d38b6ba816219eb7c05c93"  # 酷推 skey
Cookie = "sajssdk_2015_cross_new_user=1; WT_FPC=id=2d1131c72b7db82c81e1642729596695:lv=1642729629649:ss=1642729596695; ORCHES-C-TOKEN=6La6BMpPv/YjaKNxmJEmKOoDeRmghrgk53CSjPfbq4e/96N4XDxbXRLyEVj/ZJC3nE9ZBgUd9KPsnHmciodmOVu4dlVop6pTgLtcQA1Rv6xZt22KdysgjqdUrhferKhLDXfXt2ZWcl79DNmpvAyGSYy7+e7qL1EwfkJ7IXGpe0BJqm0f0saf2LlFKw8zTH6Ls3ktK8VT4UKSnb6XlQTvcLsM1bBoWkPwp5DsGN9LFTD4cg0zFqa3o/bZcjmNDC+wAlJvN8RXEysrtgCmrO6KXQ==; ORCHES-C-ACCOUNT=O+4XkPconuvrd3xb9KGQfw==; ORCHES-I-ACCOUNT-ENCRYPT=MTUyMjUwMTc2NjM=; ORCHES-I-ACCOUNT-SIMPLIFY=152****7663; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217e7a505ce1276-013890a9df55eb-3e604809-2073600-17e7a505ce27c6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.so.com%2Flink%3Fm%3Db28ozyRHdZUzd7NKo%252BB1mU5vexCPsqYx7wYBCfn23RiiO%252BSVOjxmBEn3x9OkSvbE7sgNLuX0sNd1ANEv7dohGXNdQJPWtbDWWkyZBp7c3MjH%252FM2Hvq39tpB7DoG8nDrz3Jkgw%252BBYXaacWlaWs%22%2C%22phoneNumber%22%3A%2215225017663%22%7D%2C%22%24device_id%22%3A%2217e7a505ce1276-013890a9df55eb-3e604809-2073600-17e7a505ce27c6%22%7D; sensors_stay_url=https%3A%2F%2Fyun.139.com%2Fw%2F%23%2Findex; sensors_stay_time=1642729630353"  # 抓包Cookie 存在引号时 请使用 \ 转义
Referer = "https://yun.139.com/w/"  # 抓包referer
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
    target = "https://hecaiyun.vercel.app/api/10086_calc_sign"
    payload = {
        "sourceId": 1003,
        "type": 1,
        "encryptTime": getEncryptTime()
    }
    resp = json.loads(requests.post(target, data=payload).text)
    if resp['code'] != 200:
        print('加密失败: ', resp['msg'])
    return resp['data']


def luckDraw():
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
    payload = parse.urlencode({
        "op": "luckDraw",
        "data": getTicket()
    })

    resp = json.loads(requests.post(target, headers=headers, data=payload).text)

    if resp['code'] != 10000:
        print('自动抽奖失败: ', resp['msg'])
        return '自动抽奖失败: ' + resp['msg']
    else:
        if resp['result']['type'] == '40160':
            return '自动抽奖成功: 小狗电器小型手持床铺除螨仪'
        elif resp['result']['type'] == '40175':
            return '自动抽奖成功: 飞科男士剃须刀'
        elif resp['result']['type'] == '40120':
            return '自动抽奖成功: 京东京造电动牙刷'
        elif resp['result']['type'] == '40140':
            return '自动抽奖成功: 10-100M随机长期存储空间'
        elif resp['result']['type'] == '40165':
            return '自动抽奖成功: 夏新蓝牙耳机'
        elif resp['result']['type'] == '40170':
            return '自动抽奖成功: 欧莱雅葡萄籽护肤套餐'
        else:
            return '自动抽奖成功: 谢谢参与'


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
    payload = parse.urlencode({
        "op": "receive",
        "data": ticket,
    })

    resp = json.loads(requests.post(target, headers=headers, data=payload).text)
    if resp['code'] != 10000:
        push('和彩云签到', '失败:' + resp['msg'])
    else:
        content = '签到成功\n月签到天数:' + str(resp['result']['monthDays']) + '\n总积分:' + str(
            resp['result']['totalPoints'])
        if OpenLuckDraw:
            content += '\n\n' + luckDraw()
        push('和彩云签到', content)


def main_handler(event, context):
    run()


# 本地测试
if __name__ == '__main__':
    run()
