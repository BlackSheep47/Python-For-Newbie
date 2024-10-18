import time

M_time = int(input("Enter the time in Sec: "))

for x in reversed(range(0, M_time)):
    seconds = x % 60  
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # : format specifier 
    time.sleep(1)
    
print("Game Over!")
