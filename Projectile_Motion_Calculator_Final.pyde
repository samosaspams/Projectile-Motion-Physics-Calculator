'''
Ameya Shukla 18/06/2023

This is a projectile motion calculator, which can calculate the properties of a projectile when given certain variables by the user. The code also includes an animation
and an instructions page which explains what the calculator is and how to use it. 
'''
#Sets up code
def setup():
            
    #Define global variables
    global mainMenu, calculatorScreen, instructionButtonPressed, instructionsPage, valueTime, valueHorizontalDisplacement, valueVelocity, valueLaunchAngle, valueHeight, activeInput, timeInputEnabled, heightInputEnabled, horizontalDisplacementInputEnabled, launchAngleInputEnabled, velocityInputEnabled, solveForHeight, solveForVelocity, solveForTime, solveForHorizontalDisplacement, mainMenuProjectileX, mainMenuProjectileY, calculateButtonPressed, previousCalculationButtonPressed, previousAnswersList
    
    #Assign values to global variables
    valueTime = ""
    valueHorizontalDisplacement = ""
    valueVelocity = ""
    valueLaunchAngle = ""
    valueHeight = ""
    activeCursor = ""
    mainMenu = True
    calculatorScreen = False
    instructionButtonPressed = False
    instructionsPage = False
    
    activeInput = None
    
    #Disable input boxes
    timeInputEnabled = False
    heightInputEnabled = False
    horizontalDisplacementInputEnabled = False
    velocityInputEnabled = False
    launchAngleInputEnabled = False
    
    #False if user has not chosen to solve for anything
    solveForTime = False
    solveForHeight = False
    solveForHorizontalDisplacement = False
    solveForVelocity = False
       
    accelerationGrav = -9.8 #Used in formulas 
    previousAnswersList = [] #Define list to store previous calculations 
    
    #Set initial point of main menu projectile animation
    mainMenuProjectileX = 173
    mainMenuProjectileY = 435
    
    #Set calculate button and previous calculation(s) buttons to false
    calculateButtonPressed = False
    previousCalculationButtonPressed = False
    
    #Set size to 600x600 pixels and background to white
    size(600,600)
    background(255)
    
#Define and create back button (which returns to previous page) when function is called
def backButton():
    fill(288,0,0)
    rect(533,8,50,25)
    fill(288,288,288)
    text("Back", 536,28)
    
#Creates button which takes user to instructions page from calculator screen
def instructionButton():
    fill(255,102,0)
    rect(13,9,210,25)
    fill(288,288,288)
    text("Instructions and Manual", 16,28)
    
#Creates button which takes user to previous calculations page from calculator screen
def previousCalculationButton():
    fill(128,128,128)
    rect(248,9,240,25)
    fill(288,288,288)
    text("View Previous Calculation", 254,27.5)
    
#Creates buttons from where user can choose what they want to solve for
def liveInstructionBar():
    rect(-3,43,605,89)
    fill(288,0,0)
    
    #Prints question to canvas
    textSize(22)
    text("What do you want to solve for?", 20,66)
    textSize(20)
    
    #Create boxes for each variable which, when pressed, will allow the user to solve for the respective variable
    rect(21,89,84,27)
    fill(288,288,288)
    text("Time", 29,109)
    
    #Create horiz.displacement box
    fill(288,0,0)
    rect(132,89,172.5,27)
    fill(288,288,288)
    text("Horiz.Displacement", 138,109)
    
    #Create velocity box
    fill (288,0,0)
    rect(323,89,84,27)
    fill(288,288,288)
    text("Velocity", 329,109)
    
    #Create height box
    fill(288,0,0)
    rect(433,89,84,27)
    fill(288,288,288)
    text("Height", 442,109)
    
    #Will allow boxes will turn gold when pressed to tell the user which variable they clicked on
    if solveForTime == True:
        fill(212,175,55)
        rect(21,89,84,27)
        fill(288,288,288) #Resets fill 
        text("Time", 29,109)
        
    #Turns horizontal displacement box to gold when pressed
    if solveForHorizontalDisplacement == True:
        fill(212,175,55)
        rect(132,89,172.5,27)
        fill(288,288,288)
        text("Horiz.Displacement", 138,109)
        
    #Turns velocity box to gold when pressed
    if solveForVelocity == True:
        fill(212,175,55)
        rect(323,89,84,27)
        fill(288,288,288)
        text("Velocity", 329,109)
        
    #Turns height box to gold when pressed
    if solveForHeight == True:
        fill(212,175,55)
        rect(433,89,84,27)
        fill(288,288,288)
        text("Height", 442,109)
        
#Create and define the screen where user can see their calculation results
def previousCalculationScreen():
    #Re-define previousAnswerList to global
    global previousAnswersList
    
    #Set background to white
    background(255)
    
    #Print text to canvas
    textSize(18)
    fill(255,0,0)
    text("NOTE: This calculator will only store up to: calculations! \nAnything after is deleted",14,25)
    fill(0)
    text("Previous Calculations:", 14, 89)
    
    #Print user's calculations to canvas by using for loop to print list values
    yCoordinate = 116
    for calculationNumber, calculationValue in enumerate(previousAnswersList, start=1):
        calculationText = "Calculation {}: {}".format(calculationNumber, calculationValue)
        text(calculationText, 14, yCoordinate)
        yCoordinate += 30
       
   #Call back button in previous calculation page 
    backButton()
        
#Create instructions page
def instructionScreen():
    fill(0) #Set text color 
    
    #Define and print instructions to canvas
    instructions = "Projectile motion is the motion of an object through the air \n under the influence of gravity, where the object follows a curved path \ncalled a trajectory. It can have many properties including:time, velocity \nhorizontal displacement, and the height/angle it is launched at. \nOur calculator measures time in secs, horizontal displacement and \nheight in meters, velocity in meters/sec, and angle in degrees. \n\nHow to use this calculator tool:\nStep 1:Open calculator.\nStep 2: Choose which variable you want to solve for (input boxes are \ndisabled until you choose).\nStep 3: Once you choose, certain boxes will turn white, click \non them to enter numbers (you can enter max.3 digit numbers. The \nbox will turn red when clicked which means you can enter numbers). \nStep 4: Press calculate to find answer (answer will appear in a box \nwhich is highlighted gold). \nStep 5: Press clear to reset calculator and solve again! (you can view \nprevious calculaitons via the previous calculaitons tab)  "
    textSize(18.5)
    text(instructions, 19,23)

    #Create back button
    fill(288,0,0)
    rect(533,8,50,25)
    fill(288,288,288)
    text("Back",536,27)
        
#Define main menu
def mainMenuInterface():
    #Re-define the initial coordinates of the ball as global
    global mainMenuProjectileX, mainMenuProjectileY
    
    #Set background to white
    background(255)
        
    #Create buttons leading to calculator and instructions page
    fill(54,200,150)
    rect(50,120,500,50)
    rect(50,200,500,50)

    #Print welcome message and directions to canvas
    fill(0)
    textSize(25)
    text ("Welcome to the projectile motion calculator!",25,50)
    
    #Print directions to canvas
    textSize(20)
    text("Please check out the instructions before using calculator", 27,82)
    text("Click Here for Calculator", 77,154)
    textSize(20)
    text("Instruction Screen and Manual", 65,235)  
    
    #Print base of cannon
    fill(164,116,73)
    circle(105,567.5,70)#120,567
    
    #Print and rotate the barrel of the canon
    fill(128)
    cannon_angle = radians(-690)
    rotate(cannon_angle)
    rect(355,305,30,100)#370,305
    
    #Print parabolic path of projectile
    noFill()
    strokeWeight(4)
    beginShape()
    vertex(370,305)#300,135
    quadraticVertex(305,15,650,400)#340,10
    endShape()
    
    #Print and define position of projectile (ball)
    resetMatrix()
    fill(100,84.3,0)
    circle(mainMenuProjectileX,mainMenuProjectileY,25)  
    
    #Incrament projectile's coordinates in order to animate
    mainMenuProjectileX += 1
    mainMenuProjectileY = (0.020751953*((mainMenuProjectileX-237)**2))+350 #Vertex form used to update y value
    
    #Reset projectile coordinates once projectile leaves the screen
    if mainMenuProjectileY > 615:
        mainMenuProjectileX = 173
        mainMenuProjectileY = 435
            
#Create calculator screen
def calculatorInterface():
    
    #Re-define all variables that will be changed/used in this screen as global
    global valueTime, valueHorizontalDisplacement, valueVelocity, valueHeight, activeInput, timeInputEnabled, horizontalDisplacementInputEnabled, velocityInputEnabled, heightInputEnabled, launchAngleInputEnabled, solveForTime
    
    #Set background to white
    background(255)
    
    #Add buttons and instruction bar to calculator screen
    backButton()
    instructionButton()
    liveInstructionBar()
    previousCalculationButton()
    
    #Print cannon's platform to canvas
    fill(128,0,0)
    rect(70,400,100,200)
        
    #Print cannon's base to canvas
    fill(164,116,73)
    circle(120,369.4,60)
    fill(128)
    
    #Print and rotate cannon's barrel to canvas
    cannon_angle = radians(-690)
    rotate(cannon_angle)
    rect(276,134,30,100)
        
    #Print parabolic path of projectile to canvas
    noFill()
    strokeWeight(4)
    beginShape()
    vertex(290,135)#300,135
    quadraticVertex(380,25,850,400)#340,0
    endShape()
        
    #Print projectile to canvas
    resetMatrix()
    fill(100,84.3,0)
    circle(193,253,25)
    
    #If time input box is enabled, box turns white with black outline
    if timeInputEnabled == True:
        stroke(0)  
        fill(255)  
    else:
        #Box is grey if disabled
        stroke(128)  
        fill(192) 
        
    #Print time input box
    rect(17, 186, 90, 30) 
    
    #Set text color to black when time input box is enabled
    if timeInputEnabled == True:
        fill(0)  
    else:
        fill(128)  #Text color is grey when box is disabled
    stroke(0) 
    
    #Print input box label to canvas
    text("Time:", 17, 174)
    
    #Display user input to canvas
    text(valueTime, 23, 210)

    #Set horizontal displacement input box to white when enabled 
    if horizontalDisplacementInputEnabled == True:
        stroke(0)
        fill(255)
    else:
        #Set input box to grey when disabled
        stroke(128)
        fill(192)
        
    #Define horizontal input box
    rect(156, 186, 120, 30)
    
    #Set text color to black when input box enabled
    if horizontalDisplacementInputEnabled == True:
        fill(0)
    else:
        #Set to grey when disabled
        fill(128)
    stroke(0)
    
    #Print input box labels to canvas
    text("Horizontal", 156,157)
    text("Displacement:", 156, 174)
    
    #Print user input to canvas
    text(valueHorizontalDisplacement, 161, 210)

    #Set input box to white when enabled and grey when disabled
    if velocityInputEnabled == True:
        stroke(0)
        fill(255)
    else:
        stroke(128)
        fill(192)
        
    #Create velocity input box
    rect(295, 186, 90, 30)
    
    #Set text to black when input box enabled and grey when disabled
    if velocityInputEnabled == True:
        fill(0)
    else:
        fill(128)
        
    #Print input box label and user input to canvas in specific position 
    stroke(0)
    text("Velocity:", 294, 174)
    text(valueVelocity, 300, 210)

    #Set input box to white when enabled and grey when disabled
    if launchAngleInputEnabled == True:
        stroke(0)
        fill(255)

    else:
        stroke(128)
        fill(192)
        
    #Create launch angle input box
    rect(433, 186, 90, 30)
    
    #Set text to black when input box enabled and grey when disabled
    if launchAngleInputEnabled == True:
        fill(0)
    else:
        fill(128)
    
    #Print input box label (launch angle) and user input to canvas
    stroke(0)
    text("Launch Angle:", 433, 174)
    text(valueLaunchAngle, 438, 210)

    #Set height input box to white when enabled and grey when disabled
    if heightInputEnabled == True:
        stroke(0)
        fill(255)
    else:
        stroke(128)
        fill(192)
        
    #Create input box
    rect(433, 259, 96, 30)
    
    #Set text to black when enabled and grey when disabled
    if heightInputEnabled == True:
        fill(0)
    else:
        fill(128)
        
    #Print input box label (height) and user input (valueHeight) to canvas 
    stroke(0)
    text("Height:", 435, 246)
    text(valueHeight, 440, 282)
    
    #Print calculate button
    fill(0,288,0)
    rect(480,550,100,30)
    fill(0)
    text("Calculate!", 485,573)
    
    #Print clear button
    fill(250,250,0)
    rect(479,509,100,30)
    fill(0)
    text("Clear", 484, 532)
    noFill()
    
    #Highlight time input box with gold outline when time is solved for
    if solveForTime == True and calculateButtonPressed == True:
        noFill()
        stroke(255,215,0)
        rect(17, 186, 90, 30)
        stroke(0) 
        text("Time:", 17, 174)
        text(valueTime, 23, 210)
    
    #Highlight horizontal displacement input box with gold outline when horiz.displacement is solved for
    elif solveForHorizontalDisplacement == True and calculateButtonPressed == True:
        noFill()
        stroke(255,215,0)
        rect(156, 186, 120, 30)
        stroke(0)
        text("Horizontal", 156,157)
        text("Displacement:", 156, 174)
        text(valueHorizontalDisplacement, 161, 210)
        
    #Highlight velocity input box with gold outline when it is solved for
    elif solveForVelocity == True and calculateButtonPressed == True:
        noFill()
        stroke(255,215,0)
        rect(295, 186, 90, 30)
        stroke(0)
        text("Velocity:", 294, 174)
        text(valueVelocity, 300, 210)
        
    #Highlight height input box with gold outline when it is solved for
    elif solveForHeight == True and calculateButtonPressed == True:
        noFill()
        stroke(255,215,0)
        rect(433, 259, 96, 30)
        stroke(0)
        text("Height:", 435, 246)
        text(valueHeight, 440, 282)

    #Highlights input boxes as red when they are clicked on (indicates to user that they've successfully clicked on it)
    
    #Highlight time input box to red when clicked
    if activeInput == "timeInput":
        stroke(210,96,99)  
        rect(17, 186, 90, 30)
        stroke(0)
    else:
        stroke(0)  
        #rect(17, 186, 90, 30)
    
    #Highlight horiz.displacement input box to red when clicked
    if activeInput == "horizontalDisplacementInput":
        stroke(210,96,99)  
        rect(156, 186, 120, 30)
        stroke(0)
        
    else:
        stroke(0)  
        
    
    #Highlight velocity input box to red when clicked
    if activeInput == "velocityInput":
        stroke(210,96,99)  
        rect(295, 186, 90, 30)
        stroke(0)
        
    else:
        stroke(0)
        
    
    #Highlight launch angle input box to red when clicked
    if activeInput == "launchAngleInput":
        stroke(210,96,99)  
        rect(433,186,90,30)
        stroke(0)
    
    #Highlight height input box to red when clicked
    if activeInput == "heightInput":
        stroke(210,96,99)  
        rect(433,259,96,30)
        stroke(0)
       
    #Insert diagram label for horizontal displacement
    strokeWeight(2)
    stroke(174,23,234)
    line(177,585,453,585)
    strokeWeight(4)
    stroke(0)
    text("Horiz.Displacement (m)", 220, 580)
    
    #Insert diagram labels for height
    strokeWeight(2)
    stroke(174,23,234)
    line(61,401,61,600)
    strokeWeight(4)
    stroke(0)
    text("Height", 3, 438)
    
    #Print note to user
    fill(255,0,0)
    text("NOTE:\nVelocity is \nspeed of projectile", 428,328)
    noFill()

#Define draw function (repeats forever..all permanent items placed here)
def draw():
        
    #If main menu variable is true, display main menu screen
    if mainMenu is True:
        mainMenuInterface()

    #If calculator variable is true, display calculator screen
    if calculatorScreen is True:
        calculatorInterface()
        
    #If either instructions variable is true, display instructions screen
    if instructionButtonPressed is True or instructionsPage is True:
        instructionScreen()
        
    #If prevous calculation variable is true, display previous calculation screen
    if previousCalculationButtonPressed is True:
        previousCalculationScreen()
        
#Define mouse clicked function (all actions when mouse clicked placed here)
def mouseClicked():
    
    #Print coordinate which is clicked by user
    print("Clicked", "X:", mouseX, "Y:", mouseY)

    #Re-define all variables which will be used/changed in this function as global 
    global mainMenu, calculatorScreen, instructionButtonPressed, instructionsPage, inputType, valueTime, valueHeight, valueVelocity, valueLaunchAngle, valueHorizontalDisplacement, activeInput, timeInputEnabled, heightInputEnabled, horizontalDisplacementInputEnabled, velocityInputEnabled, launchAngleInputEnabled, solveForTime, solveForHeight, solveForHorizontalDisplacement, solveForVelocity, calculateButtonPressed, previousCalculationButtonPressed, previousAnswersList
  
    #Define actions from main menu
    if mainMenu is True:
        
        #Takes user to calculator screen from main menu when calculator button pressed
        if mouseX >= 50 and mouseX <= 550 and mouseY >= 120 and mouseY <= 170:
            mainMenu = False
            calculatorScreen = True
            
        #Takes user to instructions page from main menu when instructions button pressed
        elif mouseX >= 50 and mouseX <= 550 and mouseY >= 200 and mouseY <= 250:
            mainMenu = False
            background(255)
            instructionsPage= True
            
    #Define actions from calculator screen itself
    elif calculatorScreen is True:
        
        #Take user to main menu when back button pressed 
        if mouseX >=532 and mouseX <= 584 and mouseY >= 9 and mouseY <= 35:
            calculatorScreen = False
            background(255)
            mainMenu = True
            
        #Take user to instructions page when instructions button pressed
        if mouseX >= 13 and mouseX <= 225 and mouseY >= 12 and mouseY <= 36:
            calculatorScreen = False
            background(255)
            instructionButtonPressed = True
            
        #Take user to previous calculations page when previous calculation button pressed
        if mouseX >= 248 and mouseX <= 488 and mouseY >= 11 and mouseY <= 35:
            calculatorScreen = False
            background(255)
            previousCalculationButtonPressed = True
            
        #Enable horiz.disp. input box and velocity and height input box when user chooses to solve for time
        if mouseX >= 20 and mouseX <= 105 and mouseY >= 87 and mouseY <= 116 and not (solveForHorizontalDisplacement or solveForVelocity or solveForHeight):
            horizontalDisplacementInputEnabled = True
            heightInputEnabled = True
            velocityInputEnabled = True
            solveForTime = True
            
        #Enable time, velocity, and launch angle input box when user chooses to solve for horiz.displacement     
        if mouseX >= 132 and mouseX <= 305 and mouseY >= 90 and mouseY <= 119 and not (solveForTime or solveForVelocity or solveForHeight):
            timeInputEnabled = True
            velocityInputEnabled = True
            launchAngleInputEnabled = True
            solveForHorizontalDisplacement = True
            
        #Enable time and horizontal.disp input boxes when user chooses to solve for velocity 
        if mouseX >= 325 and mouseX <= 407 and mouseY >= 89 and mouseY <= 117 and not (solveForHorizontalDisplacement or solveForTime or solveForHeight):
            timeInputEnabled = True
            horizontalDisplacementInputEnabled = True
            solveForVelocity = True
            
        #Enable time input box when user chooses to solve for height
        if mouseX >= 435 and mouseX <= 517 and mouseY >= 90 and mouseY <= 117 and not (solveForHorizontalDisplacement or solveForTime or solveForVelocity):
            timeInputEnabled = True
            solveForHeight = True
        
        #Assigns user input to time when time input box clicked meaning any values a user enters will be added to valueTime
        if mouseX >= 17 and mouseX <= 106 and mouseY >= 185 and mouseY <= 214 and timeInputEnabled == True:
            inputType = "timeInput"
            activeInput = "timeInput"
            cursor(TEXT) #Change cursor when input box clicked
            
        #Assigns user input to horizontal.disp when horizontal.disp input box clicked
        elif mouseX >= 156 and mouseX <= 246 and mouseY >= 188 and mouseY <=219 and horizontalDisplacementInputEnabled == True:
            inputType = "horizontalDisplacementInput"
            activeInput = "horizontalDisplacementInput"
            cursor(TEXT) #Changes cursor style when input box clicked (lets user know they can input)
            
        #Assigns user input to velocity when velocity input box clicked
        elif mouseX >= 295 and mouseX <= 384 and mouseY >= 188 and mouseY <= 218 and velocityInputEnabled == True:
            inputType = "velocityInput"
            activeInput = "velocityInput"
            cursor(TEXT) #Changes cursor style
        
        #Assigns user input to launch angle when launch angle input box clicked
        elif mouseX >= 433 and mouseX <= 524 and mouseY >= 189 and mouseY <= 219 and launchAngleInputEnabled == True:
            inputType = "launchAngleInput"
            activeInput = "launchAngleInput"
            cursor(TEXT) #Changes cursor style
            
        #Assigns user input to height when height input box clicked 
        elif mouseX >= 434 and mouseX <= 524 and mouseY >= 260 and mouseY <= 291 and heightInputEnabled == True:
            inputType = "heightInput"
            activeInput = "heightInput"
            cursor(TEXT) #Changes cursor style
            
        #If no input box clicked, user input is not assigned to any specific variable
        else:
            inputType = None
            activeInput = None
            cursor(ARROW)
        
        #If calculate button clicked
        if mouseX >= 480 and mouseX <= 580 and mouseY >= 550 and mouseY <= 583:
            
            #Indicate to computer that calculate button has been pressed 
            calculateButtonPressed = True
                
            #If time input box is empty and user wants to solve for time
            if valueTime == "" and solveForTime == True:
                #Calculate only if there is a value for height
                if valueHeight != "":
                    
                    #Use time-height formula to find time of projectile's flight
                    timeValueHeight = float(valueHeight)
                        
                    accelerationGrav = 9.8
                    calculatedValueTime = sqrt((2 * timeValueHeight) / accelerationGrav)
                    calculatedValueTime = round(calculatedValueTime,2)
                    valueTime = str(calculatedValueTime)
                    
                    #Format and append calculated value to previousAnswersList so that it can be viewed in previous calculations page
                    displayedValueTime = "time = {} {}".format(valueTime, "second (s)")
                    previousAnswersList.append(displayedValueTime)
                        
                #Calculate for time if given velocity and horizontal displacement                    
                elif valueVelocity != "" and valueHorizontalDisplacement != "":
                    
                    #Use speed-distance-time formula to solve for time
                    velocityValue = float(valueVelocity)
                    displacementValue = float(valueHorizontalDisplacement)
                    calculatedValueTime = displacementValue / velocityValue
                    calculatedValueTime = round(calculatedValueTime, 3)
                    valueTime = str(calculatedValueTime)
                    
                    #Format and append calculated value to list in order to view it in previous answers page
                    displayedValueTime = "time = {} {}".format(valueTime, "second(s)")
                    previousAnswersList.append(displayedValueTime)
                        
            #If horizontal displacement box is empty and user wants to solve for horizontal.disp
            if valueHorizontalDisplacement == "" and solveForHorizontalDisplacement == True:
                
                #Will solve only if time, launch angle, and velocity have a value
                if valueTime != "" and valueLaunchAngle != "" and valueVelocity != "":
                    
                    #Use kinematics formulas to solve for horizontal displacement
                    valueTime = float(valueTime)
                    valueVelocity = float(valueVelocity)
                    valueLaunchAngle = float(valueLaunchAngle)
                    
                    #Use cos to find x-component of launch angle to find x-component of velocity 
                    horizontalVelocity = valueVelocity * cos(valueLaunchAngle)
                    
                    #Solve for horizontal displacement 
                    halfAccelerationGrav = 9.8 / 2
                    calculatedValueHorizontalDisplacement = ((horizontalVelocity * valueTime) + (halfAccelerationGrav * (valueTime ** 2)))
                    calculatedValueHorizontalDisplacement = round(calculatedValueHorizontalDisplacement, 0)
                    valueHorizontalDisplacement = str(calculatedValueHorizontalDisplacement)
                    
                    #Append and format value to list in order to view it in previous calculations page
                    displayedValueHorizontalDisplacement = "horizontal displacement = {} {}".format(valueHorizontalDisplacement, "meters")
                    previousAnswersList.append(displayedValueHorizontalDisplacement)
                    
            #Solve for velocity if velocity input box is empty and if user chooses to solve for velocity 
            if valueVelocity == "" and solveForVelocity == True:
                
                #Will solve only if time and horizontal displacement have a value
                if valueTime != "" and valueHorizontalDisplacement != "":
                    
                    #Convert given values to float
                    valueTime = float(valueTime)
                    valueHorizontalDisplacement = float(valueHorizontalDisplacement)
                    
                    #Use speed-distance-time equation to solve for velocity 
                    calculatedValueVelocity = (valueHorizontalDisplacement/valueTime)
                    calculatedValueVelocity = round(calculatedValueVelocity, 3)
                    valueVelocity = str(calculatedValueVelocity)
                    
                    #Format and append values to list in order to view it in previous calculations page
                    displayedValueVelocity = "velocity = {} {}".format(valueVelocity, "meters/second")
                    previousAnswersList.append(displayedValueVelocity)
                    
            #Solve for height if user chooses to solve for height and height input box is empty
            if valueHeight == "" and solveForHeight == True:
                
                #Will solve only if time has a value
                if valueTime != "":
                    
                    #Convert time to float
                    valueTime = float(valueTime)
                    
                    #Use formula to solve for height given time
                    accelerationGrav = 9.8
                    calculatedValueHeight = ((accelerationGrav*(valueTime**2))/2)
                    calculatedValueHeight = round(calculatedValueHeight, 3)
                    valueHeight = str(calculatedValueHeight)
                    
                    #Append and format value to list in order to view in previous calculation page
                    displayedValueHeight = "height = {} {}".format(valueHeight, "meters")
                    previousAnswersList.append(displayedValueHeight)
                    
        #Reset all variables when clear button pressed
        if mouseX >= 481 and mouseX <= 580 and mouseY >= 509 and mouseY <= 540:
            valueLaunchAngle = ""
            valueHeight = ""
            valueTime = ""
            valueHorizontalDisplacement = ""
            valueVelocity = ""
            
            timeInputEnabled = False
            heightInputEnabled = False
            horizontalDisplacementInputEnabled = False
            velocityInputEnabled = False
            launchAngleInputEnabled = False
            
            solveForHeight = False
            solveForHorizontalDisplacement = False
            solveForTime = False
            solveForVelocity = False
            
            calculateButtonPressed = False
      
  #Define actions for instructions screen      
    elif instructionButtonPressed is True:
        
        #Take user back to calculator screen from instructions page when back button pressed
       if mouseX >= 533 and mouseX <= 584 and mouseY >= 9 and mouseY <= 36:
        instructionButtonPressed = False
        background(255)
        calculatorScreen = True 
        
    #Take user back to main menu when instructions page back button pressed
    elif instructionsPage is True:
        if mouseX >=532 and mouseX <= 584 and mouseY >= 9 and mouseY <= 35:
            instructionsPage = False
            background(255)
            mainMenu = True
            
    #Take user back to calculator screen from previous calculation screen if back button pressed
    elif previousCalculationButtonPressed is True:
        if mouseX >= 533 and mouseX <= 585 and mouseY >= 10 and mouseY <= 36:
            previousCalculationButtonPressed = False
            background(255)
            calculatorScreen = True
        
#Define course of action when user enters input
def keyPressed():
    #Re-define all global variables used in this function 
    global inputType, valueTime, valueHorizontalDisplacement, valueVelocity, valueLaunchAngle, valueHeight, activeInput

    #Append user inputs to valueTime if inpytType is time input
    if inputType == "timeInput":
        if key.isdigit() or (key == '.' and '.' not in valueTime): #Restricts user into entering only numbers and ONE decimal place
    
           #Restrict length to only 3 digits
            if len(valueTime) < 3:
                valueTime += key #Add the key user presses to value time variable
            
        #Allow user to delete digits via string slicing 
        elif (key == BACKSPACE or key == DELETE) and len(valueTime) > 0:
            valueTime = valueTime[:-1]
        
    #Append user input to valueHorizontalDisplacement  if input type is horizontalDisplacementInput
    elif inputType == "horizontalDisplacementInput":
        if key.isdigit() or (key == '.' and '.' not in valueHorizontalDisplacement): #Restricts user into entering only numbers and ONE decimal place
            if len(valueHorizontalDisplacement) < 3:#Restricts length to 3 digits
                valueHorizontalDisplacement += key
        elif (key == BACKSPACE or key == DELETE) and len(valueHorizontalDisplacement) > 0: #Lets user delete digits via string slicing
            valueHorizontalDisplacement = valueHorizontalDisplacement[:-1]  
            
    #Append user inputs to valueVelocity if inpyt type is velocity input
    elif inputType == "velocityInput":
        if key.isdigit() or (key == '.' and '.' not in valueVelocity): #User can only enter numbers or 1 decimal place
            if len(valueVelocity) < 3: #Restrict length to 3 digits
                valueVelocity += key
        elif (key == BACKSPACE or key == DELETE) and len(valueVelocity) > 0: #User can delete digits via string slicing
            valueVelocity = valueVelocity[:-1]   
            
    #Append user inputs to valueLaunchAngle if input type is launch angle input
    elif inputType == "launchAngleInput":
        if key.isdigit() or (key == '.' and '.' not in valueLaunchAngle): #isdigit() function only lets user enter numbers
           if len(valueLaunchAngle) < 3:#Restrict length to 3 digits 
                valueLaunchAngle += key
        elif (key == BACKSPACE or key == DELETE) and len(valueLaunchAngle) > 0: #Lets user delete digits if delete (mac) or backspace (windows) is pressed
            valueLaunchAngle = valueLaunchAngle[:-1]   
            
    #Append user inputs to valueHeight if input type is height input
    elif inputType == "heightInput":
        if key.isdigit() or (key == '.' and '.' not in valueHeight): #Only lets user enter numbers or 1 decimal place
            if len(valueHeight) < 3:#Restrict length to 3 digits
                valueHeight += key
        elif (key == BACKSPACE or key == DELETE) and len(valueHeight) > 0: #User can delete digits via string slicing 
            valueHeight = valueHeight[:-1]  
