import os
import epd4in2
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
from todoist_api_python.api import TodoistAPI
import time

####### Todoist API code
api = TodoistAPI("fa46b6d656c8cf7cdf54ee9ad099599e9a53061d")

font21 = ImageFont.truetype('Font.ttc', 21)
font28 = ImageFont.truetype('Font.ttc', 28)
font32 = ImageFont.truetype('Font.ttc', 32)

# Drawing on the Vertical image
epd = epd4in2.EPD()
Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Limage)

def display_base():
    print("Creating Display Base")
    
    #Print to display here
    epd.init()
    epd.Clear()

    #draw page border
    draw.rectangle((0,0,300,400), fill = 0)
    draw.rectangle((3,3,296,396), fill = 1)
                
    #date rectangle for date
    draw.rectangle((0,355,300,400), fill = 0) 

    #draw page lines
    draw.line((0, 40, 300, 40), fill = 0) #Title underlined draw line (x start, y start, x end, y end)
    draw.line((230, 40, 230, 400), fill = 0) # due dates section

    #due title
    draw.text((235, 3), 'Due', font = font32, fill = 0)
                
    # Todays Date
    now = datetime.now()
    draw.text((5, 360), now.strftime("%A %d %b"), font = font28, fill = 1)
    print("display created")

def display_current():
    print("Updating Tasks")
             
    #draw title
    draw.text((5, 3), 'To Do List', font = font32, fill = 0)
                
    #draw contents
    x_start_content = 7
    y_start_content = 45 
    due_content_reduced = [elem[:19] for elem in due_content]
    for i in due_content_reduced:
        if len(i) >= 19:
            i = i + "..."
        draw.text((x_start_content, y_start_content), i, font = font21, fill = 0)  #First task
        y_start_content += 30
    
    #draw date
    x_start_dates = 7
    y_start_dates = 45
    for n in due_date:
        draw.text((x_start_dates + 226, y_start_dates), n, font = font21, fill = 0)  #First task
        y_start_dates += 30

    epd.display(epd.getbuffer(Limage))

def display_future():

    print("No More Tasks Today")
    print("Showing tasks for the next 7 days")
                
    #draw title
    draw.text((5, 3), 'Next 3 Days', font = font32, fill = 0)
                          
    #draw contents
    x_start_content = 7
    y_start_content = 45
    future_content_reduced = [elem[:19] for elem in future_content]
    for i in future_content_reduced:
        if len(i) >= 19:
            i = i + ".."
        draw.text((x_start_content, y_start_content), i, font = font21, fill = 0)  #First task
        y_start_content += 30
    
    #draw date
    x_start_dates = 7
    y_start_dates = 45
    for n in future_date:
        draw.text((x_start_dates + 226, y_start_dates), n, font = font21, fill = 0)  #First task
        y_start_dates += 30

    epd.display(epd.getbuffer(Limage))
    
    
    

######## Starting Code ##########
data_test = []
result = None ### Keeps code trying to run
while result is None:
    try: 
        data = sorted(api.get_tasks(filter='Overdue | 3days'), key=lambda t: t.due.date)
        tasks = [task.content for task in data]
        dates = [task.due.date for task in data]
        due_date, future_date = [],[]

        for x in dates:
            x = datetime.strptime(x, '%Y-%m-%d')
            if x.date() <= datetime.today().date():
                due_date.append(x.strftime('%a-%d'))
            if x.date() > datetime.today().date():
                future_date.append(x.strftime('%a-%d'))
 
        due_content = tasks[0:len(due_date)]
        future_content = tasks[len(due_date):len(due_date + future_date)]
    
        if data != data_test: 
            display_base()
            if len(due_content) == 0:
                display_future()
                print("Future tasks updated")
            else:
                print("showing current display")
                display_current()
                print("Current tasks updated")
            data_test = data 
        time.sleep(20)
        
    except:
        print("Error")
        time.sleep(5)
        pass
