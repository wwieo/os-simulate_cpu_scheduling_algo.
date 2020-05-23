def truncateResult():
    with open('result.txt','a') as r:
        r.truncate(0)

def output(status):
    with open('result.txt','a') as r:
        r.write(status+"\n")

def addStatus(status, qid, time):
    rstString = " Queue"+str(qid)+": "
    if rstString not in status:
        status += (rstString+str(time))
    else:
        status += (","+str(time))
    return status
