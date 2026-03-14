print("Enter numbers to do addition. Enter 0 for the answer.")
adding = True
numbers = []
answer = 0
while adding == True:
 number = int(input("+ "))
 numbers.append(number)
 answer = sum(numbers)
 print("=", answer)
