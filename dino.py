import pyautogui as pag
from PIL import ImageGrab
import time

# Defining Function for hitting the Key required
def hit(key):
    pag.keyDown(key)
    return

# Defining Function for getting the screenshot of game window
def takeScreenshot():
    image = ImageGrab.grab().convert("L")
    # image.show()          for displaying the screenshot
    return image  

# Defining function for determining obstacle  ( Trial and Error for getting coordinates )
def isCollide(data):
    # Detect Birds
    for i in range(300,415):
        for j in range(410,563):
            if data[i, j] > 100 :
                hit("down")
                return

    # Detect Cactus
    for i in range(300,415):
        for j in range(563,650):
            if data[i, j] > 100 :
                hit("up")
                return
                
    return

# the calling function
if __name__ == '__main__':
    print('Hey! Dino Game is about to start in 2s')
    time.sleep(2)
    # hit("up")
    while True:
        image = takeScreenshot()
        data = image.load()
        isCollide(data)