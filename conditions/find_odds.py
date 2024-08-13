# create a program where the user can enter a number and it outputs if it is odd or even

username = input("Enter your name :")
gender = input("Enter you sex :")

if gender == "male":
    username = "Mr. {}".format(username)
elif gender == "female":
    username = "Mrs. {}".format(username)


entered_number = int(input("Enter any number please:"))
remainder = entered_number % 2

if remainder != 0:
    print("Hey, {}".format(username))
    print("{} is an odd number".format(entered_number))
elif remainder == 0:
    print("Hey, {}".format(username))
    print("{} is an even number".format(entered_number))