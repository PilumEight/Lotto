import random
import sys

list_boch = []
for boch in range(0, 99):
    list_boch.append(boch)

list_card = []
list_of_won = random.sample(list_boch, 99)
list_of_random_items = random.sample(list_boch, 27)
list_of_random_itemsbot = random.sample(list_boch, 27)


def clutch(some_list):
    print(some_list[0:9], len(some_list[0:9]))
    print(some_list[9:18], len(some_list[9:18]))
    print(some_list[18:27], len(some_list[18:27]))


#print(clutch(list_of_random_items))
#print(clutch(list_of_random_itemsbot))


def proverka(a, b):
    counterA = 0
    counterB = 0
    for i in a:
        if i == 'X':
            counterA += 1
            if counterA == len(a):
                sys.exit("Player WIN")
        counterA = 0
    for i in b:
        if i == 'X':
            counterB += 1
            if counterB == len(b):
                sys.exit("Player bot WIN")


#print(list_of_won)


def cycly(won, list_a, list_b):
    for i in range(len(won)):
        proverka(list_a, list_b)
        try:
            for element in range(len(list_a)):
                if won[i] == list_a[element]:
                    if list_a[element] == int(input(list_a[element])):
                        list_a[element] = 'X'
                        print("LIST A:", clutch(list_a))
                    else:
                        print("Ты ввёл неверное число и проиграл")
                        sys.exit(0)
        except ValueError:
            print("Ты ввёл неверное значение и проиграл")
            sys.exit(0)
        for element_b in range(len(list_b)):
            if won[i] == list_b[element_b]:
                list_b[element_b] = 'X'
                print("LISTA B:",  clutch(list_b))
    return list_b


def main():
  print(cycly(list_of_won, list_of_random_items, list_of_random_itemsbot))


if __name__ == '__main__':
  main()