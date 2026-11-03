def insert_patient_data(name,age):
    print(name)
    print(age)
    print('inserted into database')

insert_patient_data('nitish','thirty')

def insert_patient_data(name:str,age:int):
    print(name)
    print(age)
    print('inserted into database')

insert_patient_data('nitish','thirty')


def insert_patient_data(name:str,age:int):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('inserted into database')
    else:
        raise TypeError('name should be string and age should be string')

insert_patient_data('nitish','thirty')
# kya yeh scalable hai ? => nahi