'''Countdown Calendar'''

from datetime import date, datetime
from tkinter import Tk, Canvas

#Function reads events from events file
def read_event_list():
    #Empty list to store event name and date
    event_list = []
    #Open event file
    with open('Events.txt') as file:
        for line in file:
            #Removing the new line character
            line = line.strip('\n')
            #Split each event at comma
            current_event = line.split(',')
            #Get event date string and convert to datetime format
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            #Pass new event date back to current event index
            current_event[1] = event_date
            #Append current event list to event list
            event_list.append(current_event)

    return event_list #return event list to function

#Function calculates difference between two dates
def difference_between_dates(date1, date2):
    date_difference = str(date1 - date2)
    number_of_days = date_difference.split(' ')
    days_until_event = number_of_days[0]
    return days_until_event

#Load the Tkinter window
root = Tk()
#Create canvas to display results
c = Canvas(root, width=500, height=350, bg='white')
#Pack canvas into Tkinter window
c.pack()

title_text = 'COUNTDOWN CALENDAR'
#Add text to canvas
c.create_text(100, 50, anchor='w', fill='black',font='Arial 15 bold underline', text=title_text)

#Getting the day's date
today = date.today()
#Passing function to event list variable
event_list = read_event_list()
#Sort event list from 
event_list.sort(key=lambda x: x[1])
vertical_space = 100
for event in event_list:
    event_name = event[0]
    event_date = event[1]
    time_until_event = difference_between_dates(event_date, today)
    display = 'It is %s days until %s' % (time_until_event, event_name)
    
    if int(time_until_event) <= 7:
        text_col = 'red'
    else:
        text_col = 'blue'
    
    c.create_text(100, vertical_space, anchor='w', fill=text_col, font='Courier 10 bold', text=display)
    vertical_space = vertical_space + 30

root.mainloop()