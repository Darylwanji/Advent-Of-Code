my_hand = { 'X': 'ROCK' , 'Y': 'PAPER', 'Z':'SCISSORS'}
scores_1 = { 'X': 0 , 'Y': 3, 'Z': 6}
scores = { 'ROCK': 1 , 'PAPER': 2, 'SCISSORS': 3}
opps_hand = { 'A': 'ROCK' , 'B': 'PAPER', 'C':'SCISSORS'}

def checkWIn(oppsHand,myHand):
    if oppsHand == myHand:
        return 3
    if myHand == 'ROCK' and oppsHand == 'SCISSORS':
        return 6
    elif myHand == 'ROCK' and oppsHand == 'PAPER':
        return 0
    if myHand == 'PAPER' and oppsHand == 'ROCK':
            return 6
    elif myHand == 'PAPER' and oppsHand == 'SCISSORS':
        return 0
    if myHand == 'SCISSORS' and oppsHand == 'PAPER':
            return 6
    elif myHand == 'SCISSORS' and oppsHand == 'ROCK':
        return 0
# ---- PART 1
 
Total_score =0 
with open("input.txt","r") as file1: 
    for line in file1: 
        turn = line.strip().split(" ")
        turn_score = checkWIn(opps_hand[turn[0]],my_hand[turn[1]])
        Total_score += (turn_score+scores[my_hand[turn[1]]])
print("\nTotal Score P1 : " + str(Total_score))

def find_Hand(opps_hand,result):
    for key,value in my_hand.items():
        if checkWIn(opps_hand,value) == result:
            return value

# ---- PART 2
# Not Done
t_score = 0
with open("input.txt","r") as file2:
    for line in file2:
        turn = line.strip().split(" ")
        turn_score = checkWIn(opps_hand[turn[0]],
                    find_Hand(opps_hand[turn[0]],scores_1[turn[1]]))
        t_score += (turn_score + scores[my_hand[turn[1]]])
        
print("\nTotal Score P2 : " + str(t_score))
