# working with strings
# phrase = "Giraffe Academy"
# print(phrase.lower())
# print(phrase.isupper())
# print(phrase.upper().isupper())
# print("Giraffe\nAcademy")  # different line
# print("Giraffe\"Academy")  # showing " mark  \ escape

# print(len(phrase))
# print(phrase[0])
# print(phrase[3])
# print(phrase.index("G"))   # giving index number
# print(phrase.index("Acad"))
# print(phrase.replace("Giraffe", "Elephant"))  # replace different string

# working with number
# print(2)
# print(-2.0987)
# print(3+4)
# print(3*4+5)
# print(10 % 3)  # remainder

# from math import *
# my_num = 5
# print(my_num)
# print(str(my_num) + "my favorite number")

# num = -5
# print(abs(my_num))
# print(round(3.2))
# print(round(3.7))


# my_num = -5
# print(ceil(3.7))  # 올림
# print(sqrt(36))

# # Get input the user
# name = input("Enter your name:")
# age = input("Enter your age:")
# print("Hello " + name + "! you are " + age)


# tuple  data structer
# coordinates = (4, 5)
# print(coordinates[1])

# # function


# def sayhi(name, age):  # return 이 없는 경우
#     # 왜 str 을 써야 하나 ?  age, 그냥 으로 하면 안나옴   TypeError: can only concatenate str (not "int") to str
#     # 같은 타입을 print 에 넣지 않을 경우는 무조건 ,   + 싸인은 먹히지 않음
#     print("Hello " + name, age)


# print("Top")
# sayhi("Mike", 35)
# print("Down")

# # Return Statement


# def cube(num):  # return 이 없으면 그냥 함수만 일 하고 끝남
#     return num*num*num


# result = cube(4)
# print(result)


# if statement


# is_male = False
# is_tall = False

# if is_male and is_tall:
#     print("you are a tall male")

# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")

# else:
#     print("you are not a male and not tall")

# if Statemnet & comparisons


# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3


# print(max_num(3, 40, 5))

# # Dictionary

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March"
# }

# # The way of getting a value from the dictionary form
# print(monthConversions["Jan"])
# print(monthConversions.get("Feb"))


# print(3, " hello ")  # different type should be connected to ,  not +

# while loop
i = 1

while condition  #
