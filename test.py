# def say_hello(user_name, user_age):
#   print("hello", user_name)
#   print("I am", user_age, "years old.")
# say_hello("jeongwon", 26)

# print("\n\n")

# def say_hello(user_name="anonymous"):
#   print("hello", user_name)
# say_hello("hyewon")
# say_hello()
# print("\n\n")
# def plus(a=0,b=0):
#   print(a+b)
# def minus(a=0,b=0):
#   print(a-b)
# def multiple(a=0,b=0):
#   print(a*b)
# def divide(a=0,b=1):
#   print(a/b)
# def pow(a=0,b=0):
#   print(a**b)

# plus(4, 5)
# plus()
# minus(5, 3)
# minus()
# multiple(4, 2)
# multiple()
# divide(2, 4)
# divide()
# pow(6, 2)
# pow()

# print("\n\n")

# def tax_calc(money):
#   return money * 0.35
# def pay_tax(tax):
#   print("Th🧊ank you for paying", tax)

# to_pay = tax_calc(15000000)
# pay_tax(to_pay)

# print("\n\n")

# my_name = "hyewon"
# my_age = 26
# my_eye_color = "brown"

# print(f"Hello I'm {my_name}, I have {my_age} years in my earth, and {my_eye_color} is my eye color")

# print("\n\n")

# def make_juice(fruit):
#   return f"{fruit}+🥤"
# def add_ice(juice):
#   return f"{juice}+🧊"
# def add_suger(iced_juice):
#   return f"{iced_juice}+🍭"

# juice = make_juice("🍌")
# cold_juice = add_ice(juice)
# perfect_juice = add_suger(cold_juice)

# print(perfect_juice)

from random import randint
winner = 10

if winner > 10:
    print("Winner is greater than 10")
elif winner < 10:
    print("Winner is less than 10")
elif winner != 15:
    print("if")
else:
    print("Winner is 10")

print("\n\n")

age = int(input("How old are you?"))

if age < 18:
    print("You can't not drink.")
elif age <= 35 and age > 18:
    print("You dirnkk beer!")
elif age == 70 or age == 80:
    print("Birthday party!")
else:
    print("Go ahead!")

print("\n\n")

user_choice = int(input("Choose number."))
pc_choice = randint(1, 100)

if user_choice == pc_choice:
    print("You win!")

elif user_choice > pc_choice:
    print("Lower! computer choice", pc_choice)

elif user_choice < pc_choice:
    print("Higher! computer choice", pc_choice)

print("\n\n")
