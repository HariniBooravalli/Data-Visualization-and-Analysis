from randomwalk import RandomWalk
from random import choice
from matplotlib import pyplot as plt


#calling the class and intializing the take_walk for generatin of points
rw = RandomWalk()
rw.take_walk()

input_vec=rw.x
output_vec=rw.y

#to get multiple plots ina single graph
fig, ax = plt.subplots()

#using seaborn style of writing
plt.style.use('seaborn-deep')

ax.scatter(input_vec,output_vec,c='blue',s=10)

#we set few characterstics here, like labeling the x axis , y axis , thickness of the plot and so on
ax.set_title("Random Walk", fontsize=24)
ax.set_xlabel("X-Coordinate", fontsize=12)
ax.set_ylabel("Y-Coordinate", fontsize=12)


#Set size of tick labels
ax.tick_params(axis='both',labelsize=12)

plt.show()