###########################################################
##################        Class          ##################
###########################################################

#python中的类（class）应该理解为用于传递参数的一个用户自己定义的模块
#class中包含数据与函数
#将参数传递给class之后，即可应用class包含的函数进行操作

def __init__(self)：
#class总是开始于init，且init至少有一个参数，也就是self
#self传递进去表示函数自身已被建立
#init可以理解为“开始”

#self.name等code可以理解为为class传递新的参数

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
    
hippo = Animal('ppx',32)

hippo.description()
#class中创建函数及使用函数

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive
#class中有全局变量和局部变量的区别

hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print hippo.is_alive
hippo.is_alive = False
print hippo.is_alive
print cat.is_alive
#全局变量和局部变量可随时个性化更改

class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
#class可“继承”其它class

class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!
###
#inheritance可以在父子和子父之间相互进行

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self,hours):
    self.hours = hours
    return 12 * hours
  def full_time_wage(self,hours):
    return super(PartTimeEmployee,self).calculate_wage(hours)

  
milton =  PartTimeEmployee('Milton')
print milton.full_time_wage(10)
#通过super函数能够使class实现自身调用。注意传递的参数

############################################
############   Class 综合举例   ############
############################################
class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  
  def check_angles(self):
    s = self.angle1+self.angle2+self.angle3
    if s == 180:
      return True
    else:
      return False

my_triangle = Triangle(90,30,60)

print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle


#############################################
############   Class 综合举例2   ############
#############################################


class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  def display_car(self):
    return "This is a %s %s with %s MPG" %(self.color,self.model,self.mpg)
  def drive_car(self):
    self.condition = "used"
    return self.condition
  
class ElectricCar(Car):
  def __init__(self,battery_type):
    self.battery_type = battery_type
  
  def drive_car(self):
    self.condition = 'like new'
    return self.condition
  
my_car = ElectricCar( "battery type" )

print my_car.condition
print my_car.drive_car()
print my_car.condition

#############################################
############   Class 综合举例3   ############
#############################################

class Point3D(object):
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
  
my_point = Point3D(1,2,3)

print my_point
#repr可以直接返回想要的数据表达方式，而无需在print后面去表达