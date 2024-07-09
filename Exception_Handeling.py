try:
    numerator = int(input("Enter The Number You Want To Divide: "))
    denumerator = int(input("Enter The Number Which Will Divide: "))
    result = (numerator / denumerator)

except ZeroDivisionError as e:
    print(e)
    print("Number Can't Be Divided by 0 !")

except ValueError:
    print("Please Enter Numbers Only !")

except Exception:
    print("Something Went Wrong !")

else:
    print(f"{numerator} Divided By {denumerator} is {result}")

finally:
    print("Tnank You !")