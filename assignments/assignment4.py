# Enter the price of the house
print("Enter the house price")
price = float(input())

# Enter the credit score
print("Enter the credit score")
creditScore = int(input())

# Enter the first name
first_name = input("Enter the first name")

# Enter the last name
last_name = input("Enter the last name")

# Full name
full_name = first_name + " " + last_name

# Enter the email
email = input("Enter the email")

# Enter phone number
phone = input("Enter the phone number")

# Enter mailing
mailing = input("Enter the mailing address")

# Enter the city
city = input("Enter the city")

# Enter the state
state = input("Enter the state")

# Enter zip code
zipcode = input("Enter the zipcode")

# loan qualification


if 780 <= creditScore <= 850:
    creditScoreStatement = "Excellent credit"
    # print("zero down payment")
    downPayment = 0.0 * price
    housePrice = price + downPayment
elif 740 <= creditScore <= 779:
    creditScoreStatement = "Very good"
    downPayment = 0.2 * price
    housePrice = price + downPayment
elif 720 <= creditScore <= 739:
    creditScoreStatement = "Above average"
    downPayment = 0.3 * price
    housePrice = price + downPayment
elif 680 <= creditScore <= 719:
    creditScoreStatement = "Average"
    downPayment = 0.6 * price
    housePrice = price + downPayment
elif 620 <= creditScore <= 579:
    creditScoreStatement = "Below average"
    downPayment = 0.18 * price
    housePrice = price + downPayment
elif 580 <= creditScore <= 619:
    creditScoreStatement = "Poor credit score"
    downPayment = 0.20 * price
    housePrice = price + downPayment
elif 520 <= creditScore <= 579:
    creditScoreStatement = "Poor credit score"
    downPayment = 0.23 * price
    housePrice = price + downPayment
elif creditScore < 520:
    creditScoreStatement = "Poor credit score"
    downPayment = 0.25 * price
    housePrice = price + downPayment
else:
    print("invalid credit rating")
    creditScoreStatement = "N/A"
    downPayment = 0
    housePrice = 0

# OUTPUT
print("OUTPUT\n")
print("First Name: " + full_name )
print("Physical Address: " + mailing)
print("City: " + city + " " + " State: " + state + " " + " Zipcode: " + zipcode + "\n")
print("New House Price: " + str(housePrice) )
print("DownPayment: " + str(downPayment) )
print("CreditScore: " + str(creditScore) )
print("credit Status: " + creditScoreStatement )
