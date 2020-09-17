# PEP 8


# snake_case = 1
# CamelCase = 2
# camelCase = 3

# kebab-case = 2


some_str = "Hello world"  # str()
some_str2 = 'Hello world'

some_int = 1  # int()
some_float = 2.2142352345  # float()
some_bool = True  # boll()

ask_name = "Введите имя\n"
ask_age = "Введите возраст\n"
#
# name = input(ask_name)
#
# print("Привет", name, end='!!!!!', sep='-----')

# age = int(input(ask_age))   Запрещена пока, пользователь может совершить ошибки

# age = input(ask_age)
#
# if age.isdigit():
#    age = int(age)
 #   if age >= 18:
  #      print('Доступ к разделам ХХХ открыт')
   # elif age > 16:
    #    print('Доступ к боевикам')
    # else:
     #   print('Смотри мультики')
# else:
    # print('Введено не число')
    # print('Повторите ввод')
#
# print('Hello')
# print('World')

a = 1234561426
 # Если ввести temp = a, и поменять все а на temp, то мы сохраним переменную а
while tmp := a % 10 and a:
    # tmp = a % 10
    a //= 10  # Равно a = a // 10
    if tmp == 5:
        break  # Если Continue или нет Break, то print("Else") в конце, напечатается
    # a = a // 10
    print(tmp, a)
else:
    print("ELSE")
