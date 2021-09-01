################################################
 # Saving Frames Assignment 
 # By Aditya Khan
 # June 17, 2021
 # Purpose: To create a program where one can record the actions that they do on the display screen
 # and record it as saving seperate frames. To that end, this program is primarily an animation using 
 # interesting curves created by using trigonometry. In terms of interaction, one can play with how the
 # curves look. By pressing the shift button and moving the mouse, the curves can be moved in interesting
 # ways. Another thing that can be done is have a sphere pop out towards the user. This is done by pressing
 # 'b'. To slow down or speed up the animation, simply use the up and down arrow keys. This changes the frame
 # rate of the animation. One more thing that can be done, is summon snowballs, that by virtue of being wet, 
 # "wash" away the background and the designsm by pressing the right mouse buttom. The background can be 
 # restored immediately, and the snowballs hidden, by re-pressing the right mouse button. To record the animation
 # press 'r' when ready, and press the space bar when finished. The frames will appear in a folder names: output. 
 # Extra for experts has been challenged. 
################################################

from Snow import Snow

move = PI # Changing this variable causes the movement of the curves. 
snows = [] # An array to store every instance of the snowballs.
numDrops = 50 # # Number of snowball instances to create. 

mouseMove = False # Controls whether the mouse can move the curves.
snowState = False # Controls snow fall and precipitates the effects of snow fall. 

alphaVal = 30 # The opacity of the curve in the background. 

frameChange = 60.0 # The frame rate - changing it can change the speed of the animations. 
backgroundVal = 20.0 # The fill of the background. 

recording = False # Variable that controls whether recording happens or not. 


def setup():
    global numDrops, snows, frameChange
    
    size(1000, 800, P3D) 
    
    # Additions that make the curves appear slightly smoother/nicer. 
    blendMode(ADD)  
    smooth()

    # Creates 50 snowballs and adds it to the list of snowballs. 
    for i in range(numDrops):
        
        # Randomises the positioning of the snowballs. 
        xpos = random(30, width-30)
        ypos = random(-50, -150) # Negative to appear off screen initially. 
        
        # Randomises the dropping speed. 
        yspeed = random(5, 25) 
        
        # Controls the thickness of the ball. 
        thickness = random(2, 6)
        
        snow = Snow(xpos, ypos, yspeed, thickness)
        snows.append(snow) # Appends each snowball created to the list of snowballs. 
        

def draw():

    global move, alphaVal, frameChange, snowState, backgroundVal
    
    background(backgroundVal)
    frameRate(frameChange)
    strokeWeight(5)
    
    
    if keyPressed:
        
        # Pressing 'b' displays a sphere. 
        if key == 'b':
    
            pushMatrix()
            translate(width/2, height/2) 
            stroke(0, 255, 0, 25)
            noFill()
            
            # Equation one uses tan. As it is a circular function, the sphere jumps forward and backward. 
            sphere(equationOne(move/2)) 
            popMatrix()
            
        # Pressing the up arrow increases the frame rate. 
        if keyCode == UP:
            frameChange += 0.1
        
        # Pressing the down arrow decreases the frame rate. 
        if keyCode == DOWN:
            frameChange -= 0.1
    
    
    if snowState:
        alphaVal -= 0.1 # The curves become increasingly translucent until they are invisible. 
        if backgroundVal < 200: # The background becomes lighter. 
            backgroundVal += 0.65
            
        # Pulls each snowball from the array and calls the snowball's display and fall functions. 
        for snow in snows:
            snow.display()
            snow.fall()
            
    # The opacity and background colour are returned to default. 
    elif snowState == False:
        alphaVal = 30.0
        backgroundVal = 20.0

    backgroundDesign(alphaVal) # The curve design. 

    move += PI/4 # Ensures that the movement of the curves continue perpetually. 
    
    recordingFeature() # The recording capability. 
    
    print(frameChange)
    
def mousePressed():
    
    # Pressing the right mouse button toggles the visibility of the snowballs. 
    if mouseButton == RIGHT:
        global snowState
        snowState = not snowState
    
    
    
def keyPressed():
    global mouseMove, frameChange, recording
    
    # Pressing shift allows for the user to control the curves. 
    if keyCode == SHIFT:
        mouseMove = not mouseMove
            
    # Pressing 'r' toggles the recording capability. 
    if str(key).lower() == "r": 
        recording = not recording 
        
    # The space button exits the program. 
    if str(key) == " ": 
        exit()


# This function controls the recording capability of the program.  
def recordingFeature():
    global recording
    
    if recording: 
        saveFrame("output/frames####.png") # Save the current frame if recording is True. 
            
    # Display a message on how to record. 
    textAlign(CENTER) 
    fill(255) 
        
    if not recording: 
        text("Press r to start recording. Press SPACE to stop the program.", width/2, height-24) 
    else:
        text("Press r to stop recording. Press SPACE to stop the program.", width/2, height-24) 
    
    # Shows a red circle when recording and a blank one when not. 
    stroke(255) 
    if recording: 
        fill(255, 0, 0) 
    else: 
        noFill() 
        ellipse(width/2, height-48, 16, 16)


# This function controls the background curves. 
def backgroundDesign(alphaValue):
    pushMatrix()
    noFill()
    
    translate(width/2, height/2)
    
    # For loops allows multiple rectangles to be in play. 
    for i in range(0, 100, 1):
        
        # The red curve. 
        stroke(255, 0, 0, alphaValue)
        if mouseMove:
            rect(equationOne(mouseX/10+i), equationFour(move+i), equationThree(mouseX/10+i), equationTwo(move+i))
        else:
            rect(equationOne(move+i), equationFour(move+i), equationThree(move+i), equationTwo(move+i))
        
        # The green curve. 
        stroke(0, 255, 0, alphaValue)
        if mouseMove:
            ellipse(equationOne(move+i+30), equationTwo(-mouseY/10+i+3), equationThree(move+i+30), -equationFour(mouseY/10+i+3))    
        else:
            ellipse(equationOne(move+i+30), equationTwo(-move+i+3), equationThree(move+i+30), -equationFour(move+i+3))
    
        # Rotates the two curves. 
        rotate(radians(PI/2))
        
    popMatrix()    



# Four trigonometric equations that help create the curve. 
def equationOne(theta):
    answer = tan(theta/25) * 300 
    return answer


def equationTwo(theta):
    global move
    answer = cos(theta/30) * 100
    return answer


def equationThree(theta):
    answer = cos(theta/10) * 200
    return answer

def equationFour(theta):
    answer = sin(theta/15) * 300
    return answer

    
