# Question #01: Smallest number using a for loop
my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

smallest = my_list[0]
for num in my_list:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest)





# Question #02: Average using a for loop
total = 0
for num in my_list:
    total = total + num
average = total / len(my_list)
print("Sum:", total)
print("Average:", average)





# Question #03: Search student name
students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]

name = input("Enter a student name: ")
if name in students:
    print("Student Found")
else:
    print("Student Not Found")






# Question #04: Shopping list
shopping = []

for i in range(5):
    item = input("Enter shopping item " + str(i + 1) + ": ")
    shopping.append(item)

print("Your shopping list:", shopping)
