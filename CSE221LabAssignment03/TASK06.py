input_file = open('input6.txt','r')
size = int(input_file.readline()[0])
arr = input_file.readline().split(" ")
arr = [int(x) for x in arr]
query_size = int(input_file.readline()[0])
query = input_file.readlines()
query = [int(x.rstrip("\n")) for x in query]

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


def Kth_smallest(arr,low,high,k):
  if low == high:
    return arr[low]
  pos = Partition(arr,low,high)
  i = pos - low + 1

  if i == k:
    return arr[pos]
  elif i>k:
    return Kth_smallest(arr, low, pos-1, k)
  else:
    return Kth_smallest(arr, pos+1, high, k-i)   

str_out = ""
for i in query:
  str_out += str(Kth_smallest(arr,0,size-1,i))+"\n"

output = open('output6.txt','w')
output.write(str_out)  
