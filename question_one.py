# A python function that returns the area of a circle
# i)
def calculate_area(radius):
    area = 3.14*radius**2
    return area
print(calculate_area(5))

# ii)
# function to calculate the sum of all natural numbers up to n
def sum_of_natural_numbers(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum_of_natural_numbers([1,2,3,4]))


# iii)
numbers =  [1,3,5,7,9]
# removing an item from a list
numbers.remove(5) 
# adding an item to the list
numbers.append(10)
print(numbers)

# iv)
numbers =[1,2,3,4,5,6,7,8,9,10]
even_numbers =[]
for x in numbers:
    if x%2 ==0:
        even_numbers.append(x)
print(even_numbers)
    



# v)
student_info = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A'
}
# updating the value age to 25
student_info['age']=25
# adding a new key and value to the dictionary
student_info['city']=  'New York'
print(student_info)

# vi)
original_dict = {
    'a':3,
    'b':8,
    'c':2,
    'd':7
}
new_dict = []

for x in original_dict.values():
    if x > 5:
        new_dict.append(x)
        print(new_dict)
    else:
        pass
        