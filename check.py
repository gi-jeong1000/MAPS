"""
너비 우선 탐색 시행해야함
1,1 -> n,m으로 갈수 있는 최단 경로 탐색
BFS -> 큐 구조 사용
간선이 올라가면 +1 해준다.
n,m에 도착하면 stop
1인 것을 따라가야함
"""

def solution(maps):
    answer = 0 #간선의 개수
    n = len(maps[0]) # 가로
    m = len(maps) # 세로
    find = False # n,m으로 도달했는가?
    check = [list(False for i in range(n)) for i in range(m)] # 체킹 리스트
    Xgo = [1,0,-1,0]
    Ygo = [0,1,0,-1]
    queue = [[1,1]]
    while queue:
        first = queue.pop(0)
        for j in Ygo:
            for i in Xgo:
                y = first[0]+j
                x = first[1]+i
                if 0<=x<n and 0<=y<m:
                    if maps[y][x] == 1 and check[y][x] == False:
                        check[y][x] == True
                        answer +=1
                        queue.append([y,x])
                        if y==m and x ==n:
                            find == True
                            break

    if find == False:
        answer == -1

    return answer

a =""
a[1:]
print (a[1:]=="")