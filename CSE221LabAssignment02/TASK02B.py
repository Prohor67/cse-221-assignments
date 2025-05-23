input_file = open('input2B.txt','r')
first_list_size = input_file.readline()
first_list = input_file.readline().split(" ")
first_list[len(first_list)-1] = first_list[len(first_list)-1].rstrip("\n")
second_line_size = input_file.readline()
second_list = input_file.readline().split(" ")
second_list[len(second_list)-1] = second_list[len(second_list)-1].rstrip("\n")


def combine_list(first_list,second_List):
    new = []
    pointer1 = 0
    pointer2 = 0
    while pointer1 <= len(first_list)-1  and pointer2 <=len(second_List)-1:
        if int(first_list[pointer1]) < int(second_List[pointer2]) :
            new.append(first_list[pointer1])
            pointer1+=1
        else:
            new.append(second_List[pointer2])
            pointer2+=1
    if pointer1 == len(first_list):
        new.extend(second_List[pointer2:])
    else:
        pass
        new.extend(first_list[pointer1:])
    return new

combined_list = combine_list(first_list,second_list)
str_out = ""
for i in combined_list:
    str_out+= i+" "
output_file = open("output2B.txt",'w')
output_file.write(str_out)