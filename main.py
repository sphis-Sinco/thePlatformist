def on_a_pressed():
    startScreen_Input()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def startScreen():
    global gameState
    scene.set_background_color(15)
    scene.set_background_image(assets.image("""
        startscreen
    """))
    gameState = 0
def startScreen_Input():
    global gameState
    if gameState == 0:
        gameState = 1
gameState = 0
startScreen()