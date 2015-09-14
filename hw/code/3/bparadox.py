from random import randint

def has_duplicates(list):
    list2 = list[:]
    list2.sort()
    for i in range(len(list2) - 1):
        if list2[i] == list2[i + 1]:
            return True
    return False
    


def create_birthday_list():
    birthday_list = []
    for i in range(23):
        month = randint(1, 12)
        day = randint(1, 31)
        birthday_list.append(str(month) + str(day))
    return birthday_list
        
print has_duplicates(create_birthday_list())