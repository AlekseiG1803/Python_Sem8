import re

# Функция выбора действия
def User_Choice():
    menu = ["1-Весь справочник, 2-Поиск, 3-Внести номер, 4-Удалить, 5-Выход"]
    
    choice_num = int(input(f"Что хотите сделать? {menu} -> "))

    if choice_num == 1:
        Choice_Print_All()
    elif choice_num == 2:
        Choice_Search()
    elif choice_num == 3:
        Choice_Add()
    elif choice_num == 4:
        Choice_Dell()
    elif choice_num == 5:
        print("До свидания!")
        return
    else:
        print("Выбор некорректный")
        User_Choice()

# Функция показать весь справочник
def Choice_Print_All():
    print("Выводим справочник")

    data = open("tel.txt", "r")
    for line in data:
        print(re.sub("_", " ", line))

    User_Choice()

# Функция поиска
def Search():
    print("Запущен поиск")

    search = (input("Введите имя/номер телефона: -> ")).lower()

    data = open("tel.txt", "r")

    count_search = 0

    for line in data:
        temp = line.split()

        for i in range(len(temp)):
            temp[i] = re.sub("_", " ", temp[i])

        temp_lower = temp
        temp = tuple(temp)

        for i in range(len(temp_lower)):
            temp_lower[i] = temp_lower[i].lower()

        for el in temp_lower:
            if search in el:
                count_search += 1
                print(*temp)
                return list(temp)
    
    if count_search == 0:
        print("Ничего не найдено")


# Поиск при выборе Поиска из меню
def Choice_Search():
    Search()
    User_Choice()


# Функция добавить номер
def Choice_Add():
    print("Запущено добавление")

    name = re.sub(" ", "_", input("Введите имя контакта -> "))
    tel_num = re.sub(" ", "_", input("Введите номер телефона (можно несколько через пробел) -> "))

    new_record = f"{name} {tel_num}"

    data = open("tel.txt", "a")
    data.writelines(f"{new_record} \n")
    data.close()

    print(f"Добавлена запись: {new_record}")
    User_Choice()


# Функция удаления
def Choice_Dell():
    print("Запущено удаление")

    data = open("tel.txt", "r")

    temp_data = [line for line in data]
    for i in range(len(temp_data)):
        temp_data[i] = temp_data[i].split()

    res_search = Search()
    
    res_confirmation = int(input("Подтверждаете удаление найденных данных? 1 - да, 0 - нет -> "))
    if res_confirmation == 1:
        for i in range(len(res_search)):
            res_search[i] = re.sub(" ", "_", res_search[i])
        for j in range(len(temp_data)):
            if temp_data[j] == res_search:
                num = j
    
        res_data = [temp_data[i] for i in range(len(temp_data)) if i != num]

        data.close()

        with open("tel.txt", "w") as data:
            for el in res_data:
                data.writelines(" ".join(map(str, el)))
                data.writelines(" \n")

    User_Choice()

# asdf_a_asdf 345 
# Ivan_Comarov 89030000000 
# Bdfyjd_bdft 89034000000_89034000001 
# Fas_sdaf 9000000000 
# GGGGGG 00000 
# FFFF 343434343 
# TTTTTT 3223232323 


User_Choice()