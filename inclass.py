"""
The final results should have the following outputs
1. Numbers of days that of the total list of tips
2. Total of tips
3. Daily average
4. Least amout of tips I got (minimum)
    If my minimum is equal to 0, assign min to that amount
    Otherwise, elif my amount is less than my minimum, assign
    that minimum to my amount. 
5. Maximum of tips that I got
    if my amount is greater than the maximum
    maximum make it equal to the amount

I want that ouptut based on a cash_tips variable
"""

# List my cash_tips variable
cash_tips = [50, 100, 80, 90, 200, 120]

# Start my metrics variables
count = 0
total = 0
average = 0
minimum = 0
maximum = 0

# I want to see every tip on my list
for amount in cash_tips:
    # print(amount)
    #Calculate the cumulative sum of my tips

    # approach 1 to calculate total
    # total = total + amount
    
    # approach 2 to calculate total or cumulative sum (most common)
    total += amount
    count += 1
    # calculate the logic for minimum
    if minimum == 0:
        minimum = amount
    elif amount < minimum:
        minimum = amount

    # Logic for maximum
    if amount > maximum:
        maximum = amount
        
average = round(total / len(cash_tips),2)

print(total)
print(average)
print(minimum)
