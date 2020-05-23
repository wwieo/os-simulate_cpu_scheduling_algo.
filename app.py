from data_init import ori_data
from function import addStatus, output, truncateResult

truncateResult()
queue = ori_data.queue()
process = ori_data.process()    

n = 0
while(n<len(queue)):
    if(queue[n].qtype == "PRR"):
        process[n] = sorted(process[n], key = lambda p: p.priority)
        maxPriority = max(process[n], key = lambda p: p.priority).priority + 1        
        minPriority = min(process[n], key = lambda p: p.priority).priority        

        while(minPriority<maxPriority):
            for q in range(len(process[n])):
                pro = process[n][q]
                if(pro.priority == minPriority):
                    pro.run_times+=1
                    if(pro.time > queue[n].time_quantum):     
                        pro.time -= queue[n].time_quantum                       
                        pro.status = addStatus(pro.status, queue[n].qid, queue[n].time_quantum)
                    elif(pro.export is False):
                        pro.status = addStatus(pro.status, queue[n].qid, pro.time)
                        pro.time = 0
                        pro.export = True
                        print(pro.status) 
                        output(pro.status) 

            x = True
            for q in range(len(process[n])):
                pro = process[n][q]
                if(pro.priority == minPriority):
                    if(pro.run_times < queue[n].run_limit):
                        x = False
            if(x):
                minPriority+=1

        for q in range(len(process[n])):
            if(process[n][q].time>0):
                process[n][q].run_times = 0
                process[n+1].append(process[n][q])
            
    if(queue[n].qtype == "RR"):
        queueLimit = True
        while(queueLimit):
            queueLimit = False
            for q in range(len(process[n])):
                pro = process[n][q]
                if(pro.time > queue[n].time_quantum):     
                    pro.time -= queue[n].time_quantum                       
                    pro.status = addStatus(pro.status, queue[n].qid, queue[n].time_quantum)
                elif(pro.export is False):
                    pro.status = addStatus(pro.status, queue[n].qid, pro.time)
                    pro.time = 0
                    pro.export = True
                    print(pro.status)                   
                    output(pro.status) 
                     
                pro.run_times+=1
                if(pro.run_times<queue[n].run_limit):
                    queueLimit = True
        for q in range(len(process[n])):                
            if(process[n][q].time>0):
                process[n][q].run_times = 0
                process[n+1].append(process[n][q])
    
    if(queue[n].qtype == "SJF"):
        process[n] = sorted(process[n], key = lambda p: p.time)
        for i in range(len(process[n])):
            pro = process[n][i]
            pro.status = addStatus(pro.status, queue[n].qid, pro.time)
            print(pro.status)  
            output(pro.status) 

    n+=1
    