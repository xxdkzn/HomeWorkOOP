class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.surname, self.name) < (other.surname, other.name)

    def __le__(self, other):
        return (self.surname, self.name) <= (other.surname, other.name)

    def __gt__(self, other):
        return (self.surname, self.name) > (other.surname, other.name)

    def __ge__(self, other):
        return (self.surname, self.name) >= (other.surname, other.name)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}

    def rate_lecture(self, course, grade):
        if course in self.courses_attached:
            if course in self.lectures_grades:
                self.lectures_grades[course] += [grade]
            else:
                self.lectures_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.surname, self.name) < (other.surname, other.name)

    def __le__(self, other):
        return (self.surname, self.name) <= (other.surname, other.name)

    def __gt__(self, other):
        return (self.surname, self.name) > (other.surname, other.name)

    def __ge__(self, other):
        return (self.surname, self.name) >= (other.surname, other.name)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.surname, self.name) < (other.surname, other.name)

    def __le__(self, other):
        return (self.surname, self.name) <= (other.surname, other.name)

    def __gt__(self, other):
        return (self.surname, self.name) > (other.surname, other.name)

    def __ge__(self, other):
        return (self.surname, self.name) >= (other.surname, other.name)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        avg_grade = sum(sum(values) / len(values) for values in self.grades.values()) / len(self.grades) if self.grades else 0
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.rate_lecture(course, grade)
        else:
            return 'Ошибка'

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.surname, self.name) < (other.surname, other.name)

    def __le__(self, other):
        return (self.surname, self.name) <= (other.surname, other.name)

    def __gt__(self, other):
        return (self.surname, self.name) > (other.surname, other.name)

    def __ge__(self, other):
        return (self.surname, self.name) >= (other.surname, other.name)


def avg_grade_students(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course]) / len(student.grades[course])
            count += 1
    return total_grade / count if count > 0 else 0


def avg_grade_lecturers(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.lectures_grades:
            total_grade += sum(lecturer.lectures_grades[course]) / len(lecturer.lectures_grades[course])
            count += 1
    return total_grade / count if count > 0 else 0


# Creating instances of classes
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer1 = Lecturer('John', 'Doe')
cool_lecturer1.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Jane', 'Smith')
cool_lecturer2.courses_attached += ['Python']

cool_reviewer1 = Reviewer('Alice', 'Johnson')
cool_reviewer1.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Bob', 'Brown')
cool_reviewer2.courses_attached += ['Python']

# Rating homeworks and lectures
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(cool_lecturer1, 'Python', 9)
best_student.rate_lecturer(cool_lecturer2, 'Python', 10)

# Printing information
print(cool_reviewer1)
print(cool_reviewer2)
print(cool_lecturer1)
print(cool_lecturer2)
print(best_student)

# Comparing lecturers and students by average grades
if avg_grade_lecturers([cool_lecturer1, cool_lecturer2], 'Python') > avg_grade_students([best_student], 'Python'):
    print("Lecturers have higher average grades for the course Python")
else:
    print("Students have higher average grades for the course Python")