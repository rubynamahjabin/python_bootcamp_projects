#List Comprehension: creating new list from previous list

#Add 1 to each number in a list
numbers=[1,2,3]
new_list=[n+1 for n in numbers]
print(new_list)

#Double each number in a range of numbers
new_list=[n*2 for n in range(1,5)]
print(new_list)

#Making a new list for short names
names=["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
short_names=[name for name in names if len(name)<5]
print(short_names)

#Uppercasing all long names
names=["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
large_names=[name.upper() for name in names if len(name)>=5]
print(large_names)

#Squaring numbers in a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

#Filtering even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(item) for item in list_of_strings]
result = [num for num in numbers if num%2==0]
print(result)