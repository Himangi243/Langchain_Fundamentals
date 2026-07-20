from pydantic import BaseModel , EmailStr, Field
from typing import Optional
class Student(BaseModel):

    name:str
    age:Optional[int]=None
    email:EmailStr
    cgpa:float =Field(gt=0,lt=10,default=6,description='a decimal value the cgpa of the student')

new_student={'name':'nitish' ,'age':'32','email':'eabs@gmail.com','cgpa':5}
student=Student(**new_student)
print(student)
print(type(student))
# here we can validate our data if name is of  datatype otherthan str it will throw error

student_dict=dict(student)
print(student_dict['age'])
student_json=student.model_dump_json()