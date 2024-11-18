# main module
def main():
# Declare input variables
	inputName = ""	
	inputType = ""	
	inputAge = 0	
 
 # class variable to hold a pet
	Animal = None
 
 # create a Pet object
	Animal = Pet()
 
 # Get values for a pet
	print('Enter a pet name: ')		
	inputName = input()			
	Animal.setName(inputName)
 
	print('Enter a pet type: ')	
	inputType = input()	
	Animal.setType(inputType)
 
	print('Enter a pet age: ')		
	inputAge = int(input())		
	Animal.setAge(inputAge)
 
	# Show values for this pet
	print(f'The pet name is {Animal.getName()}')	
	print(f'The pet type is {Animal.getType()}')	
	print(f'The pet age is {Animal.getAge()}')	
	

class Pet:
    # Fields
    # Constructor
    def Pet(self, n = "", t = "", a = 0):	# Public Module Pet(String n, String t, Integer a)
        self.name = n
        self.type = t
        self.age = a
  	
  	# Mutators
    def setName(self, n):	
        self.name = n
  	
    def setType(self, t):	
        self.type = t
 
    def setAge(self, a):	
        self.age = a
 
  	# Accessors
    def getName(self):	
        return self.name	
 
    def getType(self):	
        return self.type	
  	
    def getAge(self):	
        return self.age		


main()