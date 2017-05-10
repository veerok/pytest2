def fib(num):
    list = [1, 1]
    while True:
        current = list[len(list) - 1] + list[len(list) - 2]
        if current > num:
            return list;
        list.append(current)
        print(current)
