#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

"""
1. 열기/닫기 형식이 이전거랑 같으면 곱하기
2. 열기/닫기 쌍이 맞으면 나누기
3. 열기/닫기 쌍이 안 맞으면 더하기
"""

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
            tmp*=2 # 열기/닫기 형식이 이전거랑 같으면 곱하기
    elif string[i] == "[":
        stack.append(string[i])
        if i==0 or string[i-1] == "(" or string[i-1] == "[" \
        or string[i-1] == ")" or string[i-1] == "]":
            tmp*=3 # 열기/닫기 형식이 이전거랑 같으면 곱하기
    
    # 닫는 괄호일 때
    elif string[i] == ")":
        if len(stack)==0 or stack[-1] == "[":
            answer = 0
            break
        if string[i-1] == "(":
            answer += tmp # 열기/닫기 쌍이 안 맞으면 더하기
        stack.pop()
        tmp //=2 # 열기/닫기 쌍이 맞으면 나누기
    elif string[i] == "]":
        if len(stack)==0 or stack[-1] == "(":
            answer = 0
            break
        if string[i-1] == "[":
            answer += tmp # 열기/닫기 쌍이 안 맞으면 더하기
        stack.pop()
        tmp //=3 # 열기/닫기 쌍이 맞으면 나누기
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