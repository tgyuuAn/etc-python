import numpy as np

class TTT_Env():
    def __init__(self):
        self.state = np.full((3,3),'_')
        self.done = False
        self.turn = 'X'
        self.winner = None

    def print_state(self):
        for i in self.state:
            for x in i:
                print(x, end =" ")
            print()

    
    def step(self, r,c):
        if(self._check(r,c)):
            self.state[r,c] = self.turn        
            self._winner_check()
            self.turn = 'X' if self.turn == 'O' else 'O'
            if "_" not in self.state:
                self.done = True

    def reset(self):
        self.state = np.full((3,3),'_')
        self.done = False
        self.turn = 'X'
        self.winner = None
    
    def _winner_check(self):
        cross_check = 0
        reverse_cross_check = 0
        for i in range(3):
            if((all(self.state[i,:] == [self.turn]*3)) 
                or (all(self.state[:,i] == [self.turn]*3))):
                self.winner = self.turn
                self.done = True
                #가로행이나 세로열이 모두 같은 값일 경우
                #승자는 지금 step을 둔 사람이다.

            if(self.state[i,i] == self.turn):
                cross_check += 1
                #왼쪽 위에서 오른쪽 아래를 향하는 대각선 값이 지금 step을 둔 사람의 값과 같을경우
                #cross_check를 1올린다.
                #cross_check가 3이 되면 이 또한 승자이다.

            if(self.state[i,2-i] == self.turn):
                reverse_cross_check += 1
                #오른쪽 위에서 왼쪽 아래로 향하는 대각선을 체크한다.
        
        if (cross_check == 3 or reverse_cross_check == 3):
            self.winner = self.turn
            self.done = True

    def _check(self,r,c):
        if(r>2 or c>2):
            print("0~2 범위 내 좌표를 입력하세요.\n")
        elif(self.state[r,c]!="_"):
            print("빈 곳에 수를 두세요.\n")
        else:
            return True
        return False

if __name__ == "__main__":
    env = TTT_Env()
    print("게임시작!!")
    env.print_state()
    while not env.done:
        action = input(f"플레이어 {env.turn}은(는) 수를 놓을 행과 열의 인덱스를 입력하세요. (뛰어쓰기로 구분): ")
        r, c = action.split(" ")
        env.step(int(r),int(c))
        env.print_state()
    
    if env.winner == None:
        print("무승부입니다.")
    else:
        print(f"이 게임의 승자는 플레이어 {env.winner}입니다.")
###