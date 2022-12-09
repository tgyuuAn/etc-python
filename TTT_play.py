from TTT_env import *    
from Play_auto import *
import time

env = TTT_Env()
play = 1
while play:
    
    print("\n\n==================================")
    
    while True:
        try:
            player = input("어떤 말을 선택하시겠습니까? ( X or O ) : ")
            if(player == "X" or player == "O"):
                break
            else:
                raise()
        except:
            print("정확한 값을 입력해주세요.")
    print("게임시작!!\n\n")
    env.print_state()
    while not env.done:
        
        print()
        
        if(player == env.turn):
            action = input(f"플레이어 {env.turn}은(는) 수를 놓을 행과 열의 인덱스를 입력하세요. (뛰어쓰기로 구분): ")
            r, c = map(int,action.split(" "))
            
        else:
            r, c = my_action(env.state,player)
        
        print(f"플레이어 {env.turn}은 {r}, {c}에 수를 두었습니다.")
        env.step(r,c)
        env.print_state()
        time.sleep(0.5)
    
    print() 
    
    if env.winner == None:
        print("무승부입니다.")
    else:
        print(f"이 게임의 승자는 플레이어 {env.winner}입니다.")
        
    while True:
        try:
            replay = input("다시 플레이 하겠습니까? (yes or no)")
            
            if(replay == "yes"):
                env.reset()
                break
                
            elif(replay == "no"):
                play = 0
                break
            else:
                raise()
        except:
            print("yes 나 no 둘 중 하나를 입력해주세요.")

            #