## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	
	def __init__(self):
		self.alive = True
	
## Dog is-a class
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		self.name = name
		self.legs = 4
		
	def greet(self):
		print "Bark!"
	
## Cat is-a class
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name
		self.legs = 4
		
	def greet(self):
		print "Meow"
		
## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a a name
		self.name = name
		
		## Person has a pet
		self.pet = None
		self.legs = 2
		self.alive = True
		
	def greet(self):
		print "Hello"
		
## Employee is-a class
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		## Cannot be overridden?
		super(Employee, self).__init__(name)
		## Variables, attributes
		self.salary = salary
		
	def greet(self):
		print "I'm ready to work!"
		
## Fish is-a object
class Fish(object):
	
	def __init__(self):
		self.fins = True
	
	def greet(self):
		print "Glub, glub"
	
## Salmon is-a class
class Salmon(Fish):
	
	def __init__(self):
		self.type = "salmon"
	
## Halibut is-a class
class Halibut(Fish):
	
	def __init__(self):
		self.type = "halibut"
	
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary's pet property is satan
mary.pet = satan

## frank is-a Employee with a 120000 salary
frank = Employee("Frank", 120000)

## frank's pet property is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
		
rover.greet()

satan.greet()

mary.greet()

print mary.pet.name

frank.greet()

print frank.pet.name
print frank.legs

flipper.greet()

crouse.greet()

harry.greet()