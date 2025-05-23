input_file = open('input2A.txt','r')
first_list_size = input_file.readline()
first_list = input_file.readline().split(" ")
first_list[len(first_list)-1] = first_list[len(first_list)-1].rstrip("\n")
second_line_size = input_file.readline()
second_list = input_file.readline().split(" ")
second_list[len(second_list)-1] = second_list[len(second_list)-1].rstrip("\n")

first_list.extend(second_list)
first_list.sort()

str_out = ""
for i in first_list:
    str_out+= str(i)+" "
output_file = open("output2A.txt",'w')
output_file.write(str_out)