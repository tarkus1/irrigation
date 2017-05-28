import subprocess
import csv
import re


from gpiozero import LED
from time import sleep
from datetime import datetime

gr=LED(4)
red=LED(14)



while True:
# if True:
        
    p = subprocess.Popen(["owwrite", "26.241E9D010000/date", "0"])

    p = subprocess.Popen(["owread", "26.241E9D010000/date"], stdout=subprocess.PIPE)

    (date,errcode) = p.communicate()
    dateObj = datetime.strptime(date.decode(),'%a %b %d %H:%M:%S %Y')
    dateS = datetime.strftime(dateObj,'%Y%m%d %X')
    # print(datetime.strftime(dateObj,'%Y%m%d %X'))

    print("Time: ",dateS)

    p = subprocess.Popen(["owread", "26.241E9D010000/temperature"], stdout=subprocess.PIPE)

    (temp,errcode) = p.communicate()
    print("Temp: ", float(temp))

    p = subprocess.Popen(["owread", "26.241E9D010000/humidity"], stdout=subprocess.PIPE)

    (output,errcode) = p.communicate()
    #print(output)

    humid = float(output)
    print("Moisture: ", humid)

    if humid < 200 and humid > 10:
        print('okay')
        red.off()
        gr.on()
    else :
        print('dry');
        gr.off();
        red.on()

    therow=(dateS,float(temp),float(humid))
    # print(therow)
    
    f = open('test.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(therow)
    sleep(60)

close(f)
