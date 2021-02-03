def sum_add_even():
    even = 0
    odd = 0

    for x in range(1, 101):
        mod = x % 2
        if mod == 0:
            even += x
        else:
            odd += x
    
    return even, odd


def output(even, odd):
    print(f"even_sum:{even}, odd_sum:{odd}")


even, odd = sum_add_even()
output(even, odd)
