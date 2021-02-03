def sum_avg():
    num = 0
    sum = 0

    while True:
        try:
            a = input("숫자를 입력하세요: ")

            if a == '':
                break

            sum += int(a)
            num += 1
        except Exception:
            print("문자가 아닌 숫자를 입력하세요.")
            continue

    print(f"sum: {sum}")
    print(f"avg: {sum / num}")
    return

sum_avg()