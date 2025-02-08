def divide(numerator, denominator):
    print("divide function is called")
    return numerator/denominator

devisor = int(input("provide the devisor :"))

try:
    with open("/Users/dilanjt/Documents/tuition_practical/Python-basics/exceptions/file.txt", "r") as file:
        try:
            content = file.read()   
            print(content)
        except Exception:
            print("error in reading a file")

    result = divide(6, devisor)
    print("result is :", result)
except FileNotFoundError:
    print("Exception occured when trying to access file")
except ZeroDivisionError:
    print("Zero devision error")
except Exception:
    print("general exception")


print("this will execute")