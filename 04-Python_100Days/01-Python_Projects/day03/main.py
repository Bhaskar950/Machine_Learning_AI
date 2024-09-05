print('Welcome to the rollercoaster')

height = int(input('waht is your height in cm? '))


if height >= 120:
  print("you can ride the rollercoaster!")

  age = int(input("What is your age? Please enter "))
  if age < 12:
    print(f"Your age is {age}. So you need to pay 5rs ")
  elif age == 12 | age <= 18:
    print(f"your age is {age}. So you need to pay 7rs")
  elif age > 18:
    print(f"Your age is {age}. So you need to pay 20rs")

else:
  print("Sorry, you have to grow taller before you can ride.")