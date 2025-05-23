#Reading and formating the input text file 
file_object = open('input2.txt','r')

size = int(file_object.readline())
nums = file_object.readline()
nums = nums.split(" ")
for i in range(len(nums)):
  nums[i] = int(nums[i])


#Optimized O(n^2) Bubblesort Algorithm
def BubbleSort(arr):
  #looping for each element                                                   
  for i in range(size-1):
    #flag to keep track of swapping
    flag = False
    #looping to compare elements
    for j in range(i+1,size): 
      #changing the elements in ascending order by swapping
      if arr[i] > arr[j]:
          Temp = arr[j] 
          arr[j] = arr[i] 
          arr[i] = Temp
          flag = True
    #No swapping means the array is already sorted      
    if flag == False:
      break
  return arr


#Writting the file on the text file
file_output_object = open('output2.txt','w')
str_a = ""
result = BubbleSort(nums)
for i in result:
  str_a+= str(i)+" "

file_output_object.write(f"Sorted Numbers: {str_a}")