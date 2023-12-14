# # # create a variable
# # cheer = "UCB Fintech"

# # for letter in cheer:
# #     #print each letter with the cheer variable
# #     print("Give me a " + letter + "!")
# #     print(letter + "!")

# # # print exclamation to screen ("Woohoo!!!")
# # print("\nWhat does that spell?")
# # print(cheer + "\nWoohoo!!!" + " " + cheer + "!")

# # Define variables
# principal = 300000.00
# interest_rate = .10
# time_period = 5.0

# # Compute simple interest rate
# simple_interest = principal * interest_rate * time_period

# # Print the results
# print(f"Simple interest rate for your purchase is: {simple_interest}")

# Decalre variables
original_price = 1550.00
current_price = 1450.00

# calculate 
increase = current_price - original_price
# How to calculate increase
percent_increase = (increase / original_price) * 100
recommendation = "buy"
threshold_to_buy = 1.00
threshold_to_sell = 100.00

if percent_increase >= threshold_to_sell:
    recommendation = "sell"
elif percent_increase <= threshold_to_buy:
    recommendation = "buy"
elif percent_increase < threshold_to_sell and percent_increase > threshold_to_buy:
    recommendation = "hold"
else:
    print("not enough data to make a decision. need human input")
    
print("Recommendation " + recommendation)
print()

        
