import math
from math import sin, cos, tan, sqrt, asin, atan
import turtle

import numpy as np


class ProjectileMotion:
    
    def __init__(self, velocity, angle):
        # Initialized variables: theta, V, time
        # Dependent variables: Vy
        # Constants: Vx, ay, dy
        self.V = velocity
        self.theta = angle      
        self.ay = -9.8
        self.displacement = 0
        # self.Vx is constant while self.Vy gets smaller
        self.Vx, self.Vy = self.V_Components(self.V)
        self.Vy0 = self.Vy
        
    def __repr__(self):
        return f"velocity: {self.V}, angle above horizontal: {self.theta}"
    
    # Mult each instance variable by factor
    def __mul__(self, factor):
        pass
        
    def V_Components(self, velocity):
        # Convert to degrees
        return ( velocity * cos( math.radians(self.theta) ), 
                velocity * sin( math.radians(self.theta) ))
    
    def displace(self, time, acceletation):
        return 0
    
    # If the user does not launch on Earth
    def changeAcceleration(self, acceleration):
        self.ay = acceleration
        
    # self.move fundamentally only partakes
    # what angle projectile moves, and how far.
    def move(self, time):
        
        dx = self.Vx*time
        dy = self.Vy0*time + (1/2)*self.ay * time**2
        self.displacement = sqrt(dx**2 + dy**2)
        
        # Formula that changes V components and has displacement
        # Vy**2 = Vy0**2 + 2*ay*dy
        self.Vy = sqrt( self.Vy0**2 + 2*self.ay*dy )
        
        # As Vy changes, theta changes as such converted to degrees
        self.theta = math.degrees( atan(self.Vy/self.Vx) )

        return (self.theta, self.displacement)
    
    
    
    
class App:
    
    def __init__(self, projectile, *kinematics):
        if not (isinstance(projectile, ProjectileMotion)):
            raise AttributeError("projectile is not of class ProjectileMotion")
        self.projectile = projectile
        
        # Item is the turtle for projectile
        self.item = turtle.Turtle()
        self.item.speed(0.1)
        
        
    # shape, color, etc.
    def projectileProperties(**kwargs):
        pass
    
    def motion(self, timeInterval):
        for time in np.arange(0, 1.01, timeInterval):
            angle, displacement = self.projectile.move(time)
            
            self.item.setheading(angle)
            self.item.forward(displacement)


# def main():
#     velocity = float(input("Set your initial velocity: "))
#     angle = float(input("At what angle above the horizontal (degrees)? "))
#     projectile = ProjectileMotion(velocity, angle)
#     simulation = App(projectile)
#     simulation.motion(0.01)
    
#     turtle.done()

# if __name__ == '__main__':
#     main()




























      
      
      
      
      
    