import RPi.GPIO as GPIO
import time



s2 = 23
s3 = 24
signal = 25
NUM_CYCLES = 10


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setwarnings(False)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")
  
def mapping(i,n,m,p,q):
  x=(i+q-m)/((n-m)/(p-q))
  return(x)

def redf():
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    suma=0
    for i in range(5):
      start = time.time()
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start  
      suma=suma+ NUM_CYCLES / duration   
    red=mapping(suma/5,24000,13000,255,0)
    return(red)

def bluef():
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    suma=0
    for i in range(5):
      start = time.time()
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start
      suma = suma+NUM_CYCLES / duration
    blue=mapping(suma/5,27000,20000,255,0)
    return (blue)

def greenf():
    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    suma=0;
    for i in range(5):
      start = time.time()    
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start
      suma = suma+ NUM_CYCLES / duration
    green=mapping(suma/5,21000,16000,255,0)
    return (green)

def whitef():
    suma=(redf()+bluef()+greenf())/3
    return (mapping(suma,255,0,150,0)
            
def nitrogen():
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    suma=0
    for i in range(5):
      start = time.time()
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start      #seconds to run for loop
      suma=suma+ NUM_CYCLES / duration   #in Hz
    red=mapping(suma/5,24000,13000,40,0)
    return(red)

def phosphorous():
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    suma=0
    for i in range(5):
      start = time.time()
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start
      suma = suma+NUM_CYCLES / duration
    blue=mapping(suma/5,27000,20000,45,0)
    return (blue)

def loop():
    print("The test result of nitrogen is "+nitrogen())
    input()
    print("\n\n The result of Phosphorous is"+ phosphorous())
    input()
    print("\n\n The result of Potassium is " + whitef())
    input()    

def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
