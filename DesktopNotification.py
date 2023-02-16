#install module/package
#pip install pyler

#import the package
from plyer import notification

#Specift the parameters
title = 'Hello Amazing Learners'
message = 'Do subscribe my channel! Thank you!!'

notification.notify(title= title, message= message, app_icon= None, timeout= 10, toast= False)