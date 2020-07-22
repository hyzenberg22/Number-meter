.. code:: ipython3

    
    
    b
    class It_student:
        sub=['data_structure','co','bio']
        teachers={'co':'malobika','bio':'miq_bou','data_structure':'Miq'}
        pass
    roy= It_student
    sis= It_student
    
    roy.name='shubhajit roy'
    roy.gender='male'
    roy.hight= 4.5
    
    sis.name='sristi chodhury'
    sis.gender='female'
    sis.hight= 4.2
    
    print(sis.teachers['bio'],sis.hight)
    print(sis.hight)
    
    


.. parsed-literal::

    miq_bou 4.2
    4.2
    

.. code:: ipython3

    #self and the init function in the class and object
    class It_dept:
        
        teachers={'co':'hod','bio':'miq bou','evs':'shafali'} # this is the class variable and only changed by class variable but can be acessed by the instance 
        def __init__(self,st_name,st_roll,st_number): #here the st_name is a argument , init is used as the constructer
            self.name=st_name #here the name is a instance variable 
            self.roll=st_roll
            self.number=st_number
            
        def printdetails(self):
            return f'The name is:-{self.name}, roll is:-{self.roll},number is {self.number}'
        
        def num_meter(self):
            if self.number >10:
                print('invalid input')
            elif self.number >=9:
                print('He/she is Topper')
            elif self.number >=8 and self.number <9:
                print('He/she is a normal student')
            elif self.number >=5 and self.number <8:
                print('Congratulation you are a Backbencher..!')
            else:
                print('you are in wrong place ')
                
            
    roy=It_dept('shubhajit Roy',45,9.27)
    sis=It_dept('sristi choudhory',28,9.10)
    
    print(roy.roll)
    print(roy.name)
    print(roy.printdetails())
    roy.num_meter()
    sis.num_meter()
    print(sis.__dict__['roll'])# __dict__ is a function that returns a dictionary of the objects details even you can use specific index of the dictonary
    print(roy.teachers['evs'])  
    It_dept.teachers['evs']='ud'# you can change a dict by this methode 
    
    print(It_dept.teachers)
    print(sis.teachers['evs'])
    


.. parsed-literal::

    45
    shubhajit Roy
    The name is:-shubhajit Roy, roll is:-45,number is 9.27
    He/she is Topper
    He/she is Topper
    28
    shafali
    {'co': 'hod', 'bio': 'miq bou', 'evs': 'ud'}
    ud
    


