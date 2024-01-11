# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

# Print out options
# for candy in candyList:
#     print(f'[{str[candyList.index(candy)]}]
          
for candy in candy_list:
    print(f'[{str(candy_list.index(candy))}] {candy}')