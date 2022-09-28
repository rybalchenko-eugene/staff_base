
from gettext import find
import input_data as inp

import out_data as output



def imporf_from_file(dic):

    with open('dir1.csv','r', encoding='utf-8') as d:
        for line in d:
            dic.append(line)



def click_button(dic):
    while True:
        i = inp.show_menu()
        if i == 1:
            output.print_dir(dic, inp.find_ID())
        elif i == 2:
            role = inp.find_role()
            for i in range(len(dic)):
                if role in dic[i]: 
                    output.print_dir(dic,i)
        elif i == 3:
            low_salary  = int(input("Для выборки по дапазону з/п введите нижнюю границу диапазона з/п: "))
            upper_salary = int(input("Введите верхнюю границу диапазона з/п: "))
            for i in range(len(dic)):
                salary = int(''.join(x for x in dic[i][-10:] if x.isdigit()))
                if low_salary <= salary <= upper_salary: output.print_dir(dic,i)
        elif i == 4:
            new_data = str(len(dic)) + ';' + input('Введите Фамилию Имя;Должность;Зарплату через ;')
            dic.append(new_data)
            output.print_dir(dic,len(dic)-1)
        elif i == 5:
            index = inp.find_ID()
            dic.pop(index)
        elif i == 6:
            index = inp.find_ID()
            new_data = str(index) + ';' + input('Введите обновленные данные - Фамилию Имя;Должность;Зарплату через ;') + '\n'
            dic[index] = new_data
        elif i == 7:
            output.print_dir(dic)
        elif i == 8:
            output.save_as_excel(dic)
        elif i == 9: 
            break