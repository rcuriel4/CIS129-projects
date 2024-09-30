#CIS129_AnthonyCuriel_Lab5.py
#Date: 09/29/2024

#Lab 5 The Bottle Return Program

# Step 1: Declare variables below 
totalBottles = 0
todayBottles = 0
totalPayout = 0
counter = 1
keepGoing = 'y'
   	# Step 2: Loop to run program again
while keepGoing == 'y':
	  	# Step 3: Code to set value of variables
    totalBottles = 0
    todayBottles = 0
    counter = 0
      	# code to set value of variable totalBottles
    for counter in range(1, 8):
        todayBottles = int(input("Enter number of bottles returned for day #" + str(counter) + ': '))
        totalBottles = totalBottles + todayBottles
        counter = counter + 1
    else:
        keepGoing == 'n'
        break
      	# code to set value of variable totalPayout
PayoutPerBottle = 0.10
totalPayout = totalBottles * PayoutPerBottle
		# code to print the number of total bottles and total payout
print('The total number of bottles collected is: ', totalBottles)
print(f'The total paid out is ${totalPayout: .2f}')	
keepGoing = input("Do you want to enter another week's worth of data? (Enter y or n): ")
