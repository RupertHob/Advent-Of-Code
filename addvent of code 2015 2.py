my_list = []
tc = 'True'
     
while tc == 'True':
    val=(str(input("Enter elements : ")))
    if val== 'stop': 
        tc = 'False' 
    else:
         my_list.append(str(val))
# if the input is not-integer, just print the list
print(my_list)

ttwp=0
ttrbn=0
for x in my_list:
    arry = []
    parry = []
    smol = ''
    wrp = ''
    rbn = 0
    bow = 0
    arry = x.split('x')
    wrp = (2*(int(arry[0])*int(arry[1])))+(2*(int(arry[1])*int(arry[2])))+(2*(int(arry[2])*int(arry[0])))
    rbn = (2*(int(arry[0]))+ 2*(int(arry[1])))
    if (2*(int(arry[0]))+2*(int(arry[2]))) < rbn:
         rbn = (2*(int(arry[0]))+2*(int(arry[2])))
    if (2*(int(arry[1]))+2*(int(arry[2]))) < rbn:
        rbn = (2*(int(arry[1]))+2*(int(arry[2])))
    bow = (int(arry[0])*int(arry[1])*int(arry[2]))
    parry[0:2]=(int(arry[0])*int(arry[1]),int(arry[1])*int(arry[2]),(int(arry[2])*int(arry[0])))
    parry.sort()
    smol=((parry[0]))
    ttrbn+=(rbn+bow)
    ttwp+=(smol+wrp)

next
print('Total Bow=' +str(rbn))
print ('total around =' +str(bow))
print ('total Ribbon =' +str(ttrbn))
print('total wrapping paper = ' + str(ttwp))