input_file = open('input2.txt','r')
size = input_file.readline()
arr = input_file.readline().split(" ")
arr = [int(x) for x in arr]

def Max_finder(arr):
  if len(arr)<=1:
    return arr
  else:
    mid = len(arr)//2
    a = Max_finder(arr[:mid:])
    b = Max_finder(arr[mid::])
  if a>b:
    return a
  else:
    return b

str_out = str(Max_finder(arr)[0])  

output = open('output2.txt','w')
output.write(str_out)