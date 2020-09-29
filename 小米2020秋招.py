#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/9/15 下午7:34
@Author : Catherinexxx
@Site : 
@File : 小米2020秋招.py
@Software: PyCharm
"""
# 米兔收集胡萝卜 ac
# m, n = list(map(int, input().split()))
# data = [list(map(int, input().split())) for _ in range(m)]
#
# dp = [[0]*(n+1) for _ in range(m+1)]
# for i in range(1, m+1):
#     for j in range(1, n+1):
#         dp[i][j] = data[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])
# print(dp[-1][-1])

# NMS ac29
m, t = input().split()
m = int(m)
t = float(t)
data = [list(map(float, input().split())) for _ in range(m)]
# m, t = 3, 0.3
# data = [[50.0, 51.0, 180.0, 200.0, 0.9],
# [48.0, 53.0, 170.0, 210.1, 0.8],
# [200.0, 51.0, 242.1, 81.0, 0.7]
# ]
def innerArea(bbox1, bbox0):
    x11, y11, x12, y12 = bbox1[0], bbox1[1], bbox1[2], bbox1[3]
    x01, y01, x02, y02 = bbox0[0], bbox0[1], bbox0[2], bbox0[3]
    xx1 = max(x11, x01)
    yy1 = max(y11, y01)
    xx2 = min(x12, x02)
    yy2 = min(y12, y02)
    return (xx2-xx1+1)*(yy2-yy1+1)

def NMS(bboxes, th):
    areas = []
    res = list(range(len(bboxes)))
    for bbox in bboxes:
        x1, y1, x2, y2, score = bbox[0], bbox[1], bbox[2], bbox[3], bbox[4]
        areas.append((x2-x1+1)*(y2-y1+1))
    for i in range(m-1):
        for j in range(i+1, m):
            if j in res:
                inn = innerArea(data[i][:4], data[j][:4])
                iou = inn/(areas[i]+areas[j]-inn)
                if iou > th:
                    res.remove(j)
    for i in res:
        print(' '.join(list(map(str, data[i]))))
data.sort(key=lambda x: x[-1], reverse=True)
NMS(data, t)