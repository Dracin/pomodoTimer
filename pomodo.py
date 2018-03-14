import time
import datetime
rep=1
workTime=30*60
breakTime=5*60
print 'Start Working'
while rep<5:
    time.sleep(workTime)
    print datetime.datetime.now().strftime('%H:%M')
    print 'Take 5'
    raw_input('Press Enter to start breaktime')
    time.sleep(breakTime)
    print 'Get back to work'
    print datetime.datetime.now().strftime('%H:%M')
    rep=rep+1
print 'long break' 
