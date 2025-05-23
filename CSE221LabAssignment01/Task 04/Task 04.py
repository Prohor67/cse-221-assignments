
#Reading and Formating the input text file
file_object = open('input4.txt','r')
item_no = int(file_object.readline())

name = []
time = []
location = []
for i in range(item_no):
  breakdown = file_object.readline().split(" ")
  name.append(breakdown[0])
  time.append(breakdown[6].rstrip("\n"))
  location.append(breakdown[4])


# Function to parse the time string and convert it to comparable data
def parse_time(time_str):
  time_split = time_str.split(":")
  hour = int(time_split[0])
  minute = int(time_split[1])
  return hour+minute

#Used Selection Sort for sorting the data
def sorted_train(item_no,name,time,location):
  for i in range(item_no-1):
    min_idx =i
    for j in range(i+1,item_no):
      #Comparing name in ascending order
      if name[min_idx] > name[j]:
        min_idx = j
      #If the names are equal we are comparing the times  
      elif name[min_idx] == name[j]:    
        #Comparing time in descending order            
        if parse_time(time[min_idx]) < parse_time(time[j]) :
          min_idx = j
    temp = name[i]
    temp2 = time[i]
    temp3 = location[i] 
    name[i] = name[min_idx]
    time[i] = time[min_idx]
    location[i] = location[min_idx]
    name[min_idx] = temp
    time[min_idx] = temp2
    location[min_idx] = temp3
  
  #No need to check who came first if the time and name are both equal as they will automatically place them selves that way
  #returning all the arrays in a tuple
  return (name,time,location) 

#Writting the output on the text file
file_output_object = open('output4.txt','w')
str_a = ""
name,time,location = sorted_train(item_no,name,time,location)
for i in range(item_no):
  str_a+= f"{name[i]} will departure for {location[i]} at {time[i]}\n"
file_output_object.write(str_a)
