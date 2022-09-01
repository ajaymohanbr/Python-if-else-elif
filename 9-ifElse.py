
# How to import time

from datetime import datetime
time = datetime.now().hour  #Change the number here to test different results.
#------------------------------------

if time >=0 and time <12:
    print('Bom dia!')

elif time >=12 and time <18:
    print('Boa Tarde!')

else:
    print('Boa noite!')

#print('This will be executed anyway since it´s not indented with the line')
