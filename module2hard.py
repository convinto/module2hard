def password(num):
    pass_numb = []
    for i in range(1, num):
        n = i + 1
        while n <= num:
            if num % (i + n) == 0:
                tuple_number = (i, n)
                pass_numb.append(tuple_number)
            n += 1
    return pass_numb


args = True
while args:
    number = int(input('Введите число (в пределах от 3 до 20) для получения пароля: '))
    if number in range(3, 21):
        args = False
    else:
        print('Введено число за допустимыми пределами интервала')
        print('Попробуйте еще раз')
print('Для числа', number, 'подходят пароли:', password(number))
