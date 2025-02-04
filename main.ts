controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (gameState == 0) {
    	
    }
})
function startScreen () {
    scene.setBackgroundColor(15)
    scene.setBackgroundImage(assets.image`startscreen`)
    gameState = 0
}
let gameState = 0
startScreen()
