#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

# a를 b로 만들지 않고, b를 a로 만들자.
a,b = map(int,input().split())
cnt = 1
while(b!=a):
    cnt+=1
    temp = b
    if b%10 == 1: # 끝자리에 1이 존재하면 ex: 11이면 이전 수가 바로 1로 줄어드므로 끝의 1을 빼는 작업 수행
        b//=10
    elif b%2 == 0: # 2로 나눠떨어진다면 2로 나누기
        b//=2
    
    if temp == b: # 위와 같은 연산으로 수행이 불가능하다면 -1
        print(-1)
        break
else: # b를 a로 만들수 있으면 연산 횟수 프린트
    print(cnt)