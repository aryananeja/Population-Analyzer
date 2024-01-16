# This code analyses and plots the population data of US states. 
# Written by Aryan Aneja

import matplotlib.pyplot as plt
import random

# list to store the data
data = []  

# opens and stores the data into lists  
f = open("data.csv")
for line in f:
  row = line.split(",")
  row = list(row)
  data.append(row)

# lists for different populations
tot_grid = []
w_grid = []
b_grid = []
a_grid = []
i_grid = []
states = []
row = 1

# Loop through the 50 states 
for i in range(50):
  # each race populations for 10 year in each state
  tot_pop = [0 for i in range(0,10)]
  w_pop= [0 for i in range(0,10)]  
  b_pop= [0 for i in range(0,10)]
  a_pop= [0 for i in range(0,10)]
  i_pop= [0 for i in range(0,10)]

  # the state heading 
  name = data[row][4]
  
  states.append(name)

  #loop through all the rows and check for the state name
  # breaks when a new state comes up and each race population categories are added
  # for each year
  while row <= 31410 and data[row][4] == name:
    year = int(data[row][6])
    tot_pop[year-2010] += int(data[row][7])
    w_pop[year-2010] += int(data[row][8])
    b_pop[year-2010] += int(data[row][9])
    a_pop[year-2010] += int(data[row][10])
    i_pop[year-2010] += int(data[row][11])
    row += 1

  # values appended to the original lists
  tot_grid.append(tot_pop)
  w_grid.append(w_pop)
  b_grid.append(b_pop)
  a_grid.append(a_pop)
  i_grid.append(i_pop)

# X values for the plots
years = [i for i in range(2010,2020)]

# Y values for plot1
highpop = []
lowpop = []

# Y values for plot2
democratic = []
republic = []

# data list for plot 1 y axis
high_populations = ['California','Texas','Florida','New York','Pennsylvania']
low_populations = ['Wyoming','Vermont','Alaska','North Dakota','South Dakota']

# data list for plot 2 y axis
democratic_states = ['Hawaii','Vermont','California','Maryland','Massachusetts']
republic_states =['Wyoming','Utah','Oklahoma','West Virginia','Idaho']

# Loop through the 10 years and add the total population for high population states defined for each year 
for year in range(10):
  total = 0
  for state in high_populations:
    total += tot_grid[states.index(state)][year]
  highpop.append(total)

# loop through the 10 years and add the total population for low population states defined for each year 
for year in range(10):
  total = 0
  for state in low_populations:
    total += tot_grid[states.index(state)][year]
  lowpop.append(total)

fig=plt.figure()

# Subplot 1 for plot1
fig.add_subplot(121)
plt.plot(years, highpop, '--ro')
plt.xlabel("Years")
plt.ylabel("Population Growth")
plt.title('High Pop States')
plt.grid()

# Subplot 2 for plot1
fig.add_subplot(122)
plt.plot(years, lowpop, '--bo')
plt.xlabel("Years")
plt.title('Low Pop States')
plt.grid()

plt.savefig('plot1.png', dpi = 700)
plt.clf()


# loop through 10 years and add black population for each year for democratic states stored in 
for year in range(10):
  total = 0
  for state in democratic_states:
    total += b_grid[states.index(state)][year]
  democratic.append(total)

# loop through 10 years and add black population for each year for republican states stored in list
for year in range(10):
  total = 0
  for state in republic_states:
    total += b_grid[states.index(state)][year]
  republic.append(total)

# Subplot 1 for plot2
fig.add_subplot(1,2,1)
plt.plot(years, democratic, '--ro')
plt.xlabel("Years")
plt.title('Democratic States')
plt.ylabel("Population Growth")
plt.grid()

# Subplot 2 for plot2
fig.add_subplot(1,2,2)
plt.plot(years, republic, '--bo')
plt.title('Republic States')
plt.xlabel("Years")
plt.grid()
plt.savefig('plot2.png', dpi = 700)
plt.clf()

# data list for pie
pieplot = ['White Population','Black Population','Asian Population','Indian Population']

# Variables for 1st pie chart 
B_2010_people = 0
W_2010_people = 0
A_2010_people = 0
I_2010_people = 0

# variables for 2nd pie chart
B_2019_people = 0
W_2019_people = 0
A_2019_people = 0
I_2019_people = 0

# sum up the total population for all states year 2010
for row in range(len(data)):
  if data[row][6] == "2010":
    W_2010_people += int(data[row][7])
    B_2010_people += int(data[row][8])
    A_2010_people += int(data[row][9])
    I_2010_people += int(data[row][10]) 

# First pie chart
fig.add_subplot(1,2,1)
vals1_pie = [W_2010_people, B_2010_people, A_2010_people, I_2010_people]
pie_labels = ['White','Black','Asian','Indian']
colors = ['Red','Green','Cyan','Yellow']
plt.style.use('ggplot')
plt.title('Total Population in 2010')
plt.pie(vals1_pie, autopct = '%.2f',labels = pie_labels, shadow = False, startangle = 0, colors = colors)
circle = plt.Circle(xy=(0,0), radius = .75, facecolor = 'white')
plt.gca().add_artist(circle)
plt.savefig('pie.png', dpi = 700)

# sum up the total population for all states in year 2019
for row in range(len(data)):
  if data[row][6] == "2019":
    W_2019_people += int(data[row][7])
    B_2019_people += int(data[row][8])
    A_2019_people += int(data[row][9])
    I_2019_people += int(data[row][10]) 

# Second pie chart
vals2_pie = [W_2019_people, B_2019_people, A_2019_people, I_2019_people]
fig.add_subplot(1,2,2)
plt.title('Total Population in 2019')
plt.pie(vals2_pie, autopct = '%.2f',labels = pie_labels, colors = colors, startangle = 0)
plt.savefig('pie.png', dpi = 700)
