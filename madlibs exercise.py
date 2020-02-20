print("You woke up.")
hungry = input("Are you hungry?: ")

if hungry == "yes":
    print("Go eat breakfast")
else:
    print("Don't eat breakfast")

print("You left the house.")
cloudy = input("Is it cloudy?: ")

if cloudy == "yes":
    print("Bring an umbrella")
else:
    print("Bring a sunglasses")


print("You are at the restaurant.")
eat = input("What do you wanna eat?: ")

if eat == "meat":
    print("Go order a steak")
elif eat == "pasta":
    print("Go order spaghetti & meatballs")
else:
    print("Go order a salad")
