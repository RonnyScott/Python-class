class Student:
    
    def __init__(self, name, regNo):
        self.name = name
        self.regNo = regNo
        
    def outPut(self):
        print(f"Name: {self.name}, Registration Number: {self.regNo}")
    
# Create instances of the Student class
student1 = Student("Ronny Scott", 4928)
student2 = Student("Benard Kimani", 8328)

# Call the outPut method for each student instance
student1.outPut()
student2.outPut()

# Define the ITStudent class which inherits from Student
class ITStudent(Student):
    def __init__(self, name, regNo, units, age):
        # Correct way to call the parent class's constructor
        super().__init__(name, regNo)
        self.units = units
        self.age = age
    
    # Override the outPut method
    def outPut(self):
        super().outPut()  # Call the parent class's outPut method
        print(f"Units taken: {self.units}, Student age: {self.age}")
   
# Create an instance of ITStudent and call the outPut method
student3 = ITStudent("Scott Omondi", 4159, 8, 22)
student3.outPut()
