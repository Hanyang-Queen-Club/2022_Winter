#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 파이썬 시간초과 / pypy3 통과
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(input().strip()[4:-4]) # anta와 tica를 제외한 가운데 부분만 추출

alpha = ['a', 'n', 't', 'i', 'c']
alpha_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
answer = 0

def choose_alpha(n, start): # 백트랙킹으로 n개만큼 알파벳을 alpha리스트에 추가
    global answer
    if n == 0: 
        answer = max(answer, check()) # 최댓값으로 answer 초기화
        return
    for i in range(start, len(alpha_list)):
        alpha.append(alpha_list[i])
        choose_alpha(n-1, i+1) # 배울수있는 알파벳개수 줄이고, alpha_list에서 start지점 인덱스값은 늘리고
        alpha.pop()

def check(): # anta와 tica를 제외한 가운데 부분이 alpha에 있는지 체크
    answer = 0
    for words in arr:
        isRead = True
        for i in range(len(words)):
            if words[i] not in alpha: # 가운데 부분이 alpha 안에 없다면, 배운 단어만으로 해당 글자를 읽을 수 없음
                isRead = False
                break
        if isRead: # 가운데 부분이 alpha 안에 모두 있다면, 배운 단어만으로 해당 글자를 읽을 수 있음
            answer += 1
    return answer


if K < 5:
    print(answer)
elif K == 26:
    answer = N
    print(answer)
else:
    choose_alpha(K-5, 0) # 고정으로 배워야하는 a,n,t,i,c을 뺀 나머지(배울수있는 알파벳)에 대해 백트래킹 시작 
    print(answer)
