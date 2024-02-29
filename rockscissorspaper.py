import random


def rock_paper_scissors():
    list = ['가위', '바위', '보']
    
    count = {'승': 0, '무': 0, '패': 0}
    while True:
            
        
            user = input("가위, 바위, 보 중 하나를 선택하세요 :" )
        
            if user not in list:
                print("잘못된 입력입니다. 가위, 바위, 보 중 하나를 입력해주세요")
                continue
        
            computer = random.choice(list)
        
            print(f"사용자: {user}, 컴퓨터: {computer}")
        
            if user == computer:
                print("비겼습니다!")
                count['무'] += 1
            elif (user == '가위' and computer == '보') or \
                (user == '바위' and computer == '가위') or \
                (user == '보' and computer == '바위'):
                print("이겼습니다^^")
                count['승'] += 1
            else:
                print("졌습니다ㅠㅠ")
                count['패'] += 1
            while True:

                retry = input("계속하시겠습니까? y/n : ").lower()
                if retry == 'y':
                    
                    break
                elif retry == 'n':
                    print("게임 결과:")
                    print(f"승: {count['승']}, 무: {count['무']}, 패: {count['패']}")
                    return
                else:
                    print("y나 n 둘중 하나를 입력해주세요")

rock_paper_scissors()
