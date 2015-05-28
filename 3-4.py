def get_cycles_num(num2):
    num=str(num2)
    nub_bits=[]
    for i in range(0,len(num)):
        nub_bits.append(num[i])
    cycles_list=[]
    list_len=len(nub_bits)
    while(list_len):
        nub_bits.append(nub_bits[0])
        nub_bits.pop(0)
        cycles_num=''.join(nub_bits)
        cycles_list.append(int(cycles_num))
        list_len=list_len-1
    return cycles_list
endnum=input()
total=0
for i in range(2,endnum+1):
    for j in range(2,(i/2+1)):
        if i%j==0:
            break
    else:
        if i>10:
            i_cycle=get_cycles_num(i)
            temp_cycle=[]
            for x in i_cycle:
                for y in range(2,x/2+1):
                    if x%y==0:
                        break
                else:
                    temp_cycle.append(x)
            if len(temp_cycle)==len(i_cycle):
                total+=1
        else:
            total+=1
print total