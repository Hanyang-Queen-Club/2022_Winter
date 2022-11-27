#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())

Alist = list(map(int, input().split()))
sign_list = list(map(int, input().split()))

plus = sign_list[0]
minus = sign_list[1]
multiple = sign_list[2]
division = sign_list[3]

new_sign_list = []

if plus > 0: 
    for _ in range(plus):
        new_sign_list.append('+')
if minus > 0: 
    for _ in range(minus):
        new_sign_list.append('-')
if multiple > 0: 
    for _ in range(multiple):
        new_sign_list.append('*')
if division > 0: 
    for _ in range(division):
        new_sign_list.append('/')

# print(new_sign_list)

# 중요!! 중복제거해서 시간초과 방지
sign_permutation = set(list(permutations(new_sign_list, len(new_sign_list)))) # [('+', '*'), ('*', '+')]

# print(sign_permutation)

tmp_answers = []
for signs in sign_permutation:
    total = Alist[0]
    for i in range(1, N):
        if signs[i-1] == '+': total += Alist[i]
        elif signs[i-1] == '-': total -= Alist[i]
        elif signs[i-1] == '*': total *= Alist[i]
        elif signs[i-1] == '/': total = int(total/Alist[i])
    tmp_answers.append(total)

# print(tmp_answers)
print(max(tmp_answers))
print(min(tmp_answers))
"""
3
3 4 5
1 0 1 0
35
17
"""