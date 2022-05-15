class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade_homework = 0

    def __str__(self):
        summa = 0
        number = 0
        for values in self.grades.values():
            summa += sum(values)
            number += len(values)
        if number != 0:
            self.average_grade_homework = round(summa / number, 2)

        res = f'Имя: {self.name} \nФамилия: {self.surname} \nПол: {self.gender} \nСредняя оценка за домашние задания: ' \
              f'{self.average_grade_homework} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} ' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)} \n'
        return res

    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            if self.average_grade_homework > other.average_grade_homework:
                res = f'У {self.name} {self.surname}балл выше\n'
            elif self.average_grade_homework == other.average_grade_homework:
                res = f'Средний балл у студентов одинаков\n'
            elif self.average_grade_homework < other.average_grade_homework:
                res = f'У {other.name} {other.surname} балл выше\n'
        else:
            return
        return res


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print(f'Ошибка выставления оценок лектору: {lecturer.name} {lecturer.surname} \n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.grade_for_lectures = 0

    def __str__(self):
        summa = 0
        number = 0
        for values in self.grades.values():
            summa += sum(values)
            number += len(values)
        if number !=0:
            self.grade_for_lectures = round(summa / number, 2)
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grade_for_lectures} \n'
        return res

    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            if self.grade_for_lectures > other.grade_for_lectures:
                res = f'У {self.name} {self.surname} балл выше\n'
            elif self.grade_for_lectures == other.grade_for_lectures:
                res = f'Средний балл у лекторов одинаков!\n'
            elif self.grade_for_lectures < other.grade_for_lectures:
                res = f'У {other.name} {other.surname} балл выше\n'
        else:
            return
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print(f'Ошибка выставления оценок студенту: {student.name} {student.surname}\n')

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \n'

def calculating_grade_students(students, course_students):
    summa = 0
    number = 0
    grade_students = 0
    for student in students:
        if course_students in student.grades.keys():
            summa += sum(student.grades[course_students])
            number += len(student.grades[course_students])
    if number != 0:
        grade_students = round(summa / number, 2)
    return print(f'Средняя оценка всех студентов по курсу {course_students} равна: {grade_students}\n')

def calculating_grade_lecturers(lecturers, course_lecturers):
    summa = 0
    number = 0
    grade_lecturers = 0
    for lecturer in lecturers:
        if course_lecturers in lecturer.grades.keys():
            summa += sum(lecturer.grades[course_lecturers])
            number += len(lecturer.grades[course_lecturers])
    if number != 0:
        grade_lecturers = round(summa / number, 2)
    return print(f'Средняя оценка всех лекторов по курсу {course_lecturers} равна: {grade_lecturers}\n')


# class Student
student_1 = Student('Ivan', 'Ivanov', 'man')
student_1.courses_in_progress += ['Python', 'Ada', 'Fortran']
student_1.finished_courses += ['Pascal']

student_2 = Student('Anna', 'Cvetkova', 'female')
student_2.courses_in_progress += ['Python', 'Ada', 'Pascal']
student_2.finished_courses += ['Fortran']

# class  Reviewer
print('----  Проверка срабатывания защиты от неправильного ввода  ----')
reviewer_1 = Reviewer('Vasily', 'Bistrov')
reviewer_1.courses_attached += ['Python', 'Ada']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2 = Reviewer('Alina', 'Kashina')
reviewer_2.courses_attached += ['Fortran', 'Pascal']
reviewer_2.rate_hw(student_2, 'Pascal', 10)
reviewer_2.rate_hw(student_2, 'Pascal', 9)
reviewer_2.rate_hw(student_2, 'Pascal', 10)

reviewer_1.rate_hw(student_1, 'Ada', 10)
reviewer_1.rate_hw(student_1, 'Ada', 8)
reviewer_1.rate_hw(student_1, 'Ada', 7)

reviewer_1.rate_hw(student_2, 'Ada', 10)
reviewer_1.rate_hw(student_2, 'Ada', 8)
reviewer_1.rate_hw(student_2, 'Ada', 9)
reviewer_2.rate_hw(student_2, 'Ada', 9)  # провоцируем ошибку

# Lecturer
lecturer_1 = Lecturer('Maxim', 'Perepelica')
lecturer_1.courses_attached.append("Fortran")
lecturer_1.courses_attached.append("Ada")

lecturer_2 = Lecturer('Pavel', 'Bolshov')
lecturer_2.courses_attached.append("Python")
lecturer_2.courses_attached.append("Pascal")
lecturer_2.courses_attached += ['Ada']

student_1.rate_lecture(lecturer_2, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Ada', 6)
student_1.rate_lecture(lecturer_1, 'Fortran', 8)
student_1.rate_lecture(lecturer_1, 'Fortran', 10)
student_1.rate_lecture(lecturer_1, 'Ada', 10)
student_1.rate_lecture(lecturer_2, 'Python', 8)
student_1.rate_lecture(lecturer_2, 'Ada', 10)
student_1.rate_lecture(lecturer_1, 'Fortran', 10)  # проверка срабатывания защиты

student_2.rate_lecture(lecturer_2, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Pascal', 9)
student_2.rate_lecture(lecturer_1, 'Fortran', 8)
student_2.rate_lecture(lecturer_1, 'Ada', 10)
student_2.rate_lecture(lecturer_2, 'Pascal', 8)
student_2.rate_lecture(lecturer_2, 'Ada', 10)


print('-----------  Reviewers:  ----------')
print(reviewer_1)
print(reviewer_2)

print('---------   Lecturers:  ---------')
print(lecturer_1)
print(lecturer_2)
print("Cравниваем лекторов: ", lecturer_1 < lecturer_2)

print('---------  Студенты:  ----------\n')
print(student_1)
print(student_2)
print('Сравниваем студентов: ', student_1 < student_2)

print('---------------- Считаем средние оценки ----------------')
students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]
course_students = 'Ada'
course_lecturers = 'Ada'
calculating_grade_students(students, course_students)
calculating_grade_lecturers(lecturers, course_lecturers)
course_students = 'Fortran'
course_lecturers = 'Fortran'
calculating_grade_students(students, course_students)
calculating_grade_lecturers(lecturers, course_lecturers)










