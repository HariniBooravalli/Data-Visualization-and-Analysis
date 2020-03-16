from random import choice

class RandomWalk:
    """This class represents randmwalk class and its corresponding methods needed"""
    def __init__(self,number_of_stops=5000):
        self.number_of_stops=number_of_stops
        self.x=[0]
        self.y=[0]
    

    def take_walk(self):

        while len(self.x)< self.number_of_stops:
            #make some random choices for the movement of both x and y coordinates
            # #Start with x coordinates, -1 representing going on negative x axis and +1 representing the positive x axis 
            x_direction= choice([-1,1])
            # distance to travel
            x_distance = choice([0,1,2,3])

            #Start with x coordinates, -1 representing going on negative y axis and +1 representing the positive y axis 
            y_direction= choice([-1,1])
            # distance to travel
            y_distance = choice([0,1,2,3])

            #calculate the displacemnet
            x_displacement = x_direction*x_distance
            y_displacement = y_direction*y_distance

            if x_displacement==0 and y_displacement==0:
                continue

            #to find the next stop
            x_coordinate=self.x[-1]+x_displacement
            y_coordinate=self.y[-1]+y_displacement

            #add thi coordinate to the x and y lists
            self.x.append(x_coordinate)
            self.y.append(y_coordinate)

            
            





        