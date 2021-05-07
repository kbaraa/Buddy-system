import math

user_input = []
default_array = ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","|"]
count = 0
tik_count = 0
def list_splice(target, start, delete_count=None, *items):
    if delete_count == None:
        delete_count = len(target) - start

    total = start + delete_count
    removed = target[start:total]
    target[start:total] = items

    return removed

while user_input == [] or user_input[0] != 'q':
    val = input("How many blocks do you want to allocate/free? \n")
    user_input = val.split()

    if user_input[0] == 'a':
        x = int(user_input[1])
        print(x)

        if x > 64:
            break
        log = math.ceil((math.log(x)/math.log(2)))
        tick_amount = 6 - log
        total = 64
        has_tick = False
        for n in range(tick_amount):
            if default_array[math.ceil(total / 2)] != "|":
                list_splice(default_array, math.ceil(total/2), 0, '|')
                total = total / 2
                has_tick = True
        if not has_tick:
            for n in range(tick_amount):
                if default_array[total / 2 + 32] != "|":
                    list_splice(default_array, total / 2 + 32, 0, '|')
                    total = total / 2
                    has_tick = True

        amount_allocate = int(user_input[1])
        not_found = True
        while not_found:
            for n in range(amount_allocate):
                if default_array[n] == "|":
                    new_starting = n
                    continue
                not_found = True
                starting_allocate = n
                break
        range_taken = range(starting_allocate, starting_allocate + amount_allocate)
        for n in range_taken:
            default_array[n] = "#"
        for y in default_array:
            print(y, end='')

    print("\n")

    if user_input[0] == 'f':
        index = int(user_input[1])
        tik_count = 0
        for i in range(1, index):
            if default_array[i] == "|":
                tik_count = tik_count + 1
        while default_array[index + 1] != '#':
            default_array[index + tik_count] = "-"
            index = index + 1
        for y in default_array:
            print(y, end='')
        print("\n")
    if user_input[0] == 'q':
        break
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
