import pgzrun

WIDTH = 500
HEIGHT = 500

TITLE='Good Shot Game'

#any image that we need to make as a character - we use actor function
image=Actor('alien') #this is the path of the image 

def draw():
    screen.clear() #this clears the screen
    screen.fill(color=(255,119,51))
    
   
pgzrun.go()