#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇1

# Variabels to store string of prints
msg_1 = "Welcome to the tip calculator!"
msg_2 = "What was the total bill? $"
msg_3 = "What percentage tip would you like to give? 10, 12 or 15? "
msg_4 = "How many people to split the bill? "
msg_5 = "Each person should pay: $"

print(msg_1)
total_bill = float(input(msg_2))
percent = int(input(msg_3))
people = int(input(msg_4))

# Calculate the % and add to total amount
totalPercent = percent / 100
final = total_bill * (1 + totalPercent)
result = final / people
final_result = "{:.2f}".format(result)

print(msg_5 + str(final_result))