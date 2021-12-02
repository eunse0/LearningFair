import random

yourname = input("이름을 입력해주세요 : ")               #사용자 이름 입력
print("안녕하세요 [%s]님. 게임을 시작하겠습니다."%yourname)


print("\n~~~~~~~~가위 바위 보 3 종 세트~~~~~~~~")
choice = input("- 게임선택(가위바위보 / 하나빼기 / 묵찌빠) : ") #가위바위보와 묵찌빠 중 선택
while choice != '하나빼기' and choice != '묵찌빠' and choice != '가위바위보':
    print("잘못 입력하셨습니다.")
    choice = input("- 게임선택(가위바위보 / 하나빼기 / 묵찌빠) : ")

def gbb(): #가위바위보 게임
    num=1
    winnum=0
    while True:
        print("\n가위바위보 게임 %d ROUND를 시작합니다."%num)
        print("* 패배 시 게임이 종료됩니다.")
        one = input ("- 선택 (가위 바위 보) : ")
        while one != "가위" and one != "바위" and one != "보":
                print("잘못 입력 하셨습니다.")
                one = input('- 선택 (가위 바위 보) : ')
        
 
        com = random.choice(["가위" , "바위" , "보"])
        print("\n[",yourname, "] :",one)
        print("[ 컴퓨터 ] :",com)

        if (com == one):
                print("- 결과 : 무승부")
                num+=1
        elif (com == "가위" and one == "바위"):
                print("- 결과 : 승")
                num+=1
                winnum+=1
        elif (com == "바위" and one == "보"):
                print("- 결과 : 승")
                num+=1
                winnum+=1
        elif (com == "보" and one == "가위"):
                print("- 결과 : 승")
                num+=1
                winnum+=1
        else:
                print("- 결과 : 패")
                print("\n게임 종료. [%s]님 총 %d번 승리하셨습니다."%(yourname,winnum))
                break

    
def hanabbagi():     #하나빼기 게임
    num=1
    win=0
    winnum=0
    while True :
        print("\n하나빼기 게임 %d ROUND를 시작합니다."%num)
        print("* 패배 시 게임이 종료됩니다.")
        one = input ("- 첫번째 선택 (가위 바위 보) : ")
        while one != "가위" and one != "바위" and one != "보":
            one = input("* 가위 바위 보 중에 골라주세요 : ")
        two = input ("- 두번째 선택 (가위 바위 보) : ")
        while two != "가위" and two != "바위" and two != "보":
            two = input("* 가위 바위 보 중에 골라주세요 : ")

        comone = random.choice(["가위" , "바위" , "보"])
        comtwo = random.choice(["가위" , "바위" , "보"])

        print("\n[",yourname, "] :",one,two)
        print("[ 컴퓨터 ] :",comone,comtwo)

        answer = input("- 마지막 선택 : ")
        while answer != one and answer != two:
            answer = input("- 마지막 선택 (%s, %s중에 골라주세요) : "%(one, two))
        com = random.choice([comone,comtwo])

        print("\n[",yourname, "] :",answer)
        print("[ 컴퓨터 ] :",com)

        if (com == answer):
            print("- 결과 : 무승부")
            num+=1
        elif (com == "가위" and answer == "바위"):
            print("- 결과 : 승")
            num+=1
            winnum+=1
        elif (com == "바위" and answer == "보"):
            print("- 결과 : 승")
            num+=1
            winnum+=1
        elif (com == "보" and answer == "가위"):
            print("- 결과 : 승")
            num+=1
            winnum+=1
        else:
            print("- 결과 : 패")
            print("\n게임 종료. [%s]님 총 %d번 승리하셨습니다."%(yourname,winnum))
            break


def mukzzibba():    #묵찌빠 게임
    winnum=0
    a=0
    win=0
    while(win==0):
        print("\n묵찌빠 게임 %d ROUND를 시작합니다."%int(winnum+1))
        print("* 패배 시 게임이 종료됩니다.")
        mgb = ['묵','찌','빠']
        com = random.choice(mgb)
        you= input('\n묵 찌 빠 ! (묵 찌 빠 중에 선택해주세요): ')
        while you != "묵" and you != "찌" and you != "빠":
            you= input('묵 찌 빠 ! (묵 찌 빠 중에 선택해주세요): ')

        


        while (you == com):
            print()
            print('[',yourname,'] : ' +you)
            print('[ 컴퓨터 ] : '+com)
            print('- 결과 : 무승부')
            com = random.choice(mgb)
            
            you= input('묵 찌 빠 ! (묵 찌 빠 중에 선택해주세요): ')
            while you != "묵" and you != "찌" and you != "빠":
                you= input('묵 찌 빠 ! (묵 찌 빠 중에 선택해주세요): ')

            print('묵 찌 빠 !')

        if you == '묵':
            if com == '찌':
                a = 1
            elif com == '빠':
                a = 2

        elif you == '찌':
            if com == '빠':
                a = 1
            elif com == '묵':
                a = 2

        elif you == '빠':
            if com == '묵':
                a = 1
            elif com == '찌':
                a = 2
     
        while a < 5:
            print()
            if a == 2: # 컴퓨터가 이긴 상황
                print('[',yourname,'] : ' +you)
                print('[ 컴퓨터 ] : '+com)
                print('컴퓨터의 공격')
                
                you= input('묵 찌 빠 ! (묵 찌 빠 중에 선택해주세요): ')
                while you != "묵" and you != "찌" and you != "빠":
                    you= input('묵 찌 빠 ! (묵 찌 빠 중에 선택해주세요): ')

                com = random.choice(mgb)
            
                if you == '묵':
                    if com=='찌':
                        a=1
                    elif com=='빠':
                        a=2
                    elif com=='묵':
                        a=3

                elif you == '찌':
                    if com=='빠':
                        a=1
                    elif com=='묵':
                        a=2
                    elif com=='찌':
                        a=3

                elif you == '빠':
                    if com=='묵':
                        a=1
                    elif com=='찌':
                        a=2
                    elif com=='빠':
                        a=3

            elif a==1: # 내가 이긴 상황
                print('[',yourname,'] : ' +you)
                print('[ 컴퓨터 ] : '+com)
                print('당신의 공격')

                
                you= input('묵 찌 빠 ! (묵 찌 빠 중에 선택해주세요): ')
                while you != "묵" and you != "찌" and you != "빠":
                    you= input('묵 찌 빠 ! (묵 찌 빠 중에 선택해주세요): ')


                com = random.choice(mgb)

                if you == '묵':
                    if com=='찌':
                        a=1
                    elif com=='빠':
                       a=2
                    elif com=='묵':
                        a=4

                elif you == '찌':
                    if com=='빠':
                        a=1
                    elif com=='묵':
                        a=2
                    elif com=='찌':
                        a=4

                elif you == '빠':
                    if com=='묵':
                        a=1
                    elif com=='찌':
                        a=2
                    elif com=='빠':
                        a=4
                        
            elif a==3: # 내가 진 상황에서 똑같은 걸 냈을 때
                print('[',yourname,'] : ' +you)
                print('[ 컴퓨터 ] : '+com)
                print('- 결과 : 패')
                print("\n게임 종료. [%s]님 총 %d번 승리하셨습니다."%(yourname,winnum))
                win=1
                break

            elif a==4: # 내가 이긴 상황에서 똑같은 걸 냈을 때
                print('[',yourname,'] : ' +you)
                print('[ 컴퓨터 ] : '+com)
                print('- 결과 : 승')
                winnum+=1
                break
                
        if win==1:
            break

if choice == "가위바위보":
    gbb()

elif choice == "하나빼기":
    hanabbagi()

elif choice == "묵찌빠":
    mukzzibba()
