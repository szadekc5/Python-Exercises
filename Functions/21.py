from time import sleep

def delay():
    print("Printing after delay..")


miliseconds = float(input("Enter Delay in Miliseconds : "))
sleep(miliseconds / 1000)
delay()
