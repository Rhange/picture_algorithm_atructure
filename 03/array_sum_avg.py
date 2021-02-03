def array_sum_avg():
    num_list = list()
    total = 0

    while True:
        number = input("숫자를 입력하세요. : ")

        if number == '':
            break

        number = int(number)
        num_list.append(number)
        total += number

    avg = total / len(num_list)
    print(f"total:{total}, avg:{avg}")
    return True

array_sum_avg()