input_file = open('input4.txt','r')
size = int(input_file.readline())
arr = input_file.readline().split(" ")
arr = [int(x) for x in arr]

def divide_and_conquer(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    Left = divide_and_conquer(arr[:mid])
    Right = divide_and_conquer(arr[mid:])

    if Left > Right:
      return Left
    else:
      return Right   

def max_pair_finder(arr,n):
  max_pair = 0
  for i in range(n - 1):
    x = arr[i]
    merge_value = divide_and_conquer(arr[i + 1:])[0]
    if i == 0:
      max_pair = x + (merge_value**2)
    else:  
      max_pair = max(max_pair, (x + (merge_value**2)))
  return max_pair

result = str(max_pair_finder(arr,size))
output = open('output4.txt','w')
output.write(result)