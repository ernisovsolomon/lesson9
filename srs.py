'''
1) Написать программу которая находит самое длинное слово в тексте
'''


# def longest_word(text):
#     longest = ''
#     list = text.split()
#     for i in list:
#         if len(i) > len(longest):
#             longest = i
#         else:
#             pass
#     return longest

# text = 'Написать программу которая находит самое длинное слово в тексте'

# result = longest_word(text)
# print(result)

'''
2) Тест на знание таблицы умножения
'''
from random import randint
def start_test():
    grade = 0
    for i in range(1, 6):
        num1 = randint(2, 9)
        num2 = randint(2, 9)
        right_answer = num1 * num2
        answer = int(input(f'Сколько будет {num1} * {num2} = x: '))
        
        if answer == right_answer:
            grade += 1
            print('Ответ верный!')
        else:
            print(f'Неверно! Правильный ответ: {right_answer}')
    print(f'Вы ответили на {grade * 20}% вопросов')

start_test()