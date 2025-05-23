input_file = open("input3.txt",'r')
size = int(input_file.readline())
data = input_file.readlines()
for i in range(len(data)):
  data[i] = data[i].rstrip("\n")
  
def data_formatting(data):
  for i in range(len(data)-1):
    for j in range(i+1,len(data)):
      if int(data[i][2:])>int(data[j][2:]):
        data[i],data[j] = data[j],data[i]
  return data

def schedule(size,arr):
  str_a = f"{arr[0]}\n"
  count = 1
  skip = 0
  for i in range(size-1):
    if i !=0 and i == skip  :
      continue
    for j in range(i+1,size):
      if int(arr[i][2]) <= int(arr[j][0]):
        count+=1
        str_a+=f"{arr[j]}\n"
        break
      else:
        skip = j
  final =str(count)+"\n"+str_a
  return final

data = data_formatting(data)
final_schedule = schedule(size,data)

output_file = open('output3.txt','w')
output_file.write(final_schedule)