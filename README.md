# RST Project for ICS3U
ICS3U Final Coding Project done during OSSD (Grade 12 Program)

---

## Code Description
This game is called 7 Wonders of The World: A Text-based Quiz Game where the player will answer one question for each landmark and earn points. 

First of all, a welcome message is shown to the player and it will explain the game system. The link for players to refer is also given so that player can read it before they play the quiz. For each question, player will have 3 attempts to answer. Player will get 3 Marks, when answering correctly on first attempt, 2 Marks on second attempt and 1 Mark on third attempt. 

The country list will be sorted randomly using the random.shuffle() module. Among the 3 questions and answers stored in each subprogram, a random question number is chosen using random.randint() module. For answer inputs, all answers are converted to lowercase and extra spacings are removed before they are been compared with the stored answered to remove case-sensitivity.

If the player runs out of all 3 attempts the player will give another chance where they can choose a country they want to answer and will get 2 attempts for each question. They will be given 2 Marks for correct answer on first attempt and 1 Mark for correct answer on second attempt. It is ensured that player does not choose the country that the questions are been correctly answered. 

The game will continue until the player has answered questions correctly for all 7 landmarks or when the player has typed in “N” or “n” when they are asked if they still want to answer.

---

## Fixed Error
At first, when the player typed in different cases, user’s input are not re-formatted leading crushes such as unable to find the item in arrays and showing that user’s answer is wrong even though it was correct. To fix this issue, I have used .lower() and .strip() modules to convert the input. And also when users type in country names, I used .lower() and .capitalize() modules to make the input capitalized.

For second chances, I couldn’t keep track of which landmarks are correctly answered and resulting player to answer the same question again and again. I have added a new variable named: complete_landmarks to keep track of correct landmarks. This allows player to avoid choosing the completed questions. Moreover, I forgot to reset the condition after each question making the program to not ask questions after the first correct answer is given. So, I added a line condition = False on Line 186. 

Additionally, when user has run out of attempt, the code only displays the total point making the game less interesting. I have now added a Thank you message and points player earned along with his/her name. Furthermore, the game was very crowded and as a line-based game, the appearance is very important. So, I have added a few white lines and dotted lines to separate game sections making it more absorbing. There are some more minor errors that were fixed during development but these are the major ones. 

---

## Future Improvements

I have noticed that player need to rerun the game if they want to replay the game or if they want to compete with their friends. To improve this, I want to ask whether player wants to continue another round or not and if they want to, the game will repeat and ask their names. If the name matches with the name on first round, the game will save as Round 1, Round 2, etc. If the name does not match, it will create a new 2D array and store the names and respective points. After player has decided to end the game, the game will display a score ranking. 

Moreover, I want to validate if input is empty and if so, I want to re-ask player for input so that they won’t waste one of their attempts. Empty inputs can be caused due to accidental-clicks. 

Last but not least, I want to expand the question bank and add multiple levels such as Easy, Medium and Hard for users so that the game will be catchier and interest more players
