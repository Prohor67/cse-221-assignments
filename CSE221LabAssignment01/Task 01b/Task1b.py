#Reading and formatting the text from the input text file
file_object = open('input1b.txt','r')
size = file_object.readline()
input_text= file_object.readlines()
for i in range(len(input_text)):
  input_text[i] = input_text[i].lstrip('calculate ').rstrip('\n')
 


#Function for the solution
def calculator(op):
  new_op = op.split()
  result = 0
  if new_op[1] == "+":
    result = int(new_op[0])+int(new_op[2])
  elif new_op[1] == "-":
    result = int(new_op[0])-int(new_op[2])
  elif new_op[1] == "*":
    result = int(new_op[0])*int(new_op[2])
  else:
    result = int(new_op[0])/int(new_op[2])
  return f"The result of {op} is {result}"


#Writting the result on the text file
file_output_object = open('output1b.txt','w')
str_a= ""
for i in input_text:
  str_a += calculator(i)+'\n'

file_output_object.write(str_a)