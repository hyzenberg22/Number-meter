class It_dept:
    teachers = {'co': 'hod', 'bio': 'miq bou', 'evs': 'shafali'}

    def __init__(self, st_name, st_roll, st_number):
        self.name = st_name
        self.roll = int(st_roll)
        self.cgpa =float(st_number)

    def num_meter(self):
        if self.cgpa > 10:
            print('invalid input')
        elif self.cgpa >= 9:
            print('He/she is Topper')
        elif self.cgpa >= 8 and self.cgpa < 9:
            print('He/she is a normal student')
        elif self.cgpa >= 5 and self.cgpa < 8:
            print('Congratulation you are a Backbencher..!')
        else:
            print('you are in wrong place ')

    def printdetails(self):
        return f'His/Her Name is:-{self.name}, roll is:-{self.roll}, CGPA is {self.cgpa}'


student_name = input('Enter Student name:- ')
roll=int(input('Enter your roll no:- '))
cgpa=float(input('Enter your CGPA:-'))

student_name=It_dept(student_name,roll,cgpa)
student_name.num_meter()
print(student_name.printdetails())
print(f'The teachers are :-{student_name.teachers}')