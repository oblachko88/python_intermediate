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

  def get_older(years):
    self.age += years

  def __del__(self): #Delete variable
    Person.amount -= 1

  def print():
    x = "hello world"
    return print(x)


person1 = Person("Mike", 30, 180)
print(person1)

person2 = Person("Sara", 25, 165)
print(person2)

person3 = Person("Alex", 35, 175)
print(person3)

print(Person.amount)