#This is the Number_meter

class It_dept:
    teachers = {'co': 'hod', 'bio': 'miq bou', 'evs': 'shafali'}

    def __init__(self, st_name, st_roll, st_number):
        self.name = st_name
        self.roll = int(st_roll)
        self.number =float(st_number)

    def num_meter(self):
        if self.number > 10:
            print('invalid input')
        elif self.number >= 9:
            print('He/she is Topper')
        elif self.number >= 8 and self.number < 9:
            print('He/she is a normal student')
        elif self.number >= 5 and self.number < 8:
            print('Congratulation you are a Backbencher..!')
        else:
            print('you are in wrong place ')

    def printdetails(self):
        return f'The name is:-{self.name}, roll is:-{self.roll},number is {self.number}'


student_name = input('Enter Student name:- ')
roll=int(input('Enter your roll no:- '))
cgpa=float(input('Enter your CGPA:-'))

student_name=It_dept(student_name,roll,cgpa)
student_name.num_meter()
print(student_name.printdetails())



