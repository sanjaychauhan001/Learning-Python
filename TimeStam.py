import time
 
timestamp = int(time.strftime("%H")) 
print(timestamp)
print("enter your name")
name = input()
if(timestamp >= 0 and timestamp<12):
    print("hey" , name, "good morning")
elif(timestamp >= 12 and timestamp < 17):
    print("hey" , name , "good afternoon")    
elif(timestamp >= 17 and timestamp < 21):
    print("hey" , name , "good evening")    
else:
    print("hey", name , "good night")    

