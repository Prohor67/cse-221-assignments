input_file = open('input4.txt','r')
first = input_file.readline().split(" ")
size = int(first[0])
people = int(first[1].rstrip("\n"))
timeset = input_file.readlines()
for i in range(len(timeset)):
    timeset[i] = timeset[i].rstrip("\n")

timeset = [tuple([int(x.split(" ")[0]),int(x.split(" ")[1])]) for x in timeset]


def data_formatting(data):
  for i in range(len(data)-1):
    for j in range(i+1,len(data)):
      if int(data[i][1])>int(data[j][1]):
        data[i],data[j] = data[j],data[i]
  return data


def multi_schedule(data,user):
  count = user
  for i in range(user):
    new = []
    skip = 0
    for j in range(len(data)-1):
      if j != 0 and j == skip:
        continue
      for k in range(j+1,len(data)):
        if data[j][1]<=data[k][0]:
          count+=1
          break
        else:
          skip = k
          new.append(data[k])
    data = new
  return str(count)


timeset = data_formatting(timeset)
counter = multi_schedule(timeset,people)



output_file = open('output4.txt','w')
output_file.write(counter)