#A countdown-timer
import time



def Countdown(t):
    while(t>0):
        #divmod returns the quotient and remainder of the specified input.
        mins,secs=divmod(t,60)

        #the time format for printing the time. 
        timer="{:02d}:{:02d}".format(mins,secs)
        print(timer,"\n")
        t-=1
        
        #To wait briefly.
        time.sleep(1)
    print("The specified duration has ended!")

# Main program
print("Ready? Please give the duration:")
dur=input()
Countdown(int(dur))


    







