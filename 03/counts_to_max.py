# print only odd numbers

def main():
    limit = input("숫자를 입력하세요. : ")
    limit = int(limit)

    for x in range(1, limit + 1, 2):
        print(x)


main()