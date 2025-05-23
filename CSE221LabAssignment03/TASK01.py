input_file = open('input1.txt','r')
size = input_file.readline()
arr = input_file.readline().split(" ")
arr = [int(x) for x in arr]

def merge(a,b):
  a.extend(b)
  a.sort()
  return a

def mergesort(arr):
  if len(arr)<=1:
    return arr
  else:
    mid = len(arr)//2
    a = mergesort(arr[:mid:])
    b = mergesort(arr[mid::])
  return merge(a,b)

sorted_arr = mergesort(arr)
str_out =" "
for i in sorted_arr:
  str_out += str(i)+" "
output = open('output1.txt','w')
output.write(str_out)