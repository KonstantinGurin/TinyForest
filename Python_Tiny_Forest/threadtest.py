import threading
import time
#import gpio w/e
#setup GPIO
def thread_moisture(asd):
    gpio = 0
    key = True
    while key:
        time.sleep(0.5)
        
        print("checking moisture")
        
        time.sleep(0.5)
        if int(gpio) == 1:
            print("LOW")
            #gpio = random.randint(0,2)
        if int(gpio) == 0:
            print("HIGH")
            #gpio = random.randint(0,2)
            
        time.sleep(0.5)


class sensor:
    
    
    first = ""
    def __init__ (self):
        self.first = "sensor"

    def print(self):
        print("sensor print = ",self.first)

obj = sensor()

obj.print()
    

if __name__ == "__main__":

    begin = threading.Thread(target=thread_moisture, args=(1,))

    #begin2 = threading.Thread(target=thread_temp, args=(1,))
    
    begin.start()
    #begin2.start()
    print("main method print")
