import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:

        a = heapq.heappop(scoville)
        if a >= K:
            return answer
        if not scoville:
            return -1
        b = heapq.heappop(scoville)
        answer += 1
        tmp = a + 2 * b
        heapq.heappush(scoville, tmp)

# input() scoville과 K가 주어짐