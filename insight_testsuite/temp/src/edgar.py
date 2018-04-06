import sys
"""
Created on Fri Apr  6 02:40:01 2018
Python (3.6) code for reading CSV file and writing to disk.
@author: achindha@andrew.cmu.edu (Aditya Chindhade)
"""
#if (len(sys.argv) == 1):
#    infile = open('../input/log.csv', 'r')
#    timefile = open('../input/inactivity_period.txt', 'r')
#    outfile = open('../output/sessionization.txt', 'w')
#else:
infile = open(sys.argv[1], 'r')
timefile = open(sys.argv[2], 'r')
outfile = open(sys.argv[3], 'r')
    
inact_time = int(timefile.readline())

lno = 0
ipdict = dict()
nonempty = 0

def toSeconds(date, time):
    yy,mm,dd = date.split('-')
    h,m,s = time.split(':')
    yy = int(yy)
    mm = int(mm)
    dd = int(dd)
    h = int(h)
    m = int(m)
    s = int(s)
    days = (yy % 2000 * 365) + (mm * 12) + dd
    seconds = 3600 * h + 60 * m + s
    time = days * 86400 + seconds
    return time

for line in infile:
    lno += 1
    if (lno > 1):
        nonempty = 1 #File contains at least 1 data row.
        linelist = line.split(',')
        ip = linelist[0]
        date = linelist[1]
        time = linelist[2]
        cik = linelist[4]
        accession = linelist[5]
        extention = linelist[6]
        arr = []
        #calculate value of current time in seconds.
        currtime = toSeconds(date, time)
        
        if (ipdict.get(ip) == None):
            numdocs = 1
            ipdict.update({ip: [date, time, date, time, cik, accession, extention, currtime, numdocs]})
            
        else:
            tmp = ipdict.get(ip)
            tmp[2] = date
            tmp[3] = time
            tmp[7] = currtime 
            tmp[8] += 1
            ipdict.update({ip: tmp})
        
        for ipold in ipdict:
            indate = ipdict.get(ipold)[0]
            intime = ipdict.get(ipold)[1]
            outdate = ipdict.get(ipold)[2]
            outtime = ipdict.get(ipold)[3]
            outtimesecs = ipdict.get(ipold)[7]
            docnum = ipdict.get(ipold)[8]
            duration =  toSeconds(outdate, outtime) - toSeconds(indate, intime) + 1
            inactivity = currtime - outtimesecs
            
            if ((inactivity > inact_time)):
                print(ipold,',',indate,' ',intime,',',outdate,' ',outtime,',',duration,',',docnum, file = outfile, sep = '')
                arr.append(ipold)
                
        for ips in arr:
            ipdict.pop(ips)
            
if (nonempty == 1):
    arr = []
    for ipold in ipdict:
        indate = ipdict.get(ipold)[0]
        intime = ipdict.get(ipold)[1]
        outdate = ipdict.get(ipold)[2]
        outtime = ipdict.get(ipold)[3]
        outtimesecs = ipdict.get(ipold)[7]
        docnum = ipdict.get(ipold)[8]
        duration =  toSeconds(outdate, outtime) - toSeconds(indate, intime) + 1
        inactivity = currtime - outtimesecs
        print(ipold,',',indate,' ',intime,',',outdate,' ',outtime,',',duration,',',docnum, file = outfile, sep = '')
        arr.append(ipold)
    for ips in arr:
        ipdict.pop(ips)
                
        