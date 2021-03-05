# Author: Adebayo Abiodun Jayson
# twitter: @jay_b_jayson
# https://jaysons.netlify.app




#pip3 install speedtest-cli
import speedtest

#function that gets the download speed in mega bytes per second
def get_final_speed():
    rawspeed = speedtest.Speedtest().download()
    roundedspeed = round(rawspeed)
    finalspeed = roundedspeed / 1e+6
    return finalspeed

#function that finds the average downloadspeed in mega bytes a second
def looped_av(y):
    finalspeeds = 0
    for i in range(y):
        x = get_final_speed()
        speeds = 0
        count = 0
        count += 1
        speeds += x
        print(f'{i+1}. {x}mb/s')
        

#menu loop
while True:
    repeat = input('1, 2, 3 or press {ENTER} to quit\n>>>')
    if repeat == '1':
        #single iteration
        x = get_final_speed()
        print(f'done, your download speed is {x}mb/s')
    elif repeat == '2':
        #2 iterations and finds the average speed
        x = looped_av(2)
        print(f'done, your average download speed is {x}mb/s')
    elif repeat == '3':
        #finds out how accurate the user wants the average to be, pretty pointless i know
        times_through = int(input('how many times do you want the test to run?\n>>>'))
        #iterates and finds the average download speed
        x = looped_av(times_through) 
    else:
        #breaks from the loop
        break

