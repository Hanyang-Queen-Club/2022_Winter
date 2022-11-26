#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

string = list(input()[:-1])
stack = []
answer = 0
tmp = 1

for i in range(len(string)):
    # 여는 괄호일 때
    if string[i] == "(":
        stack.append(string[i])
        if i==0 or string[i-1] == "(" or string[i-1] == "[" \
        or string[i-1] == ")" or string[i-1] == "]":
            tmp*=2
    elif string[i] == "[":
        stack.append(string[i])
        if i==0 or string[i-1] == "(" or string[i-1] == "[" \
        or string[i-1] == ")" or string[i-1] == "]":
            tmp*=3
    
    # 닫는 괄호일 때
    elif string[i] == ")":
        if len(stack)==0 or stack[-1] == "[":
            answer = 0
            break
        if string[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //=2
    elif string[i] == "]":
        if len(stack)==0 or stack[-1] == "(":
            answer = 0
            break
        if string[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //=3
    # print(i, string[i], tmp, answer)

if len(stack) != 0:
    answer = 0
print(answer)

"""
(()[[]])([])
28

[][]((])
0
"""