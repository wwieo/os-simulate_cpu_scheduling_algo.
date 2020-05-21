from data_init import ori_data

queue = ori_data.queue()
process = ori_data.process()    

check = True
while(check):



    check = False
    for i in range(len(process)):
        if process[i].time > 0:
            check = True
    check = False #test