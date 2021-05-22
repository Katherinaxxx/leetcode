#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2021/4/19 4:33 PM
@Author : Catherinexxx
@Site : github.com/Katherinaxxx
@File : 兴业数金2021春招.py
@Description: 判断输入的字符串是否包含字母和数字，并统计字符数目
"""
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    return False

def is_english(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or \
        (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    return False

def main():
    # s = '123 abc def 中kl国  abcde 伟大'
    s = input()
    res = {'数字': 0, '字母': 0, '其他符号': 0, '汉字': 0}
    for i in s:
        if i.isnumeric():
            res['数字'] += 1
        elif is_chinese(i):
            res['汉字'] += 1
        elif is_english(i):
            res['字母'] += 1
        else:
            res['其他符号'] += 1
    for k, v in res.items():
        print('%s: %s' % (k, v))

if __name__ == '__main__':
    main()