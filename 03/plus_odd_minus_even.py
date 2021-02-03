def plus_minus_sum():
    print("홀수는 양수로 더하고 짝수는 음수로 더하는 프로그램")

    number = int(input("양의 정수를 입력하세요. : "))

    sum = 0
    flag = 0

    for i in range(1, number + 1):
        if flag == 1:
            sum -= i    # 짝수일 경우
            flag = 0
        else:
            sum += i    # 홀수일 경우
            flag = 1

    print(sum)
    return sum

result = plus_minus_sum()
print(result)