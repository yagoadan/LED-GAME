
#LIBRARIES
import random           #Library to make random selection
import math             #Library that imports maths equations
import opc              #Library to led on the leds for (readopcForStrands)
import colorsys         #library to switch colours
import time             #Library to create pauses, time how long it takes use the program or even tell the user the actual time
import sys              #Library to access some variables used or maintained by the interpreter
import numpy            #Library that contains a multi-dimensional array and matrix data structures
from time import sleep  #From library Time I imported sleep so I can pause parts of the codes, giving it a break
import re
from playsound import playsound     #Library to play sounds such as mp3

#DRAWINGS
mainmenu = '''
                           OPTIONS
                 ___________________________
                |                            |
                |       1. Fading            |
                |       2. Guess             |
                |       3. DBZ               |
                |       4. Animation         |
                |       5. Morse             |
                |       6. Description       |
                |       7. Exit              |
                |____________________________|

'''

#This is a way of showing ASCII on the code. Whenever a type print(mainmenu) it will show this "OPTIONS"

colour_list = '''
                         COLOURS
                 _______________________
                |                       |
                |       1. Red          |
                |       2. Blue         |
                |       3. Green        |
                |       4. Yellow       |
                |       5. Orange       |
                |       6. Purple       |
                |       7. White        |
                |       8. Black        |
                |       9. Random       |
                |_______________________|
'''

#Similarly to mainmenu I did the same thing for "COLOURS" so the user knows what he has to input

guess = '''
                            GUESSING GAME
                 _____________________________________
                |                                     |
                |   1. (Number) -  Guess the number   |
                |   2. (Colour) -  Guess the colour   |
                |_____________________________________|
                
'''

anim = '''
                               ANIMATION
                 _____________________________________
                |                                     |
                |            1. Basic                 |
                |            2. Forest                |
                |_____________________________________|
                
'''

#Finally, the same option structure for the "GUESS GAME"


#VARIABLES
client = opc.Client('localhost:7890')
rdm = random.randint(0, 255)
led_list = [(0, 0, 0)]*360      #Make a tuple inside a list with the values for the leds and times it by 360 to show all leds
#This are all my main variables that will help me across the entire code


#DICTIONARY
colours = {'blue': (0, 0, 255),
           'red': (255, 0, 0),
           'green': (0, 255, 0),
           'yellow': (248, 252, 3),
           'orange': (252, 148, 3),
           'purple': (252, 3, 252),
           'white': (255, 255, 255),
           'black': (0, 0, 0),
           'random': (rdm, rdm, rdm)
           }


                 

#This is a dictionary, it will allow the user and me to pick a colour for some of the future funtions. This will allow the program to know that if I type someting such as 'green' it will get the (0, 255, 0), knowing that it needs to display the green colour


#DEFINE FUNCTIONS
def delay_word(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
#This function reads a word and displays them letter by letter with a time of 0.05 seconds per letter. In order to create a more visual expresion for when reading the text
        
def end():
    print('Thanks for using this code')
    exit(0)
#This is a fuction that close the program for whenever the user wants to stop

def right2(colour1):
    for x in range(0, 360):
        led_list[x] = (colours.get(colour1))
        client.put_pixels(led_list)
        time.sleep(0.001)
#Animates the leds starting from led 0 to led 359
#Allows the user to choose a colour
#Sends a signal to the client so it can be displayed
            
def snake_both(colour1, colour2, incre):
    for x in range(0, 180, incre):
        led_list[x] = (colours.get(colour1))
        led_list[359 - x] = (colours.get(colour2))
        client.put_pixels(led_list)
        time.sleep(0.001)
#Similar to the define function right2, the only difference is that it displays the leds going from led 0 to 180 and led 360 to led 180
#There are 2 colours to be input
        
def left(colour1):
    for x in range(0, 360):
        led_list[359-x] = (colours.get(colour1))
        client.put_pixels(led_list)
        time.sleep(0.001)
#Animates the leds starting from led 359 to 0
#Allows the user to choose a colour
#Sends a signal to the client so it can be displayed
        
def right3(colour1, incre):
    for x in range(0, 360, incre):
        led_list[x] = (colours.get(colour1))
        client.put_pixels(led_list)
        time.sleep(0.001)
#Goes the same direction as right2 but it skips "x" amount of leds as it can go every 2 leds or every 3 leds etc

def yago(colour1):
    for x in range(0, 360):
        #This is Y
        led_list[76] = (colours.get(colour1))
        led_list[79] = (colours.get(colour1))
        led_list[136] = (colours.get(colour1))
        led_list[137] = (colours.get(colour1))
        led_list[138] = (colours.get(colour1)) 
        led_list[139] = (colours.get(colour1))
        led_list[199] = (colours.get(colour1))
        led_list[259] = (colours.get(colour1))
        led_list[258] = (colours.get(colour1))
        led_list[257] = (colours.get(colour1)) 
        led_list[256] = (colours.get(colour1))
        #This is A
        led_list[85] = (colours.get(colour1))
        led_list[144] = (colours.get(colour1))
        led_list[146] = (colours.get(colour1)) 
        led_list[202] = (colours.get(colour1))
        led_list[203] = (colours.get(colour1))
        led_list[204] = (colours.get(colour1))
        led_list[205] = (colours.get(colour1))
        led_list[206] = (colours.get(colour1))
        led_list[207] = (colours.get(colour1))
        led_list[208] = (colours.get(colour1))
        led_list[263] = (colours.get(colour1))
        led_list[267] = (colours.get(colour1))
        #This is G
        led_list[91] = (colours.get(colour1))
        led_list[92] = (colours.get(colour1))
        led_list[93] = (colours.get(colour1))
        led_list[94] = (colours.get(colour1))
        led_list[151] = (colours.get(colour1))
        led_list[211] = (colours.get(colour1))
        led_list[213] = (colours.get(colour1))
        led_list[214] = (colours.get(colour1))
        led_list[271] = (colours.get(colour1))
        led_list[272] = (colours.get(colour1))
        led_list[273] = (colours.get(colour1))
        led_list[274] = (colours.get(colour1))
        #This is O
        led_list[97] = (colours.get(colour1))
        led_list[98] = (colours.get(colour1))
        led_list[99] = (colours.get(colour1))
        led_list[100] = (colours.get(colour1))
        led_list[101] = (colours.get(colour1))
        led_list[157] = (colours.get(colour1))
        led_list[161] = (colours.get(colour1))
        led_list[217] = (colours.get(colour1))
        led_list[221] = (colours.get(colour1))
        led_list[277] = (colours.get(colour1))
        led_list[278] = (colours.get(colour1))
        led_list[279] = (colours.get(colour1))
        led_list[280] = (colours.get(colour1))
        led_list[281] = (colours.get(colour1))
        client.put_pixels(led_list)
        time.sleep(0.05)
#This funtion displays my name in one of the animations
        
def rainbow(colour1):
    s = 1.0
    v = 1.0
    for hue in range(360):
        rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v) 
        r_float = rgb_fractional[0]
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float*255, g_float*255, b_float*255) 
        client.put_pixels([rgb]*360)
        time.sleep(0.01)
#From a colour, it will rotate 360 degrees and come back to the same colour while fading different colours thrughout the whole process      
#Colorsys returns floats between 0 and 1
#Extract said floating point numbers
#Extract said floating point numbers
        
def blinking(colour1):
    for x in range(0, 360):
        led_list[180 - x] = (colours.get(colour1))
        for i in range(2):
            x = numpy.roll(x,3)
        client.put_pixels(led_list)
        time.sleep(0.01)
#Blinks leds by switching the position
        
def flash(colour1):
    for x in range(0, 1):
        led_list = [(colours.get('black'))]*360
        time.sleep(0.01)
        client.put_pixels(led_list)
        led_list = [(colours.get(colour))]*360
        client.put_pixels(led_list)
        time.sleep(0.01)
        
def all_leds(colour1):
    led_list = (colours.get(colour1))
    client.put_pixels([led_list]*360)
    time.sleep(0.01)
#Changes all leds to a specific colour
    
def allblack():
    led_list = (0, 0, 0)
    client.put_pixels([led_list]*360)
    time.sleep(0.001)
#Changes all leds to black but the time to be display is really fast. This is because it will be used for another function

def allwhite():
    led_list = (255, 255, 255)
    client.put_pixels([led_list]*360)
    time.sleep(0.001)
#Similar to allblack() this will be used for a different function

def flashy():
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
    allblack()
    allwhite()
#Keeps changing between the allblack function and the all white function in order to create a flash animation

def blackmorse():
    led_list = (71, 70, 69)   #This led represents the dot
    client.put_pixels([led_list]*360)
    time.sleep(0.1)
    
def blackm():
    led_list = (0, 0, 0)  
    client.put_pixels([led_list]*360)
    time.sleep(0.05)

def whitemorse():
    led_list = (255, 255, 255) #This led represents the dash 
    client.put_pixels([led_list]*360)
    time.sleep(0.3)
#Shows a white colour for the morse animation
    
def morsemain(word):
    letterSpace = "..."
    wordSpace = "......."
    allblack()
    client.put_pixels(led_list)
    print("It is going to display all the letters first and after the red screen is gone that's when your encrypted word starts. ")    

    morsecode = {'a': (blackmorse(),blackm(), whitemorse()),
                 'b': (whitemorse(),blackm(), blackmorse(), blackmorse(), blackmorse()),
                 'c': (whitemorse(),blackm(), blackmorse(),blackm(), whitemorse(),blackm(), blackmorse()),
                 'd': (whitemorse(), blackmorse(), blackmorse()),
                 'e': (blackmorse()),
                 'f': (blackmorse(), blackmorse(), whitemorse(), blackmorse()),
                 'g': (whitemorse(), whitemorse(), blackmorse()),
                 'h': (blackmorse(), blackmorse(), blackmorse(), blackmorse()),
                 'i': (blackmorse(), blackmorse()),
                 'j': (blackmorse(), whitemorse(), whitemorse(), whitemorse()),
                 'k': (whitemorse(), blackmorse(), whitemorse()),
                 'l': (blackmorse(), whitemorse(), blackmorse(), blackmorse()),
                 'm': (whitemorse(), whitemorse()),
                 'n': (whitemorse(), blackmorse()),
                 'o': (whitemorse(), whitemorse(), whitemorse()),
                 'p': (blackmorse(), whitemorse(), whitemorse(), blackmorse()),
                 'q': (whitemorse(), whitemorse(), blackmorse(), whitemorse()),
                 'r': (blackmorse(), whitemorse(), blackmorse()),
                 's': (blackmorse(), blackmorse(), blackmorse()),
                 't': (whitemorse()),
                 'u': (blackmorse(), blackmorse(), whitemorse()),
                 'v': (blackmorse(), blackmorse(), blackmorse(), whitemorse()),
                 'w': (blackmorse(), whitemorse(), whitemorse()),
                 'x': (whitemorse(), blackmorse(), blackmorse(), whitemorse()),
                 'y': (whitemorse(), blackmorse(), whitemorse(), whitemorse()),
                 'z': (whitemorse(), whitemorse(), blackmorse(), blackmorse()),
                 '1': (blackmorse(), whitemorse(), whitemorse(), whitemorse(), whitemorse()),
                 '2': (blackmorse(), blackmorse(), whitemorse(), whitemorse(), whitemorse()),
                 '3': (blackmorse(), blackmorse(), blackmorse(), whitemorse(), whitemorse()),
                 '4': (blackmorse(), blackmorse(), blackmorse(), blackmorse(), whitemorse()),
                 '5': (blackmorse(), blackmorse(), blackmorse(), blackmorse(), blackmorse()),
                 '6': (whitemorse(), blackmorse(), blackmorse(), blackmorse(), blackmorse()),
                 '7': (whitemorse(), whitemorse(), blackmorse(), blackmorse(), blackmorse()),
                 '8': (whitemorse(), whitemorse(), whitemorse(), blackmorse(), blackmorse()),
                 '9': (whitemorse(), whitemorse(), whitemorse(), whitemorse(), blackmorse()),
                 '0': (whitemorse(), whitemorse(), whitemorse(), whitemorse(), whitemorse()) }

    print(all_leds('red'))
    time.sleep(1)
    client.put_pixels(led_list)
    
    switch = ""
    
    for i in list(word):
        switch = morsecode.get(i)
        client.put_pixels(led_list)
    return switch
                
    '''
    decrypt = {v: k for k, v in morsecode.items()}
    if '-' in word:
        return ''.join(decrypt[str(i)] for i in word.split())
    return ' '.join(morsecode[i] for i in word.lower())
    '''
    

    
def forest_base():
#Base
    for y in range(0, 60):
    #Chages the first 5 led stripes to baby blue and the last one to brown
        #Sky
        led_list[y] = (5, 242, 230)
        led_list[60 + y] = (5, 242, 230)
        led_list[120 + y] = (5, 242, 230)
        led_list[180 + y] = (5, 242, 230)
        led_list[240 + y] = (5, 242, 230)

        #Ground
        led_list[300 + y] = (34, 112, 26)
        
        client.put_pixels(led_list)
        time.sleep(0.05)
        
def central_forest():
    for l in range(0, 120, 5):
        led_list[183 + l] = (130, 92, 4)
        led_list[184 + l] = (130, 92, 4) 
        client.put_pixels(led_list)
        time.sleep(0.001)

    for b in range(0, 27, 5):
        led_list[62 + b] = (20, 181, 5)
        led_list[63 + b] = (20, 181, 5)
        led_list[64 + b] = (20, 181, 5)
        led_list[65 + b] = (20, 181, 5)
        led_list[92 + b] = (20, 181, 5)
        led_list[93 + b] = (20, 181, 5)
        led_list[94 + b] = (20, 181, 5)
        led_list[95 + b] = (20, 181, 5)
        led_list[122 + b] = (20, 181, 5)
        led_list[123 + b] = (20, 181, 5)
        led_list[124 + b] = (20, 181, 5)
        led_list[125 + b] = (20, 181, 5)
        led_list[152 + b] = (20, 181, 5)
        led_list[153 + b] = (20, 181, 5)
        led_list[154 + b] = (20, 181, 5)
        led_list[155 + b] = (20, 181, 5)
        client.put_pixels(led_list)
        time.sleep(0.001)
        
    for s in range(0, 240, 60):
        led_list[60 + s] = (5, 242, 230)
        led_list[61 + s] = (5, 242, 230)
        led_list[117 + s] = (5, 242, 230)
        led_list[118 + s] = (5, 242, 230)
        led_list[119 + s] = (5, 242, 230)
        led_list[87 + s] = (5, 242, 230)
        led_list[88 + s] = (5, 242, 230)
        led_list[89 + s] = (5, 242, 230)
        led_list[90 + s] = (5, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.001)

    for l in range(0, 120, 5):

        led_list[61 + l] = (5, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.001)

def left_forest():
    for l in range(0, 120, 5):
        led_list[60 + l] = (5, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.001)
        
    for b in range(0, 27, 5):
        led_list[61 + b] = (20, 181, 5)
        led_list[62 + b] = (20, 181, 5)
        led_list[63 + b] = (20, 181, 5)
        led_list[64 + b] = (20, 181, 5)
        led_list[91 + b] = (20, 181, 5)
        led_list[92 + b] = (20, 181, 5)
        led_list[93 + b] = (20, 181, 5)
        led_list[94 + b] = (20, 181, 5)
        led_list[121 + b] = (20, 181, 5)
        led_list[122 + b] = (20, 181, 5)
        led_list[123 + b] = (20, 181, 5)
        led_list[124 + b] = (20, 181, 5)
        led_list[151 + b] = (20, 181, 5)
        led_list[152 + b] = (20, 181, 5)
        led_list[153 + b] = (20, 181, 5)
        led_list[154 + b] = (20, 181, 5)
        client.put_pixels(led_list)
        time.sleep(0.001)
        
    for s in range(0, 240, 60):
        led_list[60 + s] = (5, 242, 230)
        led_list[116 + s] = (5, 242, 230)
        led_list[117 + s] = (5, 242, 230)
        led_list[118 + s] = (5, 242, 230)
        led_list[119 + s] = (5, 242, 230)
        led_list[86 + s] = (5, 242, 230)
        led_list[87 + s] = (5, 242, 230)
        led_list[88 + s] = (5, 242, 230)
        led_list[89 + s] = (5, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.001)
        
    for l in range(0, 120, 5):
        led_list[60 + l] = (5, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.001)

def right_forest():
    for l in range(0, 120, 5):
        led_list[62 + l] = (5, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.001)
        
    for b in range(0, 27, 5):
        led_list[63 + b] = (20, 181, 5)
        led_list[64 + b] = (20, 181, 5)
        led_list[65 + b] = (20, 181, 5)
        led_list[66 + b] = (20, 181, 5)
        led_list[93 + b] = (20, 181, 5)
        led_list[94 + b] = (20, 181, 5)
        led_list[95 + b] = (20, 181, 5)
        led_list[96 + b] = (20, 181, 5)
        led_list[123 + b] = (20, 181, 5)
        led_list[124 + b] = (20, 181, 5)
        led_list[125 + b] = (20, 181, 5)
        led_list[126 + b] = (20, 181, 5)
        led_list[153 + b] = (20, 181, 5)
        led_list[154 + b] = (20, 181, 5)
        led_list[155 + b] = (20, 181, 5)
        led_list[156 + b] = (20, 181, 5)
        client.put_pixels(led_list)
        time.sleep(0.001)
        
    for s in range(0, 240, 60):
        led_list[62 + s] = (5, 242, 230)
        led_list[118 + s] = (5, 242, 230)
        led_list[119 + s] = (5, 242, 230)
        led_list[120 + s] = (5, 242, 230)
        led_list[121 + s] = (5, 242, 230)
        led_list[88 + s] = (5, 242, 230)
        led_list[89 + s] = (5, 242, 230)
        led_list[90 + s] = (5, 242, 230)
        led_list[91 + s] = (5, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.001)
        
    for l in range(0, 120, 5):
        led_list[62 + l] = (5, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.001)

def forest_move():
    print(forest_base())
    for _ in range(10):
        print(central_forest())
        print(left_forest())
        print(central_forest())
        print(right_forest())
    

def dbzlogo():
#This is the DBZ game screen logo. It basically says DBZ while using the leds
    for y in range(0, 60):
        #Changes the whole leds stripes to baby blue
        led_list[y] = (5, 242, 230)
        led_list[60 + y] = (5, 242, 230)
        led_list[120+ y] = (5, 242, 230)
        led_list[239 - y] = (5, 242, 230)
        led_list[299 - y] = (5, 242, 230)
        led_list[359 - y] = (5, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.05)
        
     
    for x in range(0, 360):
        #This is D
        led_list[16] = (colours.get('yellow'))
        led_list[17] = (colours.get('yellow'))
        led_list[18] = (colours.get('yellow'))
        led_list[19] = (colours.get('yellow'))
        led_list[20] = (colours.get('yellow'))
        led_list[21] = (colours.get('yellow'))
        led_list[22] = (colours.get('yellow'))
        
        led_list[76] = (colours.get('yellow'))
        led_list[77] = (colours.get('yellow'))
        led_list[78] = (colours.get('yellow'))
        led_list[79] = (colours.get('yellow'))
        led_list[80] = (colours.get('yellow'))
        led_list[81] = (colours.get('yellow'))
        led_list[82] = (colours.get('yellow'))
        led_list[83] = (colours.get('yellow'))
        
        led_list[136] = (255, 221, 3)
        led_list[137] = (255, 221, 3)
        led_list[138] = (colours.get('white'))
        led_list[139] = (colours.get('white'))
        led_list[140] = (colours.get('white'))
        led_list[141] = (colours.get('white'))                    
        led_list[142] = (255, 221, 3)
        led_list[143] = (255, 221, 3)
        
        led_list[196] = (255, 221, 3)
        led_list[197] = (255, 221, 3)
        led_list[198] = (colours.get('white'))
        led_list[199] = (colours.get('white'))
        led_list[200] = (colours.get('white'))
        led_list[201] = (colours.get('white'))
        led_list[202] = (255, 221, 3)
        led_list[203] = (255, 221, 3)
        
        led_list[256] = (255, 173, 10)
        led_list[257] = (255, 173, 10)
        led_list[258] = (255, 173, 10)
        led_list[259] = (255, 173, 10)
        led_list[260] = (255, 173, 10)
        led_list[261] = (255, 173, 10)
        led_list[262] = (255, 173, 10)
        led_list[263] = (255, 173, 10)
        
        led_list[316] = (255, 173, 10)
        led_list[317] = (255, 173, 10)
        led_list[318] = (255, 173, 10)
        led_list[319] = (255, 173, 10)
        led_list[320] = (255, 173, 10)
        led_list[321] = (255, 173, 10)
        led_list[322] = (255, 173, 10)

        #This is B
        led_list[26] = (colours.get('red'))
        led_list[27] = (colours.get('red'))
        led_list[28] = (colours.get('red'))
        led_list[29] = (colours.get('red'))
        led_list[30] = (colours.get('red'))
        led_list[31] = (colours.get('red'))
        led_list[32] = (colours.get('red'))
        
        led_list[86] = (colours.get('red'))
        led_list[87] = (colours.get('red'))
        led_list[88] = (colours.get('white'))
        led_list[89] = (colours.get('white'))
        led_list[90] = (colours.get('white'))
        led_list[91] = (colours.get('white'))
        led_list[92] = (colours.get('red'))
        led_list[93] = (colours.get('red'))
        
        led_list[146] = (230, 2, 2)
        led_list[147] = (230, 2, 2)
        led_list[148] = (230, 2, 2)
        led_list[149] = (230, 2, 2)
        led_list[150] = (230, 2, 2)
        led_list[151] = (230, 2, 2)
        led_list[152] = (230, 2, 2)
        
        led_list[206] = (230, 2, 2)
        led_list[207] = (230, 2, 2)
        led_list[208] = (230, 2, 2)
        led_list[209] = (230, 2, 2)
        led_list[210] = (230, 2, 2)
        led_list[211] = (230, 2, 2)
        led_list[212] = (230, 2, 2)
        
        led_list[266] = (222, 7, 7)
        led_list[267] = (222, 7, 7)
        led_list[268] = (colours.get('white'))
        led_list[269] = (colours.get('white'))
        led_list[270] = (colours.get('white'))
        led_list[271] = (colours.get('white'))
        led_list[272] = (222, 7, 7)
        led_list[273] = (222, 7, 7)

        led_list[326] = (222, 7, 7)
        led_list[327] = (222, 7, 7)
        led_list[328] = (222, 7, 7)
        led_list[329] = (222, 7, 7)
        led_list[330] = (222, 7, 7)
        led_list[331] = (222, 7, 7)
        led_list[332] = (222, 7, 7)
        
        #This is Z
        led_list[36] = (colours.get('red'))
        led_list[37] = (colours.get('red'))
        led_list[38] = (colours.get('red'))
        led_list[39] = (colours.get('red'))
        led_list[40] = (colours.get('red'))
        led_list[41] = (colours.get('red'))
        led_list[42] = (colours.get('red'))

        led_list[96] = (colours.get('red'))
        led_list[97] = (colours.get('red'))
        led_list[98] = (colours.get('red'))
        led_list[99] = (colours.get('red'))
        led_list[100] = (colours.get('red'))
        led_list[101] = (colours.get('red'))
        led_list[102] = (colours.get('red'))

        led_list[159] = (230, 2, 2)
        led_list[160] = (230, 2, 2)

        led_list[218] = (230, 2, 2)
        led_list[219] = (230, 2, 2)
        
        led_list[276] = (222, 7, 7)
        led_list[277] = (222, 7, 7)
        led_list[278] = (222, 7, 7)
        led_list[279] = (222, 7, 7)
        led_list[280] = (222, 7, 7)
        led_list[281] = (222, 7, 7)
        led_list[282] = (222, 7, 7)
        
        led_list[336] = (222, 7, 7)
        led_list[337] = (222, 7, 7)
        led_list[338] = (222, 7, 7)
        led_list[339] = (222, 7, 7)
        led_list[340] = (222, 7, 7)
        led_list[341] = (222, 7, 7)
        led_list[342] = (222, 7, 7)

        client.put_pixels(led_list)
        time.sleep(0.01)

def forest():
    #This is a function that will be use in the DBZ game 
    #Forest base
    for y in range(0, 60):
    #Chages the first 5 led stripes to baby blue and the last one to brown
        #Sky
        led_list[y] = (5, 242, 230)
        led_list[60 + y] = (5, 242, 230)
        led_list[120 + y] = (5, 242, 230)
        led_list[180 + y] = (5, 242, 230)
        led_list[240 + y] = (5, 242, 230)

        #Ground
        led_list[300 + y] = (34, 112, 26)
        
        client.put_pixels(led_list)
        time.sleep(0.05)

    #Image
    for x in range(0, 360):
    #These are the main objects in the animation
    #For the tree
        #Leaves
        led_list[62] = (20, 181, 5)
        led_list[63] = (20, 181, 5)
        led_list[64] = (20, 181, 5)
        led_list[65] = (20, 181, 5)
        led_list[67] = (20, 181, 5)
        led_list[68] = (20, 181, 5)
        led_list[69] = (20, 181, 5)
        led_list[70] = (20, 181, 5)
        led_list[72] = (20, 181, 5)
        led_list[73] = (20, 181, 5)
        led_list[74] = (20, 181, 5)
        led_list[75] = (20, 181, 5)
        led_list[77] = (20, 181, 5)
        led_list[78] = (20, 181, 5)
        led_list[79] = (20, 181, 5)
        led_list[80] = (20, 181, 5)
        led_list[82] = (20, 181, 5)
        led_list[83] = (20, 181, 5)
        led_list[84] = (20, 181, 5)
        led_list[85] = (20, 181, 5)
        led_list[96] = (20, 181, 5)
        led_list[97] = (20, 181, 5)
        led_list[98] = (20, 181, 5)
        led_list[99] = (20, 181, 5)
        led_list[101] = (20, 181, 5)
        led_list[102] = (20, 181, 5)
        led_list[103] = (20, 181, 5)
        led_list[104] = (20, 181, 5)
        led_list[106] = (20, 181, 5)
        led_list[107] = (20, 181, 5)
        led_list[108] = (20, 181, 5)
        led_list[109] = (20, 181, 5)
        led_list[111] = (20, 181, 5)
        led_list[112] = (20, 181, 5)
        led_list[113] = (20, 181, 5)
        led_list[114] = (20, 181, 5)
        
        led_list[122] = (20, 181, 5)
        led_list[123] = (20, 181, 5)
        led_list[124] = (20, 181, 5)
        led_list[125] = (20, 181, 5)
        led_list[127] = (20, 181, 5)
        led_list[128] = (20, 181, 5)
        led_list[129] = (20, 181, 5)
        led_list[130] = (20, 181, 5)
        led_list[132] = (20, 181, 5)
        led_list[133] = (20, 181, 5)
        led_list[134] = (20, 181, 5)
        led_list[135] = (20, 181, 5)
        led_list[137] = (20, 181, 5)
        led_list[138] = (20, 181, 5)
        led_list[139] = (20, 181, 5)
        led_list[140] = (20, 181, 5)
        led_list[142] = (20, 181, 5)
        led_list[143] = (20, 181, 5)
        led_list[144] = (20, 181, 5)
        led_list[145] = (20, 181, 5)
        led_list[156] = (20, 181, 5)
        led_list[157] = (20, 181, 5)
        led_list[158] = (20, 181, 5)
        led_list[159] = (20, 181, 5)
        led_list[161] = (20, 181, 5)
        led_list[162] = (20, 181, 5)
        led_list[163] = (20, 181, 5)
        led_list[164] = (20, 181, 5)
        led_list[166] = (20, 181, 5)
        led_list[167] = (20, 181, 5)
        led_list[168] = (20, 181, 5)
        led_list[169] = (20, 181, 5)
        led_list[171] = (20, 181, 5)
        led_list[172] = (20, 181, 5)
        led_list[173] = (20, 181, 5)
        led_list[174] = (20, 181, 5)


        #Trunk        
        led_list[183] = (130, 92, 4)
        led_list[184] = (130, 92, 4)
        led_list[188] = (130, 92, 4)
        led_list[189] = (130, 92, 4)
        led_list[193] = (130, 92, 4)
        led_list[194] = (130, 92, 4)
        led_list[198] = (130, 92, 4)
        led_list[199] = (130, 92, 4)
        led_list[203] = (130, 92, 4)
        led_list[204] = (130, 92, 4)
        led_list[217] = (130, 92, 4)
        led_list[218] = (130, 92, 4)
        led_list[222] = (130, 92, 4)
        led_list[223] = (130, 92, 4)
        led_list[227] = (130, 92, 4)
        led_list[228] = (130, 92, 4)
        led_list[232] = (130, 92, 4)
        led_list[233] = (130, 92, 4)
        
        led_list[243] = (130, 92, 4)
        led_list[244] = (130, 92, 4)
        led_list[248] = (130, 92, 4)
        led_list[249] = (130, 92, 4)
        led_list[253] = (130, 92, 4)
        led_list[254] = (130, 92, 4)
        led_list[258] = (130, 92, 4)
        led_list[259] = (130, 92, 4)
        led_list[263] = (130, 92, 4)
        led_list[264] = (130, 92, 4)
        led_list[277] = (130, 92, 4)
        led_list[278] = (130, 92, 4)
        led_list[282] = (130, 92, 4)
        led_list[283] = (130, 92, 4)
        led_list[287] = (130, 92, 4)
        led_list[288] = (130, 92, 4)
        led_list[292] = (130, 92, 4)
        led_list[293] = (130, 92, 4)

    #For the tiny city
        led_list[147] = (235, 235, 235)
        led_list[150] = (235, 235, 235)
        led_list[151] = (235, 235, 235)
        led_list[153] = (235, 235, 235)
        led_list[207] = (235, 235, 235)
        led_list[208] = (235, 235, 235)
        led_list[209] = (235, 235, 235)
        led_list[210] = (235, 235, 235)
        led_list[211] = (235, 235, 235)
        led_list[212] = (235, 235, 235)
        led_list[213] = (235, 235, 235)
        led_list[214] = (235, 235, 235)
        
    #For the Sun
        led_list[28] = (colours.get('yellow'))
        led_list[29] = (colours.get('yellow'))
        led_list[30] = (colours.get('yellow'))
        led_list[31] = (colours.get('yellow'))
        led_list[32] = (colours.get('yellow'))
        led_list[33] = (colours.get('yellow'))
        led_list[88] = (colours.get('yellow'))
        led_list[89] = (colours.get('yellow'))
        led_list[90] = (colours.get('yellow'))
        led_list[91] = (colours.get('yellow'))
        led_list[92] = (colours.get('yellow'))
        led_list[93] = (colours.get('yellow'))
        

    #For the clouds
        led_list[5] = (colours.get('white'))
        led_list[6] = (colours.get('white'))
        led_list[7] = (colours.get('white'))
        led_list[8] = (colours.get('white'))
        led_list[9] = (colours.get('white'))
        led_list[10] = (colours.get('white'))
        led_list[16] = (colours.get('white'))
        led_list[17] = (colours.get('white'))
        led_list[18] = (colours.get('white'))
        led_list[19] = (colours.get('white'))
        led_list[20] = (colours.get('white'))
        led_list[35] = (colours.get('white'))
        led_list[36] = (colours.get('white'))
        led_list[37] = (colours.get('white'))
        led_list[46] = (colours.get('white'))
        led_list[47] = (colours.get('white'))
        led_list[48] = (colours.get('white'))
        led_list[49] = (colours.get('white'))
        led_list[50] = (colours.get('white'))
        led_list[51] = (colours.get('white'))
        led_list[52] = (colours.get('white'))
        led_list[53] = (colours.get('white'))
        led_list[54] = (colours.get('white'))
        led_list[55] = (colours.get('white'))
        led_list[56] = (colours.get('white'))
        led_list[57] = (colours.get('white'))
        led_list[58] = (colours.get('white'))
        

        
    #For the pathway
        led_list[268] = (140, 137, 129)
        led_list[269] = (140, 137, 129)
        led_list[270] = (140, 137, 129)
        led_list[271] = (140, 137, 129)
        led_list[272] = (140, 137, 129)
        led_list[273] = (140, 137, 129)

        led_list[328] = (140, 137, 129)
        led_list[329] = (140, 137, 129)
        led_list[330] = (140, 137, 129)
        led_list[331] = (140, 137, 129)
        led_list[332] = (140, 137, 129)
        led_list[333] = (140, 137, 129)
        time.sleep(0.01)
        client.put_pixels(led_list)

def city():
    for y in range(0, 60):
        led_list[y] = (140, 137, 129)
        led_list[60 + y] = (140, 137, 129)
        led_list[120 + y] = (140, 137, 129)
        led_list[180 + y] = (140, 137, 129)
        led_list[240 + y] = (140, 137, 129)
        led_list[300 + y] = (255, 255, 255)
        client.put_pixels(led_list)
        time.sleep(0.05)
        
    for z in range(0, 300, 60):
        #Sky
        led_list[7 + z] = (5, 242, 230)
        led_list[8 + z] = (5, 242, 230)
        led_list[9 + z] = (5, 242, 230)
        led_list[10 + z] = (5, 242, 230)
        led_list[16 + z] = (5, 242, 230)
        led_list[17 + z] = (5, 242, 230)
        led_list[18 + z] = (5, 242, 230)
        led_list[19 + z] = (5, 242, 230)
        led_list[25 + z] = (5, 242, 230)
        led_list[26 + z] = (5, 242, 230)
        led_list[27 + z] = (5, 242, 230)
        led_list[28 + z] = (5, 242, 230)
        led_list[29 + z] = (5, 242, 230)
        led_list[30 + z] = (5, 242, 230)
        led_list[31 + z] = (5, 242, 230)
        led_list[32 + z] = (5, 242, 230)
        led_list[33 + z] = (5, 242, 230)
        led_list[34 + z] = (5, 242, 230)
        led_list[35 + z] = (5, 242, 230)
        led_list[36 + z] = (5, 242, 230)
        led_list[45 + z] = (5, 242, 230)
        led_list[46 + z] = (5, 242, 230)
        led_list[47 + z] = (5, 242, 230)
        led_list[48 + z] = (5, 242, 230)
        led_list[56 + z] = (5, 242, 230)
        led_list[57 + z] = (5, 242, 230)
        led_list[58 + z] = (5, 242, 230)
        led_list[59 + z] = (5, 242, 230)
        
        
        client.put_pixels(led_list)
        time.sleep(0.05)
        
    for a in range(0, 120, 60):
        #door house
        led_list[182 + a] = (130, 92, 4)
        led_list[183 + a] = (130, 92, 4)
        led_list[193 + a] = (130, 92, 4)
        led_list[194 + a] = (130, 92, 4)
        led_list[201 + a] = (130, 92, 4)
        led_list[202 + a] = (130, 92, 4)
        led_list[220 + a] = (130, 92, 4)
        led_list[221 + a] = (130, 92, 4)
        led_list[231 + a] = (130, 92, 4)
        led_list[232 + a] = (130, 92, 4)
        
        
        client.put_pixels(led_list)
        time.sleep(0.05)
        
    for x in range(0, 360):
    #For the statue
        #Head
        led_list[30] = (237, 188, 38)
        led_list[31] = (237, 188, 38)
        led_list[90] = (237, 188, 38)
        led_list[91] = (237, 188, 38)
        
        #Arm
        led_list[145] = (237, 188, 38)
        led_list[146] = (237, 188, 38)
        led_list[205] = (237, 188, 38)
        led_list[206] = (237, 188, 38)
        led_list[265] = (237, 188, 38)
        led_list[266] = (237, 188, 38)

        led_list[155] = (237, 188, 38)
        led_list[156] = (237, 188, 38)
        led_list[215] = (237, 188, 38)
        led_list[216] = (237, 188, 38)
        led_list[275] = (237, 188, 38)
        led_list[276] = (237, 188, 38)
        
        #Body
        led_list[147] = (237, 188, 38)
        led_list[148] = (237, 188, 38)
        led_list[149] = (237, 188, 38)
        led_list[150] = (237, 188, 38)
        led_list[151] = (237, 188, 38)
        led_list[152] = (237, 188, 38)
        led_list[153] = (237, 188, 38)
        led_list[154] = (237, 188, 38)
        
        led_list[207] = (237, 188, 38)
        led_list[208] = (237, 188, 38)
        led_list[209] = (237, 188, 38)
        led_list[210] = (237, 188, 38)
        led_list[211] = (237, 188, 38)
        led_list[212] = (237, 188, 38)
        led_list[213] = (237, 188, 38)
        led_list[214] = (237, 188, 38)
        
        #Leg
        led_list[268] = (237, 188, 38)
        led_list[269] = (237, 188, 38)
        led_list[272] = (237, 188, 38)
        led_list[273] = (237, 188, 38)
        led_list[328] = (237, 188, 38)
        led_list[329] = (237, 188, 38)
        led_list[332] = (237, 188, 38)
        led_list[333] = (237, 188, 38)
        
    #For the buildings
        client.put_pixels(led_list)
        time.sleep(0.01)

def tournament():
    #Base for the setting
    for y in range(0, 60):
        led_list[y] = (5, 242, 230)
        led_list[60 + y] = (5, 242, 230)
        led_list[120 + y] = (colours.get('green'))
        led_list[180 + y] = (colours.get('green'))
        led_list[240 + y] = (colours.get('green'))
        led_list[300 + y] = (colours.get('white'))
        client.put_pixels(led_list)
        time.sleep(0.01)

    for z in range(0, 120, 4):
        #Barriers
        led_list[240 + z] = (colours.get('white')) 
        led_list[241 + z] = (colours.get('white'))
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for x in range(0, 120, 60):
        #Stadium
        led_list[140 + x] = (140, 137, 129)
        led_list[141 + x] = (140, 137, 129)
        led_list[142 + x] = (140, 137, 129)
        led_list[143 + x] = (140, 137, 129)
        led_list[144 + x] = (140, 137, 129)
        led_list[145 + x] = (140, 137, 129)
        led_list[146 + x] = (140, 137, 129)
        led_list[147 + x] = (140, 137, 129)
        led_list[148 + x] = (140, 137, 129)
        led_list[149 + x] = (140, 137, 129)
        led_list[150 + x] = (140, 137, 129)
        led_list[151 + x] = (140, 137, 129)
        led_list[152 + x] = (140, 137, 129)
        led_list[153 + x] = (140, 137, 129)
        led_list[154 + x] = (140, 137, 129)
        led_list[155 + x] = (140, 137, 129)
        led_list[156 + x] = (140, 137, 129)
        led_list[157 + x] = (140, 137, 129)
        led_list[158 + x] = (140, 137, 129)
        led_list[159 + x] = (140, 137, 129)
        led_list[160 + x] = (140, 137, 129)

        #Other seats left
        led_list[60 + x] = (colours.get('white'))
        led_list[61 + x] = (colours.get('white'))
        led_list[120 + x] = (colours.get('white'))
        led_list[121 + x] = (colours.get('white'))
        led_list[122 + x] = (colours.get('white'))
        led_list[124 + x] = (colours.get('white'))

        #Other seats right
        led_list[118 + x] = (colours.get('white'))
        led_list[119+ x] = (colours.get('white'))
        led_list[175 + x] = (colours.get('white'))
        led_list[177 + x] = (colours.get('white'))
        led_list[178 + x] = (colours.get('white'))
        led_list[179 + x] = (colours.get('white'))
        
    for a in range(0, 360):
        led_list[183] = (colours.get('white'))
        led_list[236] = (colours.get('white'))
        
        client.put_pixels(led_list)
        time.sleep(0.01)
        


def door():
    for y in range(0, 60):
        led_list[y] = (250, 237, 165)
        led_list[60 + y] = (250, 237, 165)
        led_list[120 + y] = (250, 237, 165)
        led_list[180 + y] = (250, 237, 165)
        led_list[240 + y] = (250, 237, 165)
        led_list[300 + y] = (140, 137, 129)
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for x in range(0, 240, 60):
        led_list[70 + x] = (130, 92, 4)
        led_list[71 + x] = (130, 92, 4)
        led_list[72 + x] = (130, 92, 4)
        led_list[73 + x] = (130, 92, 4)
        led_list[74 + x] = (130, 92, 4)
        led_list[75 + x] = (130, 92, 4)
        led_list[76 + x] = (130, 92, 4)
        led_list[77 + x] = (130, 92, 4)
        led_list[78 + x] = (130, 92, 4)
        led_list[79 + x] = (130, 92, 4)
        led_list[80 + x] = (130, 92, 4)
        
        led_list[85 + x] = (130, 92, 4)
        led_list[86 + x] = (130, 92, 4)
        led_list[87 + x] = (130, 92, 4)
        led_list[88 + x] = (130, 92, 4)
        led_list[89 + x] = (130, 92, 4)
        led_list[90 + x] = (130, 92, 4)
        led_list[91 + x] = (130, 92, 4)
        led_list[92 + x] = (130, 92, 4)
        led_list[93 + x] = (130, 92, 4)
        led_list[94 + x] = (130, 92, 4)
        led_list[95 + x] = (130, 92, 4)
        
        led_list[100 + x] = (130, 92, 4)
        led_list[101 + x] = (130, 92, 4)
        led_list[102 + x] = (130, 92, 4)
        led_list[103 + x] = (130, 92, 4)
        led_list[104 + x] = (130, 92, 4)
        led_list[105 + x] = (130, 92, 4)
        led_list[106 + x] = (130, 92, 4)
        led_list[107 + x] = (130, 92, 4)
        led_list[108 + x] = (130, 92, 4)
        led_list[109 + x] = (130, 92, 4)
        led_list[110 + x] = (130, 92, 4)
        client.put_pixels(led_list)
        time.sleep(0.01)

    for z in range(0, 60):
        led_list[197] = (237, 188, 38)
        led_list[198] = (237, 188, 38)
        led_list[212] = (237, 188, 38)
        led_list[213] = (237, 188, 38)
        led_list[227] = (237, 188, 38)
        led_list[228] = (237, 188, 38)
        client.put_pixels(led_list)
        time.sleep(0.01)

def toilet():
    
    for y in range(0, 60):
        led_list[y] = (250, 237, 165)
        led_list[60 + y] = (250, 237, 165)
        led_list[120 + y] = (250, 237, 165)
        led_list[180 + y] = (250, 237, 165)
        led_list[240 + y] = (250, 237, 165)
        led_list[300 + y] = (250, 237, 165)
        client.put_pixels(led_list)
        time.sleep(0.01)

    for x in range(0, 360, 60):
        led_list[20 + x] = (130, 92, 4)
        led_list[21 + x] = (80, 173, 160)
        led_list[22 + x] = (80, 173, 160)
        led_list[23 + x] = (80, 173, 160)
        led_list[24 + x] = (80, 173, 160)
        led_list[25 + x] = (80, 173, 160)
        led_list[26 + x] = (80, 173, 160)
        
        led_list[29 + x] = (255, 255, 255)
        led_list[30 + x] = (255, 255, 255)
        
        led_list[33 + x] = (80, 173, 160)
        led_list[34 + x] = (80, 173, 160)
        led_list[35 + x] = (80, 173, 160)
        led_list[36 + x] = (80, 173, 160)
        led_list[37 + x] = (80, 173, 160)
        led_list[38 + x] = (80, 173, 160)
        led_list[39 + x] = (130, 92, 4)
        client.put_pixels(led_list)
        time.sleep(0.01)

    for z in range(0, 120, 60):
        led_list[27 + z] = (255, 255, 255)
        led_list[32 + z] = (255, 255, 255)
        led_list[146 + z] = (255, 255, 255)
        led_list[147 + z] = (255, 255, 255)
        led_list[152 + z] = (255, 255, 255)
        led_list[153 + z] = (255, 255, 255)
        client.put_pixels(led_list)
        time.sleep(0.01)
    playsound('toilet.mp3')

def door2():
    #This is the first door from options
    for y in range(0, 60):
        led_list[y] = (250, 237, 165)
        led_list[60 + y] = (250, 237, 165)
        led_list[120 + y] = (250, 237, 165)
        led_list[180 + y] = (250, 237, 165)
        led_list[240 + y] = (250, 237, 165)
        led_list[300 + y] = (250, 237, 165)
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for x in range(0, 360, 60):  
        led_list[20 + x] = (130, 92, 4)
        led_list[39 + x] = (130, 92, 4)
        client.put_pixels(led_list)
        time.sleep(0.01)

    for z in range(0, 18, 1):
        led_list[21 + z] = (15, 242, 230)
        led_list[81 + z] = (15, 242, 230)
        led_list[141 + z] = (15, 242, 230)
        led_list[201 + z] = (15, 242, 230)
        led_list[261 + z] = (15, 242, 230)
        led_list[321 + z] = (15, 242, 230)
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for a in range(0, 240, 60):
        led_list[28 + a] = (35, 65, 150)
        led_list[29 + a] = (35, 65, 150)
        led_list[30 + a] = (35, 65, 150)
        led_list[31 + a] = (35, 65, 150)
        led_list[32 + a] = (35, 65, 150)
        led_list[33 + a] = (35, 65, 150)
        client.put_pixels(led_list)
        time.sleep(0.01)

    for b in range(0, 120 , 60):
        led_list[86 + b] = (35, 65, 150)
        led_list[87 + b] = (35, 65, 150)
        led_list[88 + b] = (35, 65, 150)
        led_list[89 + b] = (35, 65, 150)
        led_list[90 + b] = (35, 65, 150)
        led_list[91 + b] = (35, 65, 150)
        led_list[92 + b] = (35, 65, 150)
        led_list[93 + b] = (35, 65, 150)
        led_list[94 + b] = (35, 65, 150)
        led_list[95 + b] = (35, 65, 150)
        client.put_pixels(led_list)
        time.sleep(0.01)

def door3():
    for y in range(0, 60):
        led_list[y] = (250, 237, 165)
        led_list[60 + y] = (250, 237, 165)
        led_list[120 + y] = (250, 237, 165)
        led_list[180 + y] = (250, 237, 165)
        led_list[240 + y] = (250, 237, 165)
        led_list[300 + y] = (250, 237, 165)
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for x in range(0, 360, 60):
        led_list[20 + x] = (130, 92, 4)
        led_list[39 + x] = (130, 92, 4)
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for z in range(0, 18, 1):
        led_list[21 + z] = (87, 7, 20)
        led_list[81 + z] = (87, 7, 20)
        led_list[141 + z] = (87, 7, 20)
        led_list[201 + z] = (140, 137, 129)
        led_list[261 + z] = (140, 137, 129)
        led_list[321 + z] = (140, 137, 129)
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for a in range(0, 180, 60):
        led_list[208 + a] = (255,255, 255)
        led_list[209 + a] = (255,255, 255)
        led_list[210 + a] = (255,255, 255)
        led_list[211 + a] = (255,255, 255)
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for b in range(0, 360):
        led_list[207] = (46, 20, 3)
        led_list[212] = (46, 20, 3)
        led_list[147] = (46, 20, 3)
        led_list[148] = (46, 20, 3)
        led_list[149] = (46, 20, 3)
        led_list[150] = (46, 20, 3)
        led_list[151] = (46, 20, 3)
        led_list[152] = (46, 20, 3)
        client.put_pixels(led_list)
        time.sleep(0.01)

def endgame():
#This is the screen for when the game is finished
    for y in range(0, 60):
        led_list[y] = (0, 0, 0)
        led_list[60 + y] = (0, 0, 0)
        led_list[120 + y] = (0, 0, 0)
        led_list[180 + y] = (0, 0, 0)
        led_list[240 + y] = (0, 0, 0)
        led_list[300 + y] = (0, 0, 0)
        client.put_pixels(led_list)
        time.sleep(0.01)

    for x in range(0, 300, 60):
        led_list[19 + x] = (colours.get('red'))
        led_list[28 + x] = (colours.get('red'))
        led_list[32 + x] = (colours.get('red'))
        led_list[36 + x] = (colours.get('red'))
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for b in range(0, 180, 60):
        led_list[101 + b] = (colours.get('red'))
        client.put_pixels(led_list)
        time.sleep(0.01)
        
    for z in range(0, 300, 240):
        led_list[19 + z] = (colours.get('red'))
        led_list[20 + z] = (colours.get('red'))
        led_list[21 + z] = (colours.get('red'))
        led_list[22 + z] = (colours.get('red'))
        led_list[23 + z] = (colours.get('red'))
        led_list[24 + z] = (colours.get('red'))
        led_list[36 + z] = (colours.get('red'))
        led_list[37 + z] = (colours.get('red'))
        led_list[38 + z] = (colours.get('red'))
        led_list[39 + z] = (colours.get('red'))
        led_list[40 + z] = (colours.get('red'))
        client.put_pixels(led_list)
        time.sleep(0.01)

    for a in range(0, 360):
        led_list[140] = (colours.get('red'))
        led_list[141] = (colours.get('red'))
        led_list[142] = (colours.get('red'))
        
        led_list[89] = (colours.get('red'))
        led_list[150] = (colours.get('red'))
        led_list[211] = (colours.get('red'))
        client.put_pixels(led_list)
        time.sleep(0.01)
    playsound('game_over.mp3')
        
def gameStart ():
#This define funtion is a game based on the user's input something will happen. Everytime you play its different.
    print("IMPORTANT, 'none' messages will appear across the game. They do not represent anything withing the text it just means that the leds have no funtion for that line. ")
    time.sleep(2)
    print("LOADING...")             #Give loading feeling.
    print(dbzlogo())                #It will demonstrate the led animation for the DBZ.
    playsound('dbz.mp3')
    print(" ")
    print("START")
    playsound('wave.mp3')
    playsound('ha.mp3')
    while True:                     #while True in case the user types the wrong input it doesn't need to start the whole game again.
        print(" ")
        print(delay_word("You get revived by the dragon balls and your first reaction is... "))
        userInput = input("Look around - (1) Panic - (2): ")            #Taking user's input.
        linput = userInput.lower()                                      #Making the string lowercase so it doesn't matter if the user types in capitals, there will be no errors when reading it.
                
        if(linput == "look around" or linput == str(1)):                #Choices, depending on the option, it will move on to another define function to continue the game or end it like in the code.
            displayHallway(1)
                
        elif(linput == "panic" or linput == str(2)):
            gameOver(1)
                
        else:
            print("Please select one of the actions shown. ")           #Let the user know that there are only 2 options available.

def displayHallway(hallwayNumber):          #This define function creates another pathway which is connected to the previous funtion so different events can happen.
    while True:
        if(hallwayNumber == 1):             #This is a reference number for hallway since if displayHallway(1) it will continue on this section of the code, if not it will go to the one with the corresponding number
            print(forest())                 #This will display the forest animation
            playsound('forest.mp3')
            while True:
                print(delay_word("You realise that you are in a forest and far away you see a small city, what do you do... "))
                userInput = input("Walk towards the city - (1) Keep walking around - (2): ")
                linput = userInput.lower()
		
                if(linput == "walk towards the city" or linput == str(1)):
                    print(delay_word("As you keep walking towards the city you see someone flying at a high speed but the image is a bit blurry. "))
                    print(delay_word("Half an hour later you reached the city which is suprisingly huge. "))
                    print(city())
                    playsound('city.mp3')
                    print(delay_word("Then, you turn to your left and you see a statue that says Hercule." ))
                    print(delay_word("After staring the statue for a minute someone comes to you and asks you if you would like to join the fighting tournament or watch it. "))
                    print(delay_word("What do you do? "))
                    userInput = input(" Enter the tournament - (1) Watch the tournement - (2): ")           #Same as before, it takes the user's input
                    linput = userInput.lower()                                                              #Makes a lowecase to preven errors in the code when reading it
                        
                    if(linput == "enter the tournament" or linput == str(1)):                               #Depending on the option chose, it will lead to a different pathway that has different animations as well as different options
                        displayArchway(2)

                    elif(linput == "watch the tournament" or linput == str(2)):
                        displayArchway(1)

                    else:
                        print("Please select one of the actions shown. ")                                   #Makes the user choose the right option so the program doesn't give an error
                        
                elif(linput == "keep walking around" or linput == str(2)):                                  #This is the other response to the first user's input
                    displayHallway(2)
                    
                else:
                        print("Please select one of the actions shown. ")
		    
        elif(hallwayNumber == 2):
            print(delay_word("After hours of walking you realise you are still in the forest and have to go to the city as that's the only path available. "))
            print(city())
            playsound('city.mp3')
            print(delay_word("Once you got to the city you see a poster that talks about a fighting tournament. You are very curious about it as the winning price is 1 million dollars so you decide to sign up. "))
            displayArchway(2)
                        
        elif(hallwayNumber == 3):
            print(delay_word("Immediately you feel the necessity of going to the toilet and you leave the stadium in order to find a public toilet. "))
            playsound('walk.mp3')
            playsound('walk.mp3')
            playsound('walk.mp3')
            playsound('walk.mp3')
            print(door())
            print(delay_word("You entered an old building behind the stadium but you get lost. You see 3 doors. "))
            
            while True:
                print(delay_word("You decide to open one of them but you are not sure which one is the correct one as all the doors look exactly the same "))
                print(' ')
                userInput = input("First door - (1) Second door - (2) Third door - (3): ")
                linput = userInput.lower()
                        
                if(linput == "first door" or linput == str(1)):
                    playsound('door.mp3')
                    print(door2())
                    print(delay_word("Accidently you opened the main door that leads you to the fighting sceen. "))
                    playsound('ha.mp3')
                    print(delay_word("You get hit by goku's hamehameha as he thought you were the enemy. "))
                    gameOver(2)
                    
            
                elif(linput == "second door" or linput == str(2)):
                    playsound('door.mp3')
                    print(toilet())
                    print(delay_word("You found the toilet"))
                    print(delay_word("At the end of the day you enjoyed the tournament. "))
                    print(delay_word("Then randomly you hear a loud beeping noise. Turned out to be your alarm and you had to get ready for college. "))
                    print(endgame())
                    backtomenu()
                                    
                elif(linput == "third door" or linput == str(3)):
                    playsound('door.mp3')
                    print(door3())
                    print(delay_word("This door led to a massive room full of trophies and a small black desk. "))
                    print(delay_word("Behind the desk there is a white suitcase. "))
                    print(delay_word("Out of your curiosity you decide to get closer. "))
                    print(delay_word("Would you like to open the suitcase? "))
                    userInput = input(delay_word("Yes - (1)  NO - (2) "))
                    linput = userInput.lower()

                    if(linput == "yes" or linput == str(1)):
                        print(delay_word("The suitcase was full of 20 dollars note. Looks like its the main reward for the champion. "))
                        gameOver(3)

                    elif(linput == "no" or linput == str(2)):
                        print(delay_word("Someone opens the door immediately. You turn around while you are asking for the toilet. "))
                        print(delay_word("Then you notice the person is the man thats in the statue at the beginning of the city. "))
                        print(delay_word("He apologieses for having such a messy tournament and gives you 20 thousand dollars as compensation. "))
                        print(delay_word("After the whole tournament you left happy as you had enough money to start over a new life and you also became really good friends with the man. "))
                        print(endgame())
                        backtomenu()
                        
                    else:
                        print("Please select one of the actions shown. ")
                else:
                    print("Please select one of the actions shown. ")
        else:
            print("Please select one of the actions shown. ")


def displayArchway(archwayNumber):
    while True:
        if(archwayNumber == 1):
            print(tournament())
            playsound('fight.mp3')
            print(delay_word("There are a several amount of fights and you still think if you would be alive if you entered the tournement or not. "))
            displayHallway(3)

        elif(archwayNumber == 2):
            while True:
                print(delay_word("Your decision was to fight in the torunament"))
                print(tournament())
                playsound('fight.mp3')
                print(delay_word("After several fights, your body stops respoding and you are immobile. The only thing that you could control was your eyes looking left and right."))
                print(delay_word("You remember how happy you felt when you were at the stage. You get worried that you may die again as you start to see everything blurry and darker."))
                print(delay_word("Just before faint you decide to try..."))
                while True:
                    userInput = input("Standing up and scream -'I CAN CONTINUE'- (1) or pray to the gods(2): ")
                    linput = userInput.lower()
                    if(linput == "standing up and scream" or linput == str(1)):
                        print(delay_word("The whole audience starts looking at you as they hear some really high pitch noise. Everyone laughed and you started fainting. "))
                        gameOver(4)

                    elif(linput == "pray to the gods" or linput == str(2)):
                        print(delay_word("Immediately you start praying to the gods..."))
                        gameOver(4)
                            
                    else:
                        print("Please select one of the actions shown. ")
                            
        else:
            print("Please select one of the actions shown. ")


def gameOver (gameOverState):
    if(gameOverState == 1):
        print(delay_word("You panicked so much that you had a heart attack. "))
        print(delay_word("What a waste of a second chance to live. "))
        print(endgame())
        backtomenu()
        
        print(' ')
    elif(gameOverState == 2):
        print(delay_word("You take the time to look down while you are flying to heaven. Then the alarm sounds and you realise it was a dream. "))
        print(endgame())
        backtomenu()
        print(' ')
                    
    elif(gameOverState == 3):
        print(delay_word("30 seconds later someone opens the door, you were in shocked as you kept staring as if it was your golden ticket. "))
        print(delay_word("The mysterious person loudly says -'I'M GOING TO STOP YOU'-. "))
        print(delay_word("You rapidly turned to your right and notice that he was the same guy from the statue. "))
        print(delay_word("Sadly he jumps and kicks your head. You die because he thought you were a thieft who tried to steal the money 5 times before you even entered the room. "))
        print(endgame())
        backtomenu()
        print(' ')
                    
    elif (gameOverState == 4):
        print(delay_word("You see a shadow walking near by you. "))
        print(delay_word("You are not sure what it is... "))
        print(delay_word("Randomly you feel better while you are chewing a bean. "))
        print(delay_word("Then you realised that Goku gave you a senzu bean and all the damage taken has been healed up. "))
        print(delay_word("You thanks him and you start looking for a normal job and a normal life, appreciating the times you have been revived for. "))
        print(endgame())
        backtomenu()
        print(' ')
        

def menu():
    #INTRODUCTION
    
    while True:
        print(' ')
        print('Choose the type of animation desired, if any question on what each animation does type "description".')
        print(mainmenu)
        

        #OPTION PHASE
        animation = input('Enter the animation wanted: ')
        lanim = animation.lower()
        
        if (lanim == 'description' or lanim == '6'):
                                                        #This section of the code describes the user what each option does so they have a bit more of knowledge when choosing one
            print(' ')
            print('Fading - a basic animation of the leds changing colour from a darker colour to a ligher one')
            print('Guess - a basic guess the number/colour game')
            print("DBZ - A game based on Dragon Ball Z where depending on the user's input something will happen. Also known as the burtterfly effect.")
            print('Animation - different leds are changing colour while during different patterns')
            print('Morse - morse code that allows the user to see the message written encrypted by using the leds') 
            time.sleep(2)
            
        elif (lanim == 'fading' or lanim == '1'):           #Takes 2 inputs in case the user types the number or the key word
            lights = int(input('Number of lights: '))       #Takes user input to know how many leds to display
            led_list = [(0, 0, 0)]*lights                   #This is a list of a tuple of the colour of the leds, being black
            fade_am = int(input('fading amount: '))         #Amount of colour increased in each of the rgb lights
            while True:
                for led in enumerate(led_list):

                    r,g,b = led[1]
                    r = r+fade_am
                    g = g+fade_am
                    b = b+fade_am

                    new_colour = (r, g, b)
                    led_list[led[0]] = new_colour

                    if r>= 255 or r<= 0:
                        fade_am = -fade_am
    
                client.put_pixels(led_list)
                client.put_pixels(led_list)
                sleep(0.05)

    #It fades the colour from black to white adding the fade_am to the origin value (0) and the max value that it can go is 255  

        elif (lanim == 'morse' or lanim == '5'):
            message = str(input("Enter you text here: ")).lower()   #Takes user input and changes any of the capital letters and converts them into lower case
            main = morsemain(message)                             #Use moremain() define function to print output to show the user what the morse code would be like
            print(main)        
            
        elif (lanim == 'guess' or lanim == '2'):
            colourgame = ['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'white', 'black']           #A list of colours that will be randomly pick
            guess_colour = random.choice(colourgame)                                                        #Chooses a value from the list randomly so it can be guess
            guess_number = random.randint(0, 50)                                                            #Chooses a random value from a range of 0 to 50
            attempt = 0                                                                                     #This is the starting point of attempts
            print('IMPORTANT, TYPE THE WORD IN BRACKETS!')
            print(guess)                                                                                    #Prints the option ASCII drawing so the user can see it clearly
            user_input = input('What do you want to play? ')
            linput = user_input.lower()

            if (linput == 'number' or linput == '1'):                                                   #If number 1 or number is typed, it will start the guess the number game
                print('Guess the number between 0 and 50')
                user_Input = int(input('Input your answer: ' ))
                while user_Input!=guess_number:                                                         #Loops until the user's input is equal to the number randomly chosen
                    if user_Input < guess_number:
                        attempt += 1                                                                    #For every incorrect answer it will add 1 to the attempt in order to record the total amount od attempts
                        print('Try again, your number is too low')                                      #Let the user know if its higher or lower than the number chosen before
                        user_Input = int(input('Input your answer: ' ))                                 #Ask for a new input
                    
                        print(all_leds('black'))                                                        #This will animate a red blinking animation to led the user know that the answer is wrong
                        print(all_leds('red'))
                        print(all_leds('black'))
                        print(all_leds('red'))
                        print(all_leds('black'))
                        print(all_leds('red'))
                    
                    elif user_Input > guess_number:
                        attempt += 1
                        print('Try again, your number is too high')
                        user_Input = int(input('Input your answer: ' ))
                        print(all_leds('black'))
                        print(all_leds('red'))
                        print(all_leds('black'))
                        print(all_leds('red'))
                        print(all_leds('black'))
                        print(all_leds('red'))

                
                print('Well done, thats the correct number')                                            #It lets the user know that the input is right                           
                print('This is you number of attempts: ', attempt)                                      #Shows total number of attempts
                print(all_leds('black'))                                                                #Displays a green blinking animation to show the final value inserted was correct
                print(all_leds('green'))
                print(all_leds('black'))
                print(all_leds('green'))
                print(all_leds('black'))
                print(all_leds('green'))

                    
            elif (linput == 'colour' or linput == '2'):
                print(colour_list)                                                                      #Prints lisgt of colours
                print('Guess the colour')
                user_Input = input('Choose a colour: ')
                linput = user_input.lower()                                                             #Converts the input into lowercase to prevent errors
                while linput != guess_colour:
                    print(all_leds('black'))
                    print(all_leds('red'))
                    print(all_leds('black'))
                    print(all_leds('red'))
                    print(all_leds('black'))
                    print(all_leds('red'))
                    attempt += 1
                    print('Not the right colour, try again')
                    linput = input('Choose a different colour: ')                                       #Ask for a new input
                print('Well done, this is your number of attempts ', attempt)
                print(all_leds('black'))                                                        
                print(all_leds('green'))
                print(all_leds('black'))
                print(all_leds('green'))
                print(all_leds('black'))
                print(all_leds('green'))
                    
                

            else:
                print('Enter either "number" or "colour"')
            
        elif (lanim == 'animation' or lanim == '4'):                        #Starts different animations and combines them together
            print("Choose 1 of the following animations.")
            print(anim)
            user_Input = input("Enter your desire animation: ")
            linput = user_Input.lower()
            if (linput == 'basic' or linput == '1'):
                print(colour_list)                                            #Shows the possible colours that can be use
                print("Its going to ask for user'input twice to double check.")
                colour = input('first colour: ')                                #Take first input
                colourd = input('second colour: ')                              #Take second input
                colourr = input('third colour: ')                               #Take third input
                if (colour != dict.fromkeys(colours) or colourd != dict.fromkeys(colours) or colourr != dict.fromkeys(colours)):
                    while True:
                        print('Please choose the right values')
                        print(colour_list)                                            #Shows the possible colours that can be use
                        colour = input('first colour: ')                                #Take first input
                        colourd = input('second colour: ')                              #Take second input
                        colourr = input('third colour: ')                               #Take third input
                        lcolour = colour.lower()                                        #|
                        lcolourd = colourd.lower()                                      #|-- Converts all inputs to lowercase to prevent errors
                        lcolourr = colourr.lower()                                      #|
                        break
                #COMBINATION OF DEFINE FUNCTIONS
                print(snake_both(lcolour, lcolourd, 1))                         
                flashy()
                flashy()
                print(right2(lcolourr))
                print(left(lcolour))
                flashy()
                flashy()
                print(right3('random', 2))
                print(right3(lcolourd, 3))
                print(yago('orange'))
                print(rainbow('red'))

            elif (linput == 'forest' or linput == '2'):
                forest_move()

            else:
                print('Please choose one of the options above')

        elif (lanim == 'dbz' or lanim == '3'):
            #STARTS DEFINE FUNTION
            gameStart()

        elif (lanim == 'exit' or lanim == '7'):                             #In case the user wants to close the program
            end()
        
        else:
            print('Please enter one of the options above')

    
def backtomenu():
    question = input('Would you like to go back? ')
    if question == 'yes':
        return menu()
    elif question == 'no':
        end()
    else:
        print('It has to be either "yes" or "no"')
        
#START OF PROJECT
print(menu())

    
