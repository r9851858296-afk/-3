class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def rate_lecture(self, lecture, course, grade):
        if not isinstance(lecture, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress:
            return 'Ошибка'
        if course not in lecture.courses_attached:
            return 'Ошибка'
        if not isinstance(grade, (int, float)) or not (1 <= grade <= 10):
            return 'Ошибка'

        if course in lecture.grades:
            lecture.grades[course] += [grade]
        else:
            lecture.grades[course] = [grade]

    def average_s_grade(self):
            all_grades = []
            for grades_list in self.grades.values():
                all_grades.extend(grades_list)
            if not all_grades:
                return 0.0
            return sum(all_grades) / len(all_grades)

    def __str__(self):
        avg = self.average_s_grade()
        courses_str = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Курсов нет'
        finished_str = ', '.join(self.finished_courses) if self.finished_courses else 'Курсов нет'
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg:.1f}\n'
                f'Курсы в процессе изучения: {courses_str}\n'
                f'Завершенные курсы: {finished_str}')

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.average_s_grade() == other.average_s_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return False
        return self.average_s_grade() < other.average_s_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
            all_grades = []
            for grades_list in self.grades.values():
                all_grades.extend(grades_list)
            if not all_grades:
                return 0.0
            return sum(all_grades) / len(all_grades)


    def __str__(self):
        avg = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg:.1f}')

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

lecturer = Lecturer('Some', 'Buddy')
reviewer = Reviewer('Some', 'Buddy')
student = Student('Ruoy', 'Eman', 'М')


student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']
lecturer.courses_attached += ['Python', 'Git']
reviewer.courses_attached += ['Python', 'Git']


reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'Git', 10)
reviewer.rate_hw(student, 'Git', 9)



student.grades['Python'] = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
lecturer.grades = {'Python': [10, 10, 10, 10, 10, 10, 10, 10, 10, 9]}

some_reviewer = reviewer
some_lecturer = lecturer
some_student = student


print(some_reviewer)
print(some_lecturer)
print(some_student)
