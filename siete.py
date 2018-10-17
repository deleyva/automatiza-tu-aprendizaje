largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)        
        if largest == None or num > largest:
            largest = int(num)
        if smallest == None or num < smallest:
            smallest = int(num)
    except ValueError:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)