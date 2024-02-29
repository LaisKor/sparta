import random

def upanddowngame():
    while True:
        number = random.randint(1, 100)
        attempts = 0

        print("1 부터 100 사이의 숫자를 입력해주세요")

        while True:
            guess = input("숫자를 입력해주세요: ")
            
            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    raise ValueError("범위 안에 있는 숫자를 입력해주세요!")
            except ValueError as e:
                print(e)
                continue
            
            
            attempts += 1

            if guess < number:
                print("UP!")
            elif guess > number:
                print("DOWN!")
            else:
                print("맞췄습니다!")
                break
            
        while True:
            restart = input("다시 하시겠습니까? (y/n) :").lower()
            if restart == 'y':
                print(f"전 플레이어의 시도 횟수 : {attempts}")
                break
            elif restart == 'n':
                print("게임을 종료합니다")
                print(f"시도 횟수 : {attempts}")
                return
            else:
                print("y나 n 중 하나를 입력하세요.")

upanddowngame()

