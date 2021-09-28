문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.



def solution(prices):
    answer = []
    for idx, i in enumerate(prices):
        cnt = 0;
        for j in range(idx+1, len(prices)): # 비교대상은 다음 인덱스부터 끝까지 비교
            cnt += 1
            if prices[j] < i: break # 자신보다 작은 수가 나오면 종료
        answer.append(cnt)
            
    return answer
