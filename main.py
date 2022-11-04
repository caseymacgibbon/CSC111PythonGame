# ------------------------------------------------------
#        Name:  Casey and Silvia
#       Peers: N/A
#  References: https://docs.python.org/3/library/time.html
#  
# ------------------------------------------------------

#######################################################################
## Testing Area
test_mode = False
from graphics import *
from time import sleep

import os
def myTests(): 
 

  pass

## End of Testing Area
#######################################################################
  
#######################################################################


def wrongIngredient():
  """ Show the burned pie when user couldn't memorize the recipe.

  Called when the user inputs the wrong ingredient, shows a picture of a pie burning. 

  >>> wrongIngredient()
  A burned pie picture will show on the window.
  """ 
  
  burnt_pie= Image(Point(300,180),"img/burntpie.png")
  text = Text(Point(300,100), "Sorry, your pie burned!")
  text.setSize(24)
  text.setTextColor("#d94c21")
  burnt_pie.draw(win)
  text.draw(win)
  win.getMouse()
  win.close()

  pass

def pie_choice():
  """ Shows the recipe and allows the user to choose which recipe to follow.

  There are three kinds of recipes (blueberry, apple, pumpkin) that user can choose from. By clicking on the picture, user will see the specific ingreidents under each recipe.

  :return blueberry: (str): Return 'blueberry' to allow user see the recipe of blueberry.  
  :return apple: (str): Return 'apple' to allow user see the recipe of apple.  
  :return pumpkin: (str): Return 'pumpkin' to allow user see the recipe of pumpkin.  

  >>> pie_choice()
  blueberry
  """ 
  width = 300
  height = 200
  blueberry_image = Image(Point(width,height-20), "img/blueberrysign2.png")
  blueberry_image.draw(win)
  apple_image = Image(Point(width+150,height-20), "img/applesign.png")
  apple_image.draw(win)
  pumpkin_image = Image(Point(width-150,height-20), "img/pumpkinsign.png")
  pumpkin_image.draw(win)
  
  start_point = win.getMouse()
  while True:
    while 0 < start_point.getX() < 200:
      # User chooses pumpkin
      blueberry_image.undraw()
      apple_image.undraw()
      pumpkin_image.undraw()
      return "pumpkin"
    while 200 < start_point.getX() < 400 :
      # User chooses blueberry
      blueberry_image.undraw()
      apple_image.undraw()
      pumpkin_image.undraw()
      return "blueberry"
    while 400 < start_point.getX() < 600: 
      # User chooses pumpkin
      blueberry_image.undraw()
      apple_image.undraw()
      pumpkin_image.undraw()
      return "apple"
    
#clear the console after making a pie   
def cls():
  """ Clears the console when called."""
  os.system('cls' if os.name=='nt' else 'clear')
  
class Pie:
  """ Asks users to choose each ingredient from the recipe.

  Based on the recipe, users need to choose the correct ingredient from one of the three images that are given based on the recipe. Users need to click on the ingredient they want to choose and control it using arrow keys. They need to move the ingredient to the plate. If they want to change the ingredient, they can tap 'q' and click on another ingredient.

  Attributes:
  blueberries_ingredient (obj): Blueberries ingredient image
  apple_ingredient (obj): Apple ingredient image
  pumpkin_ingredient (obj): Pumpkin ingredient image
  deltaX (int): the length of movement in x-direction for each image
  deltaY (int): the length of movementin y-direction for each image
  """
  def __init__(self):
    text = Text(Point(300,50), """Use mouse to select and arrow keys to drag the correct 
  ingredient to the plate. If you click the wrong one, 
  press q to undo. Click to continue.""")
    text.setSize(13)
    text_draw(text)
    
    self.blueberries_ingredient = Image(Point(100,180),"img/blueberries.png")
    self.blueberries_ingredient.draw(win)
    
    self.apples_ingredient = Image(Point(500,180),"img/apple.png")
    self.apples_ingredient.draw(win)
  
    self.pumpkin_ingredient= Image(Point(300, 350), "img/pumpkindrawing.png")
    self.pumpkin_ingredient.draw(win)  
    self.deltaX = 30
    self.deltaY = 30
  
  def blueberry(self):
    """ Ask user to click and move the ingredient to the plate.
    
    The correct ingredient from a bowl of blueberries, an apple, or a pumpkin. If the user selects the blueberries and uses the arrow keys to drag it to the plate, the method will return True. If the user selects the wrong ingredient, the method will return False.
    
    :return: (bool): Return True if right ingredient, and False if wrong ingredient. 
    
    >>> pie_blueberry.blueberry():
    True
    >>> pie_blueberry.blueberry():
    False
    """

    while True:
      start_point = win.getMouse()
      #blueberries_ingredient (correct)
      while 50 < start_point.getX() < 200:
        key =  win.checkKey()
        centerx = self.blueberries_ingredient.getAnchor().getX()
        if key == 'Left':
          self.blueberries_ingredient.move(self.deltaX *(-1), 0)
        elif key == 'Right':
          self.blueberries_ingredient.move(self.deltaX, 0)
        elif key == "Up":
          self.blueberries_ingredient.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.blueberries_ingredient.move(0, self.deltaY)
        elif key == 'q':
          break

        if centerx > 250:
          self.blueberries_ingredient.undraw()
          self.apples_ingredient.undraw()
          self.pumpkin_ingredient.undraw()
          return True
  
      #apples_ingredient (wrong)
      while 500 < start_point.getX() < 600:
        key =  win.checkKey()
        centerx = self.apples_ingredient.getAnchor().getX()
        if key == 'Left':
          self.apples_ingredient.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.apples_ingredient.move(self.deltaX, 0)
        elif key == "Up":
         self. apples_ingredient.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.apples_ingredient.move(0, self.deltaY)
        elif key == 'q':
          break
        
        if centerx < 400:
          self.apples_ingredient.undraw()
          self.blueberries_ingredient.undraw()
          self.pumpkin_ingredient.undraw()
          return False
          
      #pumpkin ingredients (wrong)
      while 300 < start_point.getY() < 400:
        centery = self.pumpkin_ingredient.getAnchor().getY()
        key =  win.checkKey()
        if key == 'Left':
          self.pumpkin_ingredient.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.pumpkin_ingredient.move(self.deltaX, 0)
        elif key == "Up":
          self.pumpkin_ingredient.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.pumpkin_ingredient.move(0, self.deltaY)
        elif key == 'q':
          break
        
        if centery < 200:
          self.pumpkin_ingredient.undraw()
          self.blueberries_ingredient.undraw()
          self.apples_ingredient.undraw()
          return False
          
  def apple(self):
    """ Ask user to click and move the ingredient to the plate.
    
    The correct ingredient from a bowl of blueberries, an apple, or a pumpkin. If the user selects the apple and uses the arrow keys to drag it to the plate, the method will return True. If the user selects the wrong ingredient, the method will return False.
      
    :return: (bool): Return True if right ingredient, and False if wrong ingredient. 
      
    >>> pie_apple.apple():
    True
    >>> pie_apple.apple():
    False 
    """
    while True:
      start_point = win.getMouse()
      # blueberry (wrong)
      while 50 < start_point.getX() < 200:
        key =  win.checkKey()
        centerx = self.blueberries_ingredient.getAnchor().getX()
        if key == 'Left':
          self.blueberries_ingredient.move(self.deltaX *(-1), 0)
        elif key == 'Right':
          self.blueberries_ingredient.move(self.deltaX, 0)
        elif key == "Up":
          self.blueberries_ingredient.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.blueberries_ingredient.move(0, self.deltaY)
        elif key == 'q':
          break
        if centerx > 250:
          self.blueberries_ingredient.undraw()
          self.apples_ingredient.undraw()
          self.pumpkin_ingredient.undraw()
          return False
          
      #apple (correct)
      while 500 < start_point.getX() < 600:
        key =  win.checkKey()
        centerx = self.apples_ingredient.getAnchor().getX()
        if key == 'Left':
          self.apples_ingredient.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.apples_ingredient.move(self.deltaX, 0)
        elif key == "Up":
         self. apples_ingredient.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.apples_ingredient.move(0, self.deltaY)
        elif key == 'q':
          break
        if centerx < 400:
          self.apples_ingredient.undraw()
          self.blueberries_ingredient.undraw()
          self.pumpkin_ingredient.undraw()
          return True

      # pumpkin (wrong)
      while 300 < start_point.getY() < 400:
        centery = self.pumpkin_ingredient.getAnchor().getY()
        key =  win.checkKey()
        if key == 'Left':
          self.pumpkin_ingredient.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.pumpkin_ingredient.move(self.deltaX, 0)
        elif key == "Up":
          self.pumpkin_ingredient.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.pumpkin_ingredient.move(0, self.deltaY)
        elif key == 'q':
          break
        if centery < 200:
          # break
          # correct
          self.pumpkin_ingredient.undraw()
          self.blueberries_ingredient.undraw()
          self.apples_ingredient.undraw()
          return False
          # wrongIngredient()
    
  def pumpkin(self):
    """ Ask user to click and move the ingredient to the plate.
    
    The correct ingredient from a bowl of blueberries, an apple, or a pumpkin. If the user selects the pumpkin and uses the arrow keys to drag it to the plate, the method will return True. If the user selects the wrong ingredient, the method will return False.
      
    :return: (bool): Return True if right ingredient, and False if wrong ingredient. 
      
    >>> pie_pumpkin.pumpkin():
    True
    >>> pie_pumpkin.pumpkin():
    False 
    """
    while True:
      start_point = win.getMouse()
      #wrong
      while 50 < start_point.getX() < 200:
        key =  win.checkKey()
        centerx = self.blueberries_ingredient.getAnchor().getX()
        if key == 'Left':
          self.blueberries_ingredient.move(self.deltaX *(-1), 0)
        elif key == 'Right':
          self.blueberries_ingredient.move(self.deltaX, 0)
        elif key == "Up":
          self.blueberries_ingredient.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.blueberries_ingredient.move(0, self.deltaY)
        elif key == 'q':
          break
        if centerx > 250:
          self.blueberries_ingredient.undraw()
          self.apples_ingredient.undraw()
          self.pumpkin_ingredient.undraw()
          return False

      #wrong
      while 500 < start_point.getX() < 600:
        key =  win.checkKey()
        centerx = self.apples_ingredient.getAnchor().getX()
        if key == 'Left':
          self.apples_ingredient.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.apples_ingredient.move(self.deltaX, 0)
        elif key == "Up":
         self. apples_ingredient.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.apples_ingredient.move(0, self.deltaY)
        elif key == 'q':
          break
        if centerx < 400:
          self.apples_ingredient.undraw()
          self.blueberries_ingredient.undraw()
          self.pumpkin_ingredient.undraw()
          return False

      #correct
      while 300 < start_point.getY() < 400:
        centery = self.pumpkin_ingredient.getAnchor().getY()
        key =  win.checkKey()
        if key == 'Left':
          self.pumpkin_ingredient.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.pumpkin_ingredient.move(self.deltaX, 0)
        elif key == "Up":
          self.pumpkin_ingredient.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.pumpkin_ingredient.move(0, self.deltaY)
        elif key == 'q':
          break
        if centery < 200:
          self.pumpkin_ingredient.undraw()
          self.blueberries_ingredient.undraw()
          self.apples_ingredient.undraw()
          return True

  def sugar(self):
    """ Asks the user to move an ingredient to the plate.
    
    Prompts the user to choose between eggs, cinnamon, and sugar. If the user selects the sugar and uses the arrow keys to drag it to the plate, the method will return True. If the user selects the wrong ingredient, the method will return False.
    
    :return: (bool): Return True if right ingredient, and False if wrong ingredient. 
      
    >>> pie_pumpkin.sugar():
    True
    >>> pie_pumpkin.sugar():
    False 
    """
    
    self.eggs = Image(Point(300,350), "img/eggs.png")
    self.eggs.draw(win)
    self.cinnamon = Image(Point(100, 180), "img/cinnamon.png")
    self.cinnamon.draw(win)
    self.sugar_pot = Image(Point(500, 180), "img/sugar_pot.png")
    self.sugar_pot.draw(win)
  
    while True:
      start_point = win.getMouse()
      #wrong
      while 50 < start_point.getX() < 200:
        key =  win.checkKey()
        centerx = self.cinnamon.getAnchor().getX()
        if key == 'Left':
          self.cinnamon.move(self.deltaX *(-1), 0)
        elif key == 'Right':
          self.cinnamon.move(self.deltaX, 0)
        elif key == "Up":
          self.cinnamon.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.cinnamon.move(0, self.deltaY)
        elif key == 'q':
          break
        
        if centerx > 250:
          self.eggs.undraw()
          self.sugar_pot.undraw()
          self.cinnamon.undraw()
          return False

      #correct
      while 400 < start_point.getX() < 550:
        key =  win.checkKey()
        centerx = self.sugar_pot.getAnchor().getX()
        if key == 'Left':
          self.sugar_pot.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.sugar_pot.move(self.deltaX, 0)
        elif key == "Up":
         self.sugar_pot.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.sugar_pot.move(0, self.deltaY)
        elif key == 'q':
          break
        
        if centerx < 400:
          self.sugar_pot.undraw()
          self.cinnamon.undraw()
          self.eggs.undraw()
          return True

      #wrong
      while 300 < start_point.getY() < 400:
        centery = self.eggs.getAnchor().getY()
        key =  win.checkKey()
        if key == 'Left':
          self.eggs.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.eggs.move(self.deltaX, 0)
        elif key == "Up":
          self.eggs.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.eggs.move(0, self.deltaY)
        elif key == 'q':
          break
        
        if centery < 200:
          self.cinnamon.undraw()
          self.eggs.undraw()
          self.sugar_pot.undraw()
          return False

  def butter(self):
    """ Asks the user to move an ingredient to the plate.
    
    Prompts the user to choose between eggs, cinnamon, and butter. If the user selects the butter and uses the arrow keys to drag it to the plate, the method will return True. If the user selects the wrong ingredient, the method will return False.
    
    :return: (bool): Return True if right ingredient, and False if wrong ingredient. 
      
    >>> pie_pumpkin.butter():
    True
    >>> pie_pumpkin.butter():
    False 
    """
    
    self.butter = Image(Point(300,350), "img/butter.png")
    self.butter.draw(win)
    self.cinnamon = Image(Point(100, 180), "img/cinnamon.png")
    self.cinnamon.draw(win)
    self.eggs = Image(Point(500, 180), "img/eggs.png")
    self.eggs.draw(win)
  
    while True:
      start_point = win.getMouse()
      #wrong
      while 50 < start_point.getX() < 200:
        key =  win.checkKey()
        centerx = self.cinnamon.getAnchor().getX()
        if key == 'Left':
          self.cinnamon.move(self.deltaX *(-1), 0)
        elif key == 'Right':
          self.cinnamon.move(self.deltaX, 0)
        elif key == "Up":
          self.cinnamon.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.cinnamon.move(0, self.deltaY)
        elif key == 'q':
          break
        
        if centerx > 250:
          self.eggs.undraw()
          self.butter.undraw()
          self.cinnamon.undraw()
          return False

      #wrong
      while 400 < start_point.getX() < 550:
        key =  win.checkKey()
        centerx = self.eggs.getAnchor().getX()
        if key == 'Left':
          self.eggs.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.eggs.move(self.deltaX, 0)
        elif key == "Up":
         self.eggs.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.eggs.move(0, self.deltaY)
        elif key == 'q':
          break
        
        if centerx < 400:
          self.eggs.undraw()
          self.cinnamon.undraw()
          self.butter.undraw()
          return False

      #correct
      while 300 < start_point.getY() < 400:
        centery = self.butter.getAnchor().getY()
        key =  win.checkKey()
        if key == 'Left':
          self.butter.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.butter.move(self.deltaX, 0)
        elif key == "Up":
          self.butter.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.butter.move(0, self.deltaY)
        elif key == 'q':
          break

        if centery < 200:
          self.cinnamon.undraw()
          self.eggs.undraw()
          self.butter.undraw()
          return True
          
  def flour(self):
    """ Asks the user to move an ingredient to the plate.
    
    Prompts the user to choose between eggs, cinnamon, and flour. If the user selects the flour and uses the arrow keys to drag it to the plate, the method will return True. If the user selects the wrong ingredient, the method will return False.
    
    :return: (bool): Return True if right ingredient, and False if wrong ingredient. 
      
    >>> pie_pumpkin.flour():
    True
    >>> pie_pumpkin.flour():
    False 
    """
    
    self.cinnamon = Image(Point(300,350), "img/cinnamon.png")
    self.cinnamon.draw(win)
    self.flour = Image(Point(100, 180), "img/flour2.gif")
    self.flour.draw(win)
    self.eggs = Image(Point(500, 180), "img/eggs.png")
    self.eggs.draw(win)
  
    while True:
      start_point = win.getMouse()

      #correct
      while 50 < start_point.getX() < 200:
        key =  win.checkKey()
        centerx = self.flour.getAnchor().getX()
        if key == 'Left':
          self.flour.move(self.deltaX *(-1), 0)
        elif key == 'Right':
          self.flour.move(self.deltaX, 0)
        elif key == "Up":
          self.flour.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.flour.move(0, self.deltaY)
        elif key == 'q':
          break
        
        if centerx > 250:
          self.eggs.undraw()
          self.flour.undraw()
          self.cinnamon.undraw()
          return True

      #wrong
      while 400 < start_point.getX() < 550:
        key =  win.checkKey()
        centerx = self.eggs.getAnchor().getX()
        if key == 'Left':
          self.eggs.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.eggs.move(self.deltaX, 0)
        elif key == "Up":
         self.eggs.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.eggs.move(0, self.deltaY)
        elif key == 'q':
          break
        
        if centerx < 400:
          self.eggs.undraw()
          self.cinnamon.undraw()
          self.flour.undraw()
          return False

      #wrong
      while 300 < start_point.getY() < 400:
        centery = self.cinnamon.getAnchor().getY()
        key =  win.checkKey()
        if key == 'Left':
          self.cinnamon.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.cinnamon.move(self.deltaX, 0)
        elif key == "Up":
          self.cinnamon.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.cinnamon.move(0, self.deltaY)
        elif key == 'q':
          break

        if centery < 200:
          self.cinnamon.undraw()
          self.eggs.undraw()
          self.flour.undraw()
          return False

          
  def pieCrust(self):
    """ Asks the user to move an ingredient to the plate.
    
    Prompts the user to choose between eggs, pie crust, and butter. If the user selects the pie crust and uses the arrow keys to drag it to the plate, the method will return True. If the user selects the wrong ingredient, the method will return False.
    
    :return: (bool): Return True if right ingredient, and False if wrong ingredient. 
      
    >>> pie_pumpkin.pieCrust():
    True
    >>> pie_pumpkin.pieCrust():
    False 
    """
    
    self.eggs = Image(Point(100,180), "img/eggs.png")
    self.eggs.draw(win)
    self.butter = Image(Point(500, 180), "img/butter.png")
    self.butter.draw(win)
    self.pie_crust = Image(Point(300, 350), "img/piecrust.png")
    self.pie_crust.draw(win)

    
    while True:
      start_point = win.getMouse()
      #wrong
      while 50 < start_point.getX() < 200:
        key =  win.checkKey()
        centerx = self.eggs.getAnchor().getX()
        if key == 'Left':
          self.eggs.move(self.deltaX *(-1), 0)
        elif key == 'Right':
          self.eggs.move(self.deltaX, 0)
        elif key == "Up":
          self.eggs.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.eggs.move(0, self.deltaY)
        elif key == 'q':
          break
        if centerx > 250:
          self.eggs.undraw()
          self.butter.undraw()
          self.pie_crust.undraw()
          return False

      #wrong
      while 400 < start_point.getX() < 550:
        key =  win.checkKey()
        centerx = self.butter.getAnchor().getX()
        if key == 'Left':
          self.butter.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.butter.move(self.deltaX, 0)
        elif key == "Up":
         self.butter.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.butter.move(0, self.deltaY)
        elif key == 'q':
          break
        if centerx < 400:
          self.pie_crust.undraw()
          self.butter.undraw()
          self.eggs.undraw()
          return False

      #correct
      while 300 < start_point.getY() < 400:
        centery = self.pie_crust.getAnchor().getY()
        key =  win.checkKey()
        if key == 'Left':
          self.pie_crust.move(-1 * self.deltaX, 0)
        elif key == 'Right':
          self.pie_crust.move(self.deltaX, 0)
        elif key == "Up":
          self.pie_crust.move(0, -1 * self.deltaY)
        elif key == "Down":
          self.pie_crust.move(0, self.deltaY)
        elif key == 'q':
          break
        if centery < 200:
          self.eggs.undraw()
          self.butter.undraw()
          self.pie_crust.undraw()
          return True

def text_draw(text):
  """ Draws given text to the window in purple: used for the opening instructions.

  Inputs parameter 'text' and draws it to the window.
  
  :param text: (graphics.Text): A text graphic object with a given point and string.

  >>> text_draw(Text(Point(300,50), "Pie Chef Memory Game"))
  Pie Chef Memory Game
  """
  text.setTextColor("purple")
  text.draw(win)
  win.getMouse()
  text.undraw()
  
#Pie drawing canvas
win = GraphWin("Pie", 600, 400)
  
def main():
  #set the background
  width = 300
  height = 200
  myImage = Image(Point(width,height),"img/drawing2.png")
  myImage.draw(win)

  
  #beginning instruction
  print("""Hello! Welcome to our Pie Chef Memory Game. You need to memorize all the ingredients (in order!) to make a pie. The recipe will appear after you choose the pie, and it will disappear after 5 seconds.
You can choose to make: blueberry, apple, or pumpkin pie.
What kind of pie would you like to make today? (Click on the screen to continue.)""")
  text = Text(Point(300,50), "Pie Chef Memory Game")
  text.setSize(27)
  text = text_draw(text)
  

  text = Text(Point(300, 90), """Memorize all the ingredients (in order!) to make 
a pie after 5 seconds of looking at the recipe!""")
  text.setSize(14)
  text = text_draw(text)
  
  text = Text(Point(300,100), "What kind of pie would you like to make today?")
  text.setSize(14)
  text.setTextColor("purple")
  text.draw(win)
  win.getMouse()
  

  pie_type = pie_choice()
  text.undraw()
    
  #jump to each type of pie based on user's choice
  if pie_type == 'blueberry':
    blueberry_image = Image(Point(width+170,height+100), "img/recipe_blueberry2.png")
    blueberry_image.draw(win)
    time.sleep(5)
    blueberry_image.undraw()
    pie_blueberry = Pie()
    
    #decide whether the user's choices of ingredients are correct
    if pie_blueberry.blueberry():
      if pie_blueberry.sugar():
        if pie_blueberry.pieCrust():
          blueberry_pie = Image(Point(300,180), "img/blueberry_pie.png")
          text = Text(Point(300,100), "Congratulations! You made a pie!")
          text.setSize(24)
          text.setTextColor("#2189d9")
          blueberry_pie.draw(win)
          text.draw(win)
          cls()
        else:
          wrongIngredient()
      else:
        wrongIngredient()
    else:
      wrongIngredient()

  elif pie_type == 'apple':
    apple_image = Image(Point(width+20,height+80), "img/recipe_apple.png")
    apple_image.draw(win)
    time.sleep(5)
    apple_image.undraw()
    pie_apple = Pie()
    #decide whether the user's choices of ingredients are correct
    if pie_apple.apple():
      if pie_apple.sugar():
        if pie_apple.butter():
          if pie_apple.pieCrust():
            apple_pie = Image(Point(300,195), "img/apple_pie.png")
            text = Text(Point(300,100), "Congratulations! You made a pie!")
            text.setSize(24)
            text.setTextColor("#d64f3a")
            apple_pie.draw(win)
            text.draw(win)
            cls()
          else:
            wrongIngredient()
        else:
          wrongIngredient()
      else:
        wrongIngredient()
    else:
        wrongIngredient()
      
  elif pie_type == 'pumpkin':
    pumpkin_image = Image(Point(width+170,height+100), "img/recipe_pumpkin2.png")
    pumpkin_image.draw(win)
    time.sleep(5)
    pumpkin_image.undraw()
    pie_pumpkin = Pie()
    #decide whether the user's choices of ingredients are correct
    if pie_pumpkin.pumpkin():
      if pie_pumpkin.sugar():
        if pie_pumpkin.butter():
          if pie_pumpkin.flour():
            if pie_pumpkin.pieCrust():
              pumpkin_pie = Image(Point(300,195), "img/pumpkinpie3.png")
              text = Text(Point(300,100), "Congratulations! You made a pie!")
              text.setSize(24)
              text.setTextColor("#f59542")
              pumpkin_pie.draw(win)
              text.draw(win)
              cls()
            else:
              wrongIngredient()
          else:
            wrongIngredient()
        else:
          wrongIngredient()
      else:
        wrongIngredient()
    else:
      wrongIngredient()
  else:
    print("That's not an option, sorry!")



if __name__ == "__main__":
  if (test_mode):
    myTests()
  else:
    main()
