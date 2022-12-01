# Reindeer trackers
count = 1  
# Dictionary of Calories
calories_dict = {}
with open("input.txt","r") as file1: 
    calories = []
    for lines in file1:
        if lines != '\n' and lines != '':
            calories.append(int(lines))
        else: 
            calories_dict[str(count)] = sum(calories)
            calories = []
            count +=1

print("PART 1 ----- \n\tIndex : " + str(max(calories_dict,key=calories_dict.get)))
print("\tHighest: " + str(calories_dict[str(max(calories_dict,key=calories_dict.get))]))
#  -------- PART 2 ------------- #  
top3  = []
for i in range(3): 
    max_key = max(calories_dict,key=calories_dict.get)
    top3.append(calories_dict[str(max_key)])
    del calories_dict[str(max_key)]

print("\nPART 2 -------\n\tTop 3 : ", top3)
print("\tSum: " + str(sum(top3)))
