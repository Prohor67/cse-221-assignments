input_file = open('input1A.txt','r')
first = input_file.readline().split(" ")
size = int(first[0])
target = int(first[1].rstrip("\n"))
arr = input_file.readline().split(" ")
for i in range(len(arr)):
  arr[i] = int(arr[i].rstrip("\n"))


def summation(size,arr,target):
  flag= False
  for i in range(size-1):
    for j in range(i+1,size):
      if arr[i]+arr[j] == target:
        str_a = str(i+1)+" "+str(j+1)
        flag = True
        break
  if flag==False:
    return "Impossible"
  else:
    return str_a

result = summation(size,arr,target)

output_file = open('output1A.txt','w')
output_file.write(result)