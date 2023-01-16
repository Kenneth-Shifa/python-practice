#show all teachers
lines = []
with open("temp.txt") as temp:
    for line in temp:
        lines.append(line)

#show all english teachers
for line in lines:
    sub = line.split('-')[1]
    if(sub == 'English'):
        print(line)


#show all teachers whose salary is more than 2000
for line in lines:
    pay=line.split('-')[2]
    if(pay>'2000'):
        print(line)

#show all teachers who Math english and salary is more than 2000
for line in lines:
    sub=line.split('-')[1]
    pay = line.split('-')[2]
    if(sub=="English" or sub=="Math") and (pay > '2000'):
        print(line)
