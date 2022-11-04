# CSC 111 Final Project -- Be A Chef!
This program is a memory game designed for people of all ages. The game will first show three recipes-- blueberry pie, apple pie, and pumpkin pie-- and ask the user to choose from one of the three. After selecting, the user needs to memorize the ingredients from the recipe and then choose the correct ingredients. The game includes three levels of difficulty: easy(blueberry), middle(apple), and hard(pumpkin).

# Required files for this project
  - main.py
  - graphics.py

# How to interact with this project
  - First, users will read a short paragraph about basic information of this game and what they can expect from the outcome.
  - Then, the program will ask you pick one of the three recipes (blueberry, apple, and pumpkin). By clicking on the recipe picture, users will only see the recipe they select. Users need to memorize the ingredients on the given recipe within 5 seconds. After 5 seconds, the recipe will disappear, and the first group of choices of ingredients will appear.
  - Based on the level of difficulty, users will see different numbers of groups in sequence. For blueberry pie, they will see three groups. For apple pie, they will see four groups. And for pumpkin pie, they will see five groups. Within each group, three ingredients will appear. Only one of them appeared on the recipe. Users need to click on the correct ingredient and move it to the plate shown in the window using keyboards. To change their choice of ingredient, they can tap "q" and click on the ingredient they want to choose. If they choose the correct ingredient and move it to the plate, ingredients of this group will disappear, and next group of ingredient will appear. After choosing all the ingredients appeared on the recipe, they will see the picture of a completed pie and win the game! However, if any one of the step is wrong (for example, they move the wrong ingredient to the plate), they will directly see a burned pie and told they fail.

# Why we choose not to write test.py
All of our functions and methods draw to the window, and none of them operate based on the console. Because of this, it will be too difficult to write test.py. We included our attempt to write a test based on our original code.