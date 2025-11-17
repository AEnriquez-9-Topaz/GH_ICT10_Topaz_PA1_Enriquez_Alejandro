# Working with sets
from pyscript import display, document


Social_Studies_Club = {'Alisa', 'Boby', 'Charlies', 'Dian'} # Students in SS Club
Math_Club = {'Charlies', 'Dian', 'Eve', 'Frank'} # Students in Math Club

display(f'Those in social studies club: {Social_Studies_Club}', 
        target='SS club') #Display SS Club members
display (f'Those in math club: {Math_Club}', 
        target='Math club') #Display Math Club members


display(Social_Studies_Club | Math_Club, target='output1') #Union, who are students in at least one club
display(Social_Studies_Club & Math_Club, target='output2') #Intersection, who are in both clubs
display(Social_Studies_Club - Math_Club, target='output3') #Difference, who are only in SS Club
display(Math_Club - Social_Studies_Club, target='output4') #Difference, who are only in Math Club
display(Social_Studies_Club ^ Math_Club, target='output5') #Symmetric Difference, who are in only one club

