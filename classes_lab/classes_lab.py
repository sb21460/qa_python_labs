

class Student:
    def __init__(self, name, age, student_class):
        self.name = name
        self.age = age
        self.student_class = student_class

    def get_student_average_score(self):
        test_score_1 = int(input("Please enter test score 1 : "))
        test_score_2 = int(input("Please enter test score 2 : "))
        test_score_3 = int(input("Please enter test score 3 : "))
        average_test_score = (test_score_1 + test_score_2 + test_score_3) / 3
        return average_test_score


student1 = Student("Sandhya", 40, "9MY")
print(f"Student {student1.name} in {student1.student_class} is {student1.age} years old "
      f"with an average score of {student1.get_student_average_score()}")

