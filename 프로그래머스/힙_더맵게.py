import heapq

def solution(scoville, K):
    ''' https://programmers.co.kr/learn/courses/30/lessons/42626
    
    Notes:
        1. scoville을 heap으로 변환
        2. heap에서 2개 꺼내서 스코빌 계산
        3. 다시 heap에 추가 후 K가 넘는 지 확인
    
    Args:
        scoville (list): int값 스코빌지수들을 담은 리스트
        K (int): 목표 스코빌 값

    Returns:
        answer (int): 스코빌을 섞은 최솟값

    '''
    
    answer = 0
    heap = scoville
    heapq.heapify(heap)
    
    while len(heap) != 1:        
        heapq.heappush(heap, heapq.heappop(heap)+heapq.heappop(heap)*2)
        
        answer += 1

        if K <= heap[0]:
            return answer
    
    return -1


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
