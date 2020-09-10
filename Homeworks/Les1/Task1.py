
ask_name = "Введите имя\n"

name = input(ask_name)
print('Привет,', name)

ask_surname = "Введите фамилию\n"

surname = input(ask_surname)
print("Чудесная фамилия,", surname)

ask_age = "Укажите ваш возраст\n"

age = input(ask_age)
print("Ваш возраст,", age)


print(f"Привет, {surname} {name}. Тебе {age}!")