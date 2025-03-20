import sys
sys.stdin = open("input.txt","r")

import heapq
name="ABCDE"
n,m=map(int,input().split())    # n은 정점의 개수, m은 간선의 개수
arr=[[] for _ in range(n)]  # 인접리스트
for _ in range(m):
    a,b,c=map(int,input().split()) #시작,도착,비용
    arr[a].append((b,c))
start,end=map(int,input().split()) #시작점,도착점인덱스
result=[21e8]*n
heap=[(0,start)]    # 힙에는 (비용, 인덱스) 순으로 넣음 : 비용 기준으로 오름차순 정렬하기 위해서
result[start]=0 # 시작점에서 시작점으로의 비용은 0

while heap:
    
    ky_cost,ky=heapq.heappop(heap) # 시작점에서 경유지까지의 정보 (힙에서 가져온 정보)

    if result[ky]<ky_cost: continue # 힙에서 가져온 정보가 최신 데이터 값보다 크다면 pass

    for dochack,dochack_cost in arr[ky]: # 경우지에서 도착점까지의 정보를 인접리스트에서 가져오기
        Baro=result[dochack] # 시작->도착
        New=ky_cost+dochack_cost # 시작 -> 경유지 -> 도착
        if New<Baro: # 경유지 들리는게 더 저렴하다면
            result[dochack]=New # result 갱신
            heapq.heappush(heap,(New,dochack)) # heap에 갱신된 정보를 업데이트

print(*result)
print(result[end])
