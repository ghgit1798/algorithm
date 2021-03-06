from collections import deque

def solution(prices):
    '''
    Notes:
        1. 1번째 가격을 꺼낸다.
        2. 2번째, 3번째... 주식 가격보다 작은 가격을 만날때까지 +1초
        3. 2번 결과 seconds를 저장한다.
            - prices의 최대길이는 100,000
            - price의 최대값은 10,000
    Args:
        prices (list): 주식 가격(int)을 담은 리스트

    Returns:
        answer (list): 주식이 떨어지지 않은 초를 담은 리스트
    '''
    
    answer = []
    prices = deque(prices)

    while prices:
        p = prices.popleft()
        
        cnt = 0
        for price in prices:
            if p > price:
                cnt += 1
                break
            cnt += 1
        
        answer.append(cnt)

    return answer

def stack_solution(prices):
    answer = [0]*len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i) 
    
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1

    return answer

def extra_solution(prices):    
    answer = [0]*len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

prices = [1,2,3,2,3]
print(stack_solution(prices))