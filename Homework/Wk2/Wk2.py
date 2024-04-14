import matplotlib.pyplot as plot


# COPIED FROM ASSIGNMENT 

# set up your lists
#numlist = [8, 6, 5, 3]
newVals = [10, 3, 22, 45]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['red', 'green', 'pink', 'purple']
explodelist = [0.1, 0.1, 0.1, 0.1]
# make the pie chart
plot.pie(newVals, labels=namelist, autopct='%.0f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('newPiechart.png')
