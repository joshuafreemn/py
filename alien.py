alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#dictionary with one key-value pair
alien_1 = {'color': 'blue'}

print(alien_1['color'])

#lookup points of alien_0
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#adding to exsiting dictionarys
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#starting w/ an empty list
alien_2 = {}

alien_2['color'] = 'pink'
alien_2['points'] = 20
print(alien_2)

#starting w/ empty dictionary
alien_3 = {}

alien_3['color'] = 'yellow'
alien_3['points'] = '44'

print(alien_3)

#modyfiing values
print("The alien is " + alien_3['color'] + ".")
alien_3 = {'color': 'orange'}
print("The alien is now " + alien_3['color'] + ".")

#removing key-value pairs
del alien_0['x_position']
del alien_0['y_position']
print(alien_0)