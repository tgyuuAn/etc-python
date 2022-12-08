import numpy as np

Size = 3
class TTT_Env():
    def __init__(self):
        self.state = np.full((Size,Size),'_')
        self.done = False
        self.turn = 'X'
        self.winner = None
        
    def print_state(self):
        col_count = 0

        print(f"{self.turn}의 차례입니다.\n")
        print("X  ", end = " ")
        for x in range(Size):
            print(x, end=" ")
        print("\n")
        for i in self.state:
            print(col_count,"|" , end=" ")
            for x in i:
                print(x, end =" ")
            col_count += 1
            print("\n")
    
    def step(self, r,c):
        if(self._check(r,c)):
            self.state[r,c] = self.turn        
            self.winner_check()
            self.turn = 'X' if self.turn == 'O' else 'O'
               
    def reset(self):
        self.state = np.full((Size,Size),'_')
        self.done = False
        self.turn = 'X'
        self.winner = None
    
    def winner_check(self):
        cross_check = 0
        reverse_cross_check = 0
        
        for i in range(Size):
            
            if((all(self.state[i,:] == [self.turn]*Size)) 
                or (all(self.state[:,i] == [self.turn]*Size))):
                self.winner = self.turn
                self.done = True
                
                #가로행이나 세로열이 모두 같은 값일 경우
                #승자는 지금 step을 둔 사람이다.
                
            if(self.state[i,i] == self.turn):
                cross_check += 1
                
                #왼쪽 위에서 오른쪽 아래를 향하는 대각선 값이 지금 step을 둔 사람의 값과 같을경우
                #cross_check를 1올린다.
                #cross_check가 3이 되면 이 또한 승자이다.
                
            if(self.state[i,(Size-1)-i] == self.turn):
                reverse_cross_check += 1
                #오른쪽 위에서 왼쪽 아래로 향하는 대각선을 체크한다.
        if (cross_check == Size or reverse_cross_check == Size):
            self.winner = self.turn
            self.done = True
    def _check(self,r,c):
        if(r>(Size-1) or c>(Size-1)):
            print("0~2 범위 내 좌표를 입력하세요.\n")
        elif(self.state[r,c]!="_"):
            print("빈 곳에 수를 두세요.\n")
        else:
            return True
        return False