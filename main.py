# Random module used
import random

# Display welcome message and rules to the users
print ("""Welcome from 7 Wonders of the World Game!
--------------------------------------------------------
Here's the rules:
1. You will hop onto each landmarks and answer questions related to them.
2. You will have 3 attempts for each question where you will given 3 points for correct answer on first attempt, 2 points on second attempt and 1 point on third attempt.
3. Your points will be display after you have completed the game or when you lost.

Take note that spelling error is not allowed
--------------------------------------------------------
Read through this link to help you with quiz:
https://www.britannica.com/list/new-seven-wonders-of-the-world
""")

# Initialise variables
seven_wonders = ["China", "Mexico", "Jordan", "Peru", "Brazil", "Italy", "India"]
game_condition = True
total_points = 0
country_count = 0
complete_landmarks = []
name = ""

random.shuffle(seven_wonders) # Shuffle the list of landmarks

# Subprogram of China that store questions, answers and display welcome message
def china():
    china_questions = ["How long is the Great World of China(in km): ",
                      "How long is the Great World of China in Chinese Study(in km): ",
                      "How does scholar note the Great World of China as: "
                      ]
    china_answers = ["8850","21200","political propaganda"]
    print ("Welcome from The Great World of China")
    return china_questions,china_answers

# Subprogram of Mexico that store questions, answers and display welcome message
def mexico():
    mexico_questions = ["How tall is the pyramid above Main Plaza? (in m): ",
                      "How many steps are there in structure?: ",
                      "What is the shape of stone at the base?: "
                      ]
    mexico_answers = ["24","365","snake head"]
    print ("Welcome from Chichén Itzá in Mexico")
    return mexico_questions,mexico_answers

# Subprogram of Jordan that store questions, answers and display welcome message
def jordan():
    jordan_questions = ["Which kind of mountains Petra is in?: ",
                      "How many population Petra is predicted to have?: ",
                      "When was Petra discovered?: "
                      ]
    jordan_answers = ["sandstone","30000","1912"]
    print("Welcome from Petra in Jordan")
    return jordan_questions,jordan_answers

# Subprogram of Peru that store questions, answers and display welcome message
def peru():
    peru_questions = ["When was Machu Picchu discovered?: ",
                      "How does Bingham believed Machu Picchu is for?: ",
                      "Where is Machu Picchu located?: "
                      ]
    peru_answers = ["1911","virgins of the sun","andes mountains"]
    print("Welcome from Machu Picchu in Peru")
    return peru_questions,peru_answers
    
# Subprogram of Brazil that store questions, answers and display welcome message
def brazil():
    brazil_questions = ["Where is Christ the Redeemer is located?: ",
                      "When did the construction of Christ the Redeemer start?: ",
                      "How tall is Christ the Redeemer? (in m): "
                      ]
    brazil_answers = ["rio de janerio","1926","30"]
    print("Welcome from Christ the Redeemer in Brazil")
    return brazil_questions,brazil_answers
    
# Subprogram of Italy that store questions, answers and display welcome message
def italy():
    italy_questions = ["Whose order was to build the Colosseum?: ",
                      "Give the dimensions of the Colosseum (width m x length m): ",
                      "How many spectators the Colosseum is capable of?: "
                      ]
    italy_answers = ["emperor vespansian","189x156","50000"]
    print("Welcome from the Colosseum in Italy")
    return italy_questions,italy_answers

# Subprogram of India that store questions, answers and display welcome message
def india():
    india_questions = ["Who built the Taj Mahal?: ",
                      "How many years did it take to build Taj Mahal?: ",
                      "What is Taj Mahal made of?: "
                      ]
    india_answers = ["shah jahan","22","white marble"]
    print("Welcome from the Taj Mahal in India")
    return india_questions,india_answers

print("--------------------------------------------------------")
name = input("What is your name?: " ) # Ask user's name as input

# Loops the program until user explored all lankmarks or when the
# user runs out of moves
while country_count < 7 and game_condition == True:
    condition = False # Condition of answering the question correctly
    attempt = 1 # Number of attempt
    print("--------------------------------------------------------")
    # Check lankmark and run the corresponding subprogram
    if seven_wonders[country_count] == "China":
        questions, answers = china()
    elif seven_wonders[country_count] == "Mexico":
        questions, answers = mexico()
    elif seven_wonders[country_count] == "Jordan":
        questions, answers = jordan()
    elif seven_wonders[country_count] == "Peru":
        questions, answers = peru()
    elif seven_wonders[country_count] == "Brazil":
        questions, answers = brazil()
    elif seven_wonders[country_count] == "Italy":
        questions, answers = italy()
    elif seven_wonders[country_count] == "India":
        questions, answers = india()
    
    question_no = random.randint(0, 2) # Randomly select questions from three questions

    # Repeat while condition is false and all number of attempts is not used
    while condition != True and attempt <= 3:
        answer = input(questions[question_no]) # Ask user for answer as input
        answer = answer.lower().strip() # Convert answer to lowercase and removing extra spaces
        # Check if the answer is correct
        if answers[question_no] == answer:
            condition = True
            complete_landmarks.append(seven_wonders[country_count]) # Add completed lankmarks in list
            print("Congrats! You've gotten the correct answer!")
            print()
            # Give and display points based on number of attempt
            if attempt == 1:
                points = 3
            elif attempt == 2:
                points = 2
            elif attempt == 3:
                points = 1
            total_points += points # Increment total points
            print(f"You have gotten {points} points for {seven_wonders[country_count]}!")
        
        else:
            print(f"Oops... Try again! You have {3 - attempt} attempt(s) left.") 
            print()
        
        attempt += 1
    
    # Check if the user ran out of attempt and display appropiate message
    if condition == False:
        print("You have run out of attempt.")
        game_condition = False
    
    country_count += 1 # Increase country count

# Giving additional chance if all attempts are been used   
if game_condition == False:
    print("--------------------------------------------------------")
    print("I know it's not ideal to leave when attempt run out")
    print("I will give you one more chance but you will have 2 attempts for each question")
    play = input("Do you still want to continue? (Y or N): ")
    play = play.lower()
    
    # Continue the game if user wish to.
    while play == "y":
        country = input("Which country do you want to answer?: ")
        country = country.lower().capitalize()
        
        # Ensure the choice user made is not repeated
        while country in complete_landmarks or country not in seven_wonders: 
            if country in complete_landmarks:
                print ("You have to choose country that has not been chosen")
            else: 
                print ("Your choice is not in the list")
            print ("Please select one from below:")
            for landmark in seven_wonders:
                if landmark not in complete_landmarks:
                    print (landmark)
            print("--------------------------------------------------------")
            country = input("Which country do you want to answer?: ")
            country = country.lower().capitalize()
   
        attempt = 1
        condition = False
        print("--------------------------------------------------------")
        
        # Call appropiate subprogram
        if country == "China":
            questions, answers = china()
        elif country == "Mexico":
            questions, answers = mexico()
        elif country == "Jordan":
            questions, answers = jordan()
        elif country == "Peru":
            questions, answers = peru()
        elif country == "Brazil":
            questions, answers = brazil()
        elif country == "Italy":
            questions, answers = italy()
        elif country == "India":
            questions, answers = india()
        
        question_no = random.randint(0, 2) # Randomly select questions from three questions

        # Repeat until the answer is correct or when all attempt has been used up
        while condition != True and attempt <= 2:
            answer = input(questions[question_no]) # Ask user for answer as input
            answer = answer.lower().strip() # Convert answer to lowercase and removing extra spaces
            # Check if the answer is correct
            if answers[question_no] == answer:
                condition = True
                complete_landmarks.append(country) # Add completed lankmarks in list
                print("Congrats! You've gotten the correct answer!")
                print()
                # Give and display points based on number of attempt
                if attempt == 1:
                    points = 2
                elif attempt == 2:
                    points = 1
                total_points += points # Increment total points
                print(f"You have gotten {points} points for {country}!")
            
            # Display a message if the answer is incorrect
            else:
                print(f"Oops... Try again! You have {2 - attempt} attempt(s) left.") 
                print()
        
            attempt += 1
            
        # Check if all landmarks have been answered
        if len(complete_landmarks) == 7:
            play = "n"
            
        # Ask user whether they want to continue if there are landmarks left
        else:
            play = input("Do you still want to continue? (Y or N): ")
            play = play.lower()

# Display total points and thank you message
print("--------------------------------------------------------")    
print(f"Thank you {name.strip()} for playing!")
print(f"Your total point is {total_points}")
print("--------------------------------------------------------")  
# Display landmarks user explored
print("You have discovered: ")
for each in complete_landmarks:
    print (each)
