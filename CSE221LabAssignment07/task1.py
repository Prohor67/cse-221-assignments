def initialization(n):
    individuals = []
    for i in range(n+1):
        individuals.append(i)  
    size = [1] * (n + 1) 

    return individuals, size


def finding_person(given, individuals):
    if individuals[given] == given: 
        return given
    individuals[given] = finding_person(individuals[given], individuals)  
    return individuals[given]


def union(person_1, person_2, individuals, size):
    root_1 = finding_person(person_1, individuals)
    root_2 = finding_person(person_2, individuals)
    if root_1 != root_2:  
        if size[root_1] < size[root_2]:  
            individuals[root_1] = root_2
            size[root_2] += size[root_1]
        else:
            individuals[root_2] = root_1
            size[root_1] += size[root_2]


input_file =open("input1.txt", "r")
output_file=open("output1.txt", "w") 
N, K = map(int, input_file.readline().split())
individuals, size = initialization(N)
while K!=0:
    friends = list(map(int, input_file.readline().split()))
    union(friends[0], friends[1], individuals, size)
    output_file.write(str(size[finding_person(friends[0], individuals)]) + "\n")
    K-=1
