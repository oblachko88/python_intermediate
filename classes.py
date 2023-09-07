class Person:

  amount = 0

  def __init__(self, name, age, height): #Make a class
    self.name = name
    self.age = age
    self.height = height
    Person.amount += 1

  def __str__(self):
    return "Name: {}, Age: {}, Height {}".format(self.name, self.age, self.height)
    # return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

  def get_older(self, years):
    self.age += years
    return self.age

  def __del__(self): #Delete variable
    Person.amount -= 1

  def print():
    x = "hello world"
    return print(x)

class Worker: 
  
  def __init__ (self, name, age, height, salary):
    super(Worker, self).__init__(name, age, height)
    self.salary = salary

  def __str__(self):
    text = super(Worker, self).__str__()
    text += ", Salary {}".format(self.salary)
    return text

  def calc_yearly_salary(self):
    return self.salary * 12

worker1 = Worker("Henry", 25, 174, 3000)

print(worker1)
print(worker1.calc_yearly_salary())