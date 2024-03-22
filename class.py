'''
Объектно Ориентированное Программирование
'''

'''
1) Создайте класс Book с атрибутами (свойствами) title author pages
добавьте метод info

'''
# class Book:
#     def __init__(self, title, author, pages) -> None:
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def info(self):
#         print(f'Название: {self.title} \nАвтор: {self.author} \nСтраницы: {self.pages}')
    
#     def size(self):
#         if self.pages > 300:
#             print('Книга большая')
#         else:
#             print('Кнгиа маленькая')
    
# book1 = Book('Грокаем алгоритмы', 'Адитья Бхаргава', 290)
# book1.info()
# book1.size()

'''
Создайте класс Student с атрибутами name, grades
добавьте методы для установки и получения оценки студента
'''
# class Student:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.grade = None
    
#     def set_grade(self, grade):
#         self.grade = grade
    
#     def get_grade(self):
#         if self.grade is None:
#             print('Student doesn\'t have any grades')
#         else:
#             print(f'Student grade: {self.grade}')

    
# student1 = Student('Solomon')
# student1.set_grade(95)
# student1.get_grade()
'''

'''
class Teacher:
    def __init__(self, name, subject) -> None:
        self.name = name
        self.subject = subject

    def info(self):
        print(f'{self.name} Subject: {self.subject}')

class TeacherMath(Teacher):
    pass

class TeacherLang(Teacher):
    pass

teacher_math = TeacherMath(name='Zahar', subject='Math')
teacher_lang = TeacherLang(name='Gaido Van Rassum', subject='Python')

teacher_math.info()
teacher_lang.info()