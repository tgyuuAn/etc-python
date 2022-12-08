from TTT_env import *
from Play_auto import *
        
env = TTT_Env()
play = 1
loop = 5
winner_play_X = {'X' : 0, 'O' : 0, None:0}
winner_play_O = {'X' : 0, 'O' : 0, None:0}
text = input("게임 과정을 지켜보겠습니까? (no 입력시 보지않음):")
for player in ['X','O']:
    computer = 'O' if player == 'X' else 'X'
    
    for _ in range(loop):
        
        if text != "no" :
            print("게임시작!!")
            env.print_state()
        while not env.done:
        
            if player == env.turn:
                r,c = my_action(env.state,computer) 
            
            else:
                r,c = random_action(env.state)
                
            if text != "no" :
                print(f"플레이어 {env.turn}은 {r}, {c}에 수를 두었습니다.")
                env.step(r,c)
                env.print_state()
            
            else:
                env.step(r,c)
                
            if("_" not in env.state):
                env.done = True
                
        if player == "X":
            winner_play_X[env.winner] += 1
        else:
            winner_play_O[env.winner] += 1
            
        if text != "no" :
            print() 
            if env.winner == None:
                print("무승부입니다.")
            else:
                print(f"이 게임의 승자는 플레이어 {env.winner}입니다.")
                
        env.reset()
print(f"X 플레이 : win {100*winner_play_X['X']/loop}%, lose {100*winner_play_X['O']/loop}%, draw {100*winner_play_X[None]/loop}%")
print(f"O 플레이 : win {100*winner_play_O['O']/loop}%, lose {100*winner_play_O['X']/loop}%, draw {100*winner_play_O[None]/loop}%")