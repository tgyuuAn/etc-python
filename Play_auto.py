import random as rd

Size = 5 

def random_action(state):    
    while True:
        r = rd.randint(0,(Size-1))
        c = rd.randint(0,(Size-1))
        if(state[r][c]=="_"):
            return r,c
        
def my_action(state,computer):
    
    #가운데가 비어있으면 무조건 가운데가 먹는 것이 이득임.
    if(state[(Size//2)][(Size//2)]=="_"): return (Size//2),(Size//2)
    player = "X" if computer == "O" else "O"
    
    
    #플레이어가 끝낼 수 있으면 공격해서 끝냄.
    check = [[state[row][col] == player for col in range(Size)] for row in range(Size)]
    for idx in range(Size):    
    #행 검사
        if sum(check[idx]) == (Size-1) and state[idx][check[idx].index(False)] == "_":
            return idx, check[idx].index(False)
        
    #열 검사
        temp = [x[idx] for x in check]
        if sum(temp) == (Size-1) and state[temp.index(False)][idx] == "_":
            return temp.index(False), idx
    #정대각선 검사
        temp = [check[idx][idx] for idx in range(Size)]
        if sum(temp) == (Size-1) and state[temp.index(False)][temp.index(False)] == "_":
            return temp.index(False), temp.index(False)
    
    #역대각선 검사
        temp = [check[idx][(Size-1)-idx] for idx in range(Size)]
        if sum(temp) == (Size-1) and state[temp.index(False)][(Size-1)-temp.index(False)] == "_":
            return temp.index(False), (Size-1)-temp.index(False)
        
    #아닐경우, 수비코드
    check = [[state[row][col] == computer for col in range(Size)] for row in range(Size)]
    for idx in range(Size):    
        #행 검사
        if sum(check[idx]) == (Size-1) and state[idx][check[idx].index(False)] == "_":
            return idx, check[idx].index(False)
        
        #열 검사
        temp = [x[idx] for x in check]
        if sum(temp) == (Size-1) and state[temp.index(False)][idx] == "_":
            return temp.index(False), idx
        #정대각선 검사
        temp = [check[idx][idx] for idx in range(Size)]
        if sum(temp) == (Size-1) and state[temp.index(False)][temp.index(False)] == "_":
            return temp.index(False), temp.index(False)
    
        #역대각선 검사
        temp = [check[idx][(Size-1)-idx] for idx in range(Size)]
        if sum(temp) == (Size-1) and state[temp.index(False)][(Size-1)-temp.index(False)] == "_":
            return temp.index(False), (Size-1)-temp.index(False)
    
    
    #수비할 것이 없으면 랜덤코드
    while True:
        r = rd.randint(0,(Size-1))
        c = rd.randint(0,(Size-1))
        if(state[r][c]=="_"):
            return r,c