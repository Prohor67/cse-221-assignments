#Reading and formating the text file for input
file_object = open('input3.txt','r')
item_no = int(file_object.readline())
ID = file_object.readline().split(" ")
Mark = file_object.readline().split(" ")
for i in range(item_no):
  ID[i] = int(ID[i])
  Mark[i] = int(Mark[i])
  

#Used Selection Sort for the solution
def sorted_marks(item_no,ID,Mark):
  for i in range(item_no-1):
    #max_id
    max_idx = i
    for j in range(i+1,item_no):
      #Comparing marks
      #Mark in Descending Order
      if Mark[max_idx] < Mark[j]:
        max_idx = j    
      #If the marks are equal, then comparing the ID  
      elif Mark[max_idx] == Mark[j]:
        #ID in Ascending order
        if ID[max_idx]>ID[j]:
          max_idx = j
  
    temp = Mark[i]
    temp2 = ID[i] 
    Mark[i] = Mark[max_idx]
    ID[i] = ID[max_idx]
    Mark[max_idx] = temp
    ID[max_idx] = temp2  
   #returning both arrays in a tuple   
  return (ID,Mark)
  
#Writting the output on the text file
file_output_object = open('output3.txt','w')
str_a = ""
ID,Mark = sorted_marks(item_no, ID, Mark)   
for i in range(item_no):
  str_a+=f"ID: {str(ID[i])} Mark: {str(Mark[i])}\n"
file_output_object.write(str_a)
