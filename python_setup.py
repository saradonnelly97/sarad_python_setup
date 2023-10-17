#Homework Prompts 
#Prompt 1 
def hello():
    print("Hey you!")

hello()

#Prompt 2
def pack(x, y, z):
    return [x, y, z]

x = "Socks"
y = "Dress"
z = "Sunblock"
packing_list = pack(x, y, z)
print(packing_list)

#Prompt 3 
def eat_lunch(lunchbox):
    if not lunchbox:
        print("My lunchbox is empty :(")
    else:
        print("First I eat", lunchbox[0])
        for item in lunchbox[1:]:
            print ("Next I will eat", item)

lunchbox = ["celery", "oreos", "cheesestick", "crackers"]
eat_lunch(lunchbox)


#practice 1
#greeting = "Hello, World"

#print(greeting)

#practice 2
#number_list = range (10)

#print (number_list)

#practice 3
#for i in number_list: 
#    print(i)

#practice 4
#def print_name(firstname):
#    print(firstname)

#print_name("Sara")

#practice 5
#def print_name(firstname, lastname):
#    return firstname + " " + lastname

#print(print_name("Sara", "Donnelly"))

#practice 6
#def print_name(firstname, lastname):
#    return firstname + " " + lastname

#name = print_name("Sara", "Donnelly")
#print(name)

#continuing on the activity 2
#prompt 1
#def say_hello():
#    print("Hello World")

#say_hello()

#prompt 2
#x = 1 
#y = 2 
#def add_integers():
#    print(x + y)

#add_integers()

#prompt 3 
#def average(x, y):
#    return (x + y)/2

#x = 5
#y = 7
#print(average(x, y))

#prompt 4
#def name_format(first_name, last_name):
#    return f"{last_name}, {first_name}"

#prompt 5
#def graduation_list(first, last, year, student_id):
#    return [first, last, year, student_id]

#prompt 6
#def above_18(x):
#    return x > 18

#prompt 7
#def reverse(str):
#    print(str[::-1])

