
# Snow class is defined. 
class Snow(object):
    
    # The constructor function helps initialise the snowballs with the given characteristics. 
    def __init__(self, xpos, ypos, yspeed, thickness):
        
        # Determines the position of the snow ball. 
        self.xpos = xpos
        self.ypos = ypos
        
        self.yspeed = yspeed # The speed. 
        self.thickness = thickness # The thickness. 
        
    
    # Function to display the instance of the snow ball at the given x-position, y-position, with the proper fill and thickness. 
    def display(self):
        fill(255)
        strokeWeight(self.thickness)
        ellipse(self.xpos, self.ypos, 10, 10)
        
    # Function that allows the snowball to fall.       
    def fall(self):
        
        # Movement - the y position is continually changed by its speed. 
        self.ypos += self.yspeed
        
        # If the snow ball's y position is below the screen, then it reappears elsewhere. 
        if self.ypos > height:
            self.ypos = random(-50, -150)
            self.xpos = random(30, width-30)
            

                

        

                           
