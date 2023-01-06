#show all teachers
lines = []
with open("temp.txt") as temp:
    for line in temp:
        lines.append(line)
for line in lines:
    print(line)
#show all english teachers
for line in lines:
    sub=line.split('-')[1]
    if(sub=='English'):
        print(line)


#show all teachers whose salary is more than 2000

#show all teachers who Math english and salary is more than 2000