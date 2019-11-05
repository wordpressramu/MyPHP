import pyautogui as gui, time
def testfirefox():
    screenWidth, screenHeight = gui.size()
    gui.moveTo(5,screenHeight)
    
    gui.click()
    gui.typewrite('Control Panel', interval=0.25)
    
    gui.press('enter')
    time.sleep(4)
    gui.keyDown('alt')
    gui.press(' ')
    gui.press('x')
    gui.keyUp('alt')
    #gui.getWindow("All Control Panel Items").minimize()
    #gui.getWindow("All Control Panel Items").maximize()
    time.sleep(2)
    gui.moveTo(400,40,2)
    gui.click()
    gui.typewrite("Control Panel\All Control Panel Items\Programs and Features\WinRAR 5.31 beta 1 (32-bit)")
    gui.press('enter')
	#gui.getWindow("Stack Overflow").minimize()
	#gui.getWindow("music").maximize()
	#gui.pyautogui.displayMousePosition() #display mouse position
	
    '''
    gui.keyDown('alt')
    gui.press(' ')
    gui.press('x')
    gui.keyUp('alt')
    gui.click(250,22)
    gui.click(371,51)
    gui.typewrite('https://medium.com/financeexplained')
    gui.press('enter')
    '''
    
    
    #https://medium.com/financeexplainedhttps://medium.com/financeexplained
def identifyloc():
    while True:
        currentMouseX, currentMouseY = gui.position()
        print(currentMouseX,currentMouseY)
        time.sleep(3)
testfirefox()
