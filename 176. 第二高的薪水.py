#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2020/8/26 下午10:32
@Author : Catherinexxx
@Site : 
@File : 176. 第二高的薪水.py
@Software: PyCharm
"""
select (select distinct salary from Employee order by salary desc limit 1,1) as SecondHighestSalary
