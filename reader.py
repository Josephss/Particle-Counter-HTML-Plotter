
# Author: Joseph Mammo
# Analysis: O(n) ~ has the potential to be improved!
# Current features: - Take in row csv file and hourly and monthly plot the occupied and unoccupied data of the a specific locations

#Import the required libraries
import csv 
from datetime import datetime
import numpy as np
import plotly 
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

#read in the CSV and store it in a huge array
f = open('MetOneAll.csv')
csv_f = csv.reader(f)

csv_srf =[] #Surface IH Office Data
csv_trs = [] # Transition W_D data
csv_crn = [] # LL Cavern NE Corner data
csv_ecntrm = [] # E Count Room NW Corner data
csv_ewall = [] # E Count Room W Wall data
csv_ecntrmm = [] # E Count Room data
csv_dvs = [] # Common Corridor Refrig data
csv_dvs_srt = [] # organized Common Corridor Refrig data -- weekdays from 8 to 5
csv_mdjdrm = [] # MJD Detector Room
csv_mdjmrm = [] # MJD Machine Room
csv_bhsubrm = [] # BHSU Brick Room

#Parameter - location data -> array
for row in csv_f:
    if(row[2] == "Surface IH Office"):
        csv_srf.append(row)
    if(row[2] == "Transition W_D"):
        csv_trs.append(row)
    if(row[2] == "LL Cavern NE Corner"):
        csv_crn.append(row)
    if(row[2] == "E Count Room NW Corner"):
        csv_ecntrm.append(row)
    if(row[2] == "Common Corridor Refrig"):
        csv_dvs.append(row)
    if(row[2] == "E Count Room W Wall"):
        csv_ewall.append(row)
    if(row[2] == "E Count Room"):
        csv_ecntrmm.append(row)
    if(row[2] == "MJD Detector Room"):
        csv_mdjdrm.append(row)
    if(row[2] == "MJD Machine Room"):
        csv_mdjmrm.append(row)
    if(row[2] == "BHSU Brick Room"):
        csv_bhsubrm.append(row)


# -- START ANALYSIS CODE -- #

loc_data_occ = []
loc_data_uocc = []
loc_data = []

def location(loc_num):
    global loc_name # modify the value for the global variable, loc_name
    if(loc_num == 1):
        for row in csv_dvs:
            loc_data.append(row)
        loc_name = "Common Corridor Refrig"
    elif(loc_num == 2):
        for row in csv_crn:
            loc_data.append(row)
        loc_name = "LL Cavern NE Corner"
    elif(loc_num == 3):
        for row in csv_srf:
            loc_data.append(row)
        loc_name = "Surface IH Office"
    elif(loc_num == 4):
        for row in csv_trs:
            loc_data.append(row)
        loc_name = "Transition W_D"
    elif(loc_num == 5):
        for row in csv_ecntrm:
            loc_data.append(row)
        loc_name = "E Count Room NW Corner"
    elif(loc_num == 6):
        for row in csv_ewall:
            loc_data.append(row)
        loc_name = "E Count Room W Wall"
    elif(loc_num == 7):
        for row in csv_ecntrmm:
            loc_data.append(row)
        loc_name = "E Count Room"
    elif(loc_num == 8):
        for row in csv_mdjdrm:
            loc_data.append(row)
        loc_name = "MJD Detector Room"
    elif(loc_num == 9):
        for row in csv_mdjmrm:
            loc_data.append(row)
        loc_name = "MJD Machine Room"
    elif(loc_num == 10):
        for row in csv_bhsubrm:
            loc_data.append(row)
        loc_name = "BHSU Brick Room"
    else:
        print("ERROR: Please input a valid number!")
    # START: Occupied - unoccupied splitter
    for row in loc_data:
        date_object = datetime.strptime(row[0], '%m/%d/%Y %H:%M')
        h = (date_object - date_object.replace(hour=0,minute=0,second=0)).seconds / 3600.
        w = date_object.isocalendar()[1]
        d = date_object.isocalendar()[2]
        if((date_object.weekday() == 5 or date_object.weekday() == 6 and ((w/2 == 2) and d == 0) and ((w/2 != 2) and d == 4)) and (h >=8 and h < 18)):
            loc_data_uocc.append(row)
        else:
            loc_data_occ.append(row)           
    #END: Occupied - unoccupied splitter
    return loc_data
#location(loc) #call and pass the location input


#Hourly Plotter
#inpt_num = int(input("Hourly plotter: Enter 1 for occupied and 2 for unoccupied: ")) # 1 = occupied and 2 = unoccupied
time_grapher_occu = []
time_grapher_unoc = []
time_nor = [8,9,10,11,12,13,14,15,16,17]
time_avg = [] 
def hourly(inpt):
    global title
    del time_grapher_occu[:]
    del time_grapher_unoc[:]
    if(inpt == 1):
        for row in loc_data_occ:
            #print("ESSE")
            time_grapher_occu.append(row)
        title = "Occupied Data"
        grapher(time_grapher_occu)
    elif(inpt == 2):
        #print("========================================================++++++++++++++++++++++==========================")
        for row in loc_data_uocc:
            #print("NOOENO")
            time_grapher_unoc.append(row) 
        title = "Unoccupied Data"
        grapher(time_grapher_unoc)
    return
loccc = []
def grapher(inputtt):
    global time_avg
    del loccc[:]
    for row in time_avg:
        if(float(row)) > 0:
            for row in time_avg:
                del row
    for row in inputtt:
        loccc.append(row)
    e = []
    n = []
    t = []
    el = []
    twl = []
    o = []
    tw = []
    th = []
    fo = []
    fi = []
    
    for row in loccc:
        #print(row)
        date_object = datetime.strptime(row[0], '%m/%d/%Y %H:%M')
        #print(date_object.weekday()) #only 0 - 4 are needed
        h = (date_object - date_object.replace(hour=0,minute=0,second=0)).seconds / 3600.
        if (h == 8):
            e.append(int(row[1]))
        elif (h == 9):
            n.append(int(row[1]))
        elif (h == 10):
            t.append(int(row[1]))        
        elif (h == 11):
            el.append(int(row[1]))
        elif (h == 12):
            twl.append(int(row[1]))
        elif (h == 13):
            o.append(int(row[1]))
        elif (h == 14):
            tw.append(int(row[1]))
        elif (h == 15):
            th.append(int(row[1]))
        elif (h == 16):
            fo.append(int(row[1]))
        elif (h == 17):
            fi.append(int(row[1]))
         
    #if val == nan, enter 0! -- fix
    if(np.mean(e) > 0):
        time_avg.append(np.mean(e))
    else:
        time_avg.append(0)
    if(np.mean(n) > 0):
        time_avg.append(np.mean(n))
    else:
        time_avg.append(0)
    if(np.mean(t) > 0):
        time_avg.append(np.mean(t))
    else:
        time_avg.append(0)
    if(np.mean(el) > 0):
        time_avg.append(np.mean(el))
    else:
        time_avg.append(0)
    if(np.mean(twl) > 0):
        time_avg.append(np.mean(twl))
    else:
        time_avg.append(0)
    if(np.mean(o) > 0):
        time_avg.append(np.mean(o))
    else:
        time_avg.append(0)
    if(np.mean(tw) > 0):
        time_avg.append(np.mean(tw))
    else:
        time_avg.append(0)
    if(np.mean(th) > 0):
        time_avg.append(np.mean(th))
    else:
        time_avg.append(0)
    if(np.mean(fo) > 0):
        time_avg.append(np.mean(fo))
    else:
        time_avg.append(0)
    if(np.mean(fi) > 0):
        time_avg.append(np.mean(fi))
    else:
        time_avg.append(0)
        
   
    # Calculates the average for valid values
    dynamic_avg_time = []
    ctt = 0
    for row in time_avg:
        if (row > 0):
            dynamic_avg_time.append(row)
        else:
            ctt +=1
            
    def caution():
        print("=========================================================================================")
        print(" ")
        print("ATTENTION:" + str(ctt) + " invalid values have been excluded from the average.")
        print(" ")
        print("=========================================================================================")
        return
    if (ctt != 0):
        caution()
        
    #plt.plot(time_nor,time_avg)
    #plt.title(title + " data for " + loc_name + " | avg:" + str(np.mean(dynamic_avg_time)) + " per.5 micro meter/ft^3")
    #plt.ylabel('Particle Count per.5 micro meter/ft^3')
    #plt.xlabel('Time in hours')
    ##plt.legend(" | avg:" + str(np.mean(time_avg)) + " per.5 micro meter/ft^3")
    #patch = mpatches.Patch(color='blue', label='Mean:' + str(np.mean(dynamic_avg_time)) + ' per.5 micro meter/ft^3' + "\n" + 'Median: ' + str(np.median(dynamic_avg_time)) + ' per.5 micro meter/ft^3' + "\n" + 'Max: ' + str(np.max(dynamic_avg_time)) + ' per.5 micro meter/ft^3' + "\n" + " Min: " + str(np.min(dynamic_avg_time)) + ' per.5 micro meter/ft^3')
    #plt.legend(handles=[patch])
    #plt.show()
    #print(time_avg)
    return

#hourly(inpt_num) #call and insert the type input

# Monthly Plotter
#TODO: need to separate data by year!

#inptt_monthly = int(input("Monthly plot: enter 1 for occupied and 2 for unoccupied: "))
monthly_grapher = []
month_nor = [1,2,3,4,5,6,7,8,9,10,11,12]
month_avg = []
mon_title = ""

def monthly(inptt):
    global mon_title
    
    jan = []
    feb = []
    mar = []
    apr = []
    may = []
    jun = []
    jul = []
    aug = []
    sep = []
    octt = []
    nov = []
    dec = []
    
    if(inptt == 1):
        for row in loc_data_occ:
            monthly_grapher.append(row)
            mon_title = "Occupied Data"
    elif(inptt == 2):
        for row in loc_data_uocc:
            monthly_grapher.append(row)
            mon_title = "Unoccupied Data"
            
    for row in monthly_grapher:
        month_object = datetime.strptime(row[0], '%m/%d/%Y %H:%M')
        m = month_object.month
        if(m == 1):
            jan.append(int(row[1]))
        elif(m == 2):
            feb.append(int(row[1]))
        elif(m == 3):
            mar.append(int(row[1]))
        elif(m == 4):
            apr.append(int(row[1]))
        elif(m == 5):
            may.append(int(row[1]))
        elif(m == 6):
            jun.append(int(row[1]))
        elif(m == 7):
            jul.append(int(row[1]))
        elif(m == 8):
            aug.append(int(row[1]))
        elif(m == 9):
            sep.append(int(row[1]))
        elif(m == 10):
            octt.append(int(row[1]))
        elif(m == 11):
            nov.append(int(row[1]))
        elif(m == 12):
            dec.append(int(row[1]))
            
    if(np.mean(jan)):
        month_avg.append(np.mean(jan))
    else:
        month_avg.append(0)
    if(np.mean(feb)):
        month_avg.append(np.mean(feb))
    else:
        month_avg.append(0)
    if(np.mean(mar)):
        month_avg.append(np.mean(mar))
    else:
        month_avg.append(0)
    if(np.mean(apr)):
        month_avg.append(np.mean(apr))
    else:
        month_avg.append(0)
    if(np.mean(may)):
        month_avg.append(np.mean(may))
    else:
        month_avg.append(0)
    if(np.mean(jun)):
        month_avg.append(np.mean(jun))
    else:
        month_avg.append(0)
    if(np.mean(jul)):
        month_avg.append(np.mean(jul))
    else:
        month_avg.append(0)
    if(np.mean(aug)):
        month_avg.append(np.mean(aug))
    else:
        month_avg.append(0)
    if(np.mean(sep)):
        month_avg.append(np.mean(sep))
    else:
        month_avg.append(0)
    if(np.mean(octt)):
        month_avg.append(np.mean(octt))
    else:
        month_avg.append(0)
    if(np.mean(nov)):
            month_avg.append(np.mean(nov))
    else:
        month_avg.append(0)    
    if(np.mean(dec)):
        month_avg.append(np.mean(dec))
    else:
        month_avg.append(0)
    
    # Calculates the average for valid values
    dynamic_avg = []
    ct = 0
    for row in month_avg:
        if (row > 0):
            dynamic_avg.append(row)
        else:
            ct +=1
            
    def caution_month():
        print("=========================================================================================")
        print(" ")
        print("ATTENTION:" + str(ct) + " invalid values have been excluded from the average.")
        print(" ")
        print("=========================================================================================")
        return
    if (ct != 0):
        caution_month()
        
        
    #plt.plot(month_nor,month_avg)
    #plt.title(mon_title + " data for " + loc_name + " | avg:" + str(np.mean(dynamic_avg)) + " per.5 micro meter/ft^3")
    #plt.ylabel('Particle Count per.5 micro meter/ft^3')
    #plt.xlabel('Months')
    ##patch = mpatches.Patch(color='blue', label='avg:' + str(np.mean(dynamic_avg)) + ' per.5 micro meter/ft^3')
    #patch = mpatches.Patch(color='blue', label='Mean:' + str(np.mean(dynamic_avg)) + ' per.5 micro meter/ft^3' + "\n" + 'Median: ' + str(np.median(dynamic_avg)) + ' per.5 micro meter/ft^3' + "\n" + 'Max: ' + str(np.max(dynamic_avg)) + ' per.5 micro meter/ft^3' + "\n" + " Min: " + str(np.min(dynamic_avg)) + ' per.5 micro meter/ft^3')
    #plt.legend(handles=[patch])
    #plt.show()
    return month_avg

#monthly(inptt_monthly)
# -- END ANALYSIS CODE -- #


def html_plot(num):
    location(num)
    
    hourly_occ = []
    hourly_unocc = []
    monthly_occ = []
    monthly_unocc = []
    
    hourly(1)
    for row in time_avg:
        hourly_occ.append(row)
    h_occ_title = title
    del time_grapher_occu[:]
    del time_grapher_unoc[:]  
    del time_avg[:]
    hourly(2)
    for row in time_avg:
        hourly_unocc.append(row)
    h_unocc_title = title
    monthly(1)
    for row in month_avg:
        monthly_occ.append(row)
    m_occ_title = mon_title
    del monthly_grapher[:]
    del month_avg[:]
    monthly(2)
    for row in month_avg:
        monthly_unocc.append(row)
    m_unocc_title = mon_title
    #plot the data on an HTML page
    trace0 = go.Scatter(
        x=time_nor, y=hourly_occ, name = 'Hourly ' + h_occ_title
    )
    trace1 = go.Scatter(
        x=time_nor, y=hourly_unocc, name = 'Hourly ' + h_unocc_title
    )
    trace2 = go.Scatter(
      x=month_nor, y=monthly_occ, name = 'Monthly ' + m_occ_title,
    )
    trace3 = go.Scatter(
      x=month_nor, y=monthly_unocc, name = 'Monthly ' + m_unocc_title,
    )
    fig = tools.make_subplots(rows=2, cols=2)
    
    fig.append_trace(trace0, 1, 1)
    fig.append_trace(trace1, 1, 2)
    fig.append_trace(trace2, 2, 1)
    fig.append_trace(trace3, 2, 2)
    
    fig['layout'].update(title= title + ' and ' + mon_title + ' plot of ' + loc_name)
    plotly.offline.plot(fig, filename = loc_name + ".html")
    return
#Test
#html_plot(2)
#html_plot(8)
#html_plot(10)

info = '1 = Davis Campus Common Corridor; 2 = LL Cavern NE Corner; 3 = Surface IH Office; 4 = Transition W_D; 5 = E Count Room NW Corner; 6 = E Count Room W Wall; 7 = E Count Room; 8 = MJD Detector Room; 9 = MJD Machine Room; 10 = BHSU Brick Room'
print(info)
plotInput = int(input("Enter a number from 1 - 10: ")) # 1 = csv_dvs, 2 = csv_crn, 3 = csv_srf, 4 = csv_trs, 5 = csv_ecntrm, 6 = csv_ewall, 7 = csv_ecntrmm
html_plot(plotInput)