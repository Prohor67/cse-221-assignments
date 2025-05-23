#Reading and formatting the text file
file_object = open('input1a.txt','r')
T = file_object.readline()
items = file_object.readlines()
for i in range(T):
  items[i] = int(items[i].rstrip('\n'))


# Function to determine Odd and Even
def odd_even(num):
  if num%2 ==0:
    return f"{num} is an Even number"
  else:
    return f"{num} is an Odd number"
  

#Writting the result on a text file
file_output_object = open('output1a.txt','w')
str_a= ""
for i in items:
  str_a += odd_even(i)+'\n'

file_output_object.write(str_a)
