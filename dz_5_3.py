from itertools import zip_longest

""" a list of tutors in which there are fewer tutors than classes"""

tutors_1 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

""" a list of tutors in which there are more tutors than classes"""

tutors_2 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Олег', 'Игорь', 'Павел'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

teach_class = zip_longest(tutors_1, klasses[:len(tutors_1)])

teach_class_2 = zip_longest(tutors_2, klasses[:len(tutors_2)])

print(type(teach_class))
print(*teach_class)

print(*teach_class_2)
