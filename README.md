This code is part of the app my team made for Praxis Engineering to implement efficiencies in scheduling work/meetings 
using the employees' calendars, locations, emails, and other information.

The code uses Flutter's Geolocation package to record the user's location every ten minutes and send the data to Firebase's Realtime Database 
for cost-effective data storage. Then it creates groups of employees using k-means clustering to identify employees who are in close proximity of
each other. This is especially useful for employees who visit/work at multiple branches on different days of the week.
