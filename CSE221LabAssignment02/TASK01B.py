input_file = open('input1B.txt','r')
first = input_file.readline().split(" ")
size = int(first[0])
target = int(first[1].rstrip("\n"))
arr = input_file.readline().split(" ")
for i in range(len(arr)):
  arr[i] = int(arr[i].rstrip("\n"))


def summation(size,arr,target):
  pointer1 = 0
  pointer2 = len(arr)-1
  flag = False
  while (pointer1<pointer2):
    if arr[pointer1]+arr[pointer2] == target:
      str_pr = str(pointer1+1)+" "+str(pointer2+1)
      flag = True
      break
    elif arr[pointer1]+arr[pointer2] < target:
      pointer1+=1
    else:
      pointer2-=1
  if flag == False:
    return "Impossible"
  else:
    return str_pr
  

result = summation(size,arr,target)
print(result)
output_file = open('output1B.txt','w')
output_file.write(result)