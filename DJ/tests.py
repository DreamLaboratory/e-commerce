# class Person:
#     def __init__(self, name, surname, number):
#         self.name = name
#         self.surname = surname
#         self.number = number
#
#     def get_info(self):
#         return f"ism:{self.name}\n" \
#                f"familya:{self.surname}\n" \
#                f"number:{self.number}\n"
#
#
# class Student(Person):
#     UNDERGRADUATE, POSTGRADUATE = range(2)
#
#     def __init__(self, student_type, *args, **kwargs):
#         self.student_typ = student_type
#         self.classes = []
#         super(Student, self).__init__(*args, **kwargs)
#
#     def get_info(self, course):
#         return f"ism:{self.name}\n" \
#                f"familya:{self.surname}\n" \
#                f"number:{self.number}\n" \
#                f"kurs:{course}\n" \
#                f"turi:{self.student_typ}"
#
#
# class StaffMember(Person):
#     PERMANENT, TEMPORARY = range(2)
#
#     def __init__(self, employment_type, *args, **kwargs):
#         self.employment_type = employment_type
#         super(StaffMember, self).__init__(*args, **kwargs)
#
#     def get_info(self):
#         return f"ism:{self.name}\n" \
#                f"familya:{self.surname}\n" \
#                f"number:{self.number}\n" \
#                f"turi:{self.employment_type}\n"
#
#
# class Lecturer(StaffMember):
#     def __init__(self, *args, **kwargs):
#         self.course_taught = []
#         super(Lecturer, self).__init__(*args, **kwargs)
#
#     def assign_teaching(self, course):
#         self.course_taught.append(course)
#
#
# ###person
# person = Person('Jasurbek', 'Idrisov', 993853402)
# print(person.get_info())
#
# ####student
# student = Student(Student.UNDERGRADUATE, 'jasurbek', 'idrisov', 9935664738)
# print(student.get_info(3))
#
# ###person jobs
#
# staffMember = StaffMember(StaffMember.PERMANENT, 'jasurbek', 'idrisov', 9994377744)
# print(staffMember.get_info())


# class Person:
# 
#     def __init__(self, person_name, person_age):
#         self.name = person_name
#         self.age = person_age
# 
#     def get_name(self):
#         print(self.name)
# 
#     def get_age(self):
#         print(self.age)
# 
# 
# class Student(Person):
#     student_id = ''
# 
#     def __init__(self, student_name, student_age, student_id):
#         Person.__init__(self, student_name, student_age)
#         self.student_id = student_id
# 
#     def get_id(self):
#         return self.student_id
# 
# 
# person1 = Person("Jasur",22)
# person1.get_age()
# person1.get_name()
# 
# student1 = Student('fayzulloh',22,"236237")
# print(student1.get_id())
# student1.get_name()




# class A:
#     def __init__(self):
#         print('A sinfi initsializatiya bolmoqda')
#
#     def sub_method(self, b):
#         print('A sinfidan korsatilmoqda,', b)
#
#
# class B(A):
#     def __init__(self):
#         print('B sinfi initsializatisyalanmoqda......')
#         super().__init__()
#
#     def sub_method(self, b):
#         print('B sinfidan korstailmoqda:', b)
#         super().sub_method(b + 1)
#
#
# class C(B):
#     def __init__(self):
#         print('C sinfi initsializatsiyalanmoqda...')
#         super().__init__()
#
#     def sub_method(self, b):
#         print('C sinfidan ko`rsatilmoqda:', b)
#         super().sub_method(b + 1)
#
#
# if __name__ == '__main__':
#     c = C()
#     c.sub_method(3)




















