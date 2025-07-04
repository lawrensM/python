#Loops Control Statements

fruits = ['apple', 'banana', 'cherry', 'date']

for fruit in fruits:
    if fruit == 'cherry':
        break  # Exit the loop when 'cherry' is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == 'cherry':
        continue # skip cherry and moves to the next iteration
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == 'cherry':
        pass # Placeholder, no action is needed for cherry
    print(fruit)