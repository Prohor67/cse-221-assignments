
input_file = open('input5.txt','r')
size = int(input_file.readline())
arr = input_file.readline().split(" ")
arr = [int(x) for x in arr]

def Partition(arr,low,high):
  pivot = arr[high]
  i = low-1
  for j in range(low,high):
    temp = 0
    if arr[j]<=pivot:
      i+=1
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
  temp2 = arr[high]
  arr[high] = arr[i+1]
  arr[i+1] = temp2
  return i+1 

def Quicksort(arr,low,high):
  if low < high:
    part = Partition(arr,low,high)
    Quicksort(arr,low,part-1)
    Quicksort(arr,part+1,high)

Quicksort(arr,0,size-1)
str_out = ""
for i in arr:
  str_out+= str(i)+" "
output = open('output5.txt','w')
output.write(str_out)