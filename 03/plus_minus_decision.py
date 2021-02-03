def decision():
    print("종료하시려면 엔터만 누르세요.")

    while True:
        try:
            answer = input("정수를 입력하세요. : ")

            if answer == '':
                print("Bye Bye")
                return
            
            answer = int(answer)

            if answer > 0:
                print("양수")
            elif answer < 0:
                print("음수")
            else:
                print("제로")
        except ValueError:
            print("정수만 입력 가능합니다.")
            continue

decision()