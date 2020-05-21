
class Queue(object):
    def __init__(self, qid:int, qtype:str, 
                 run_limit:int, time_quantum:int) -> None:
        self.qid = qid
        self.qtype = qtype
        self.run_limit = run_limit
        self.time_quantum = time_quantum

class Process(object):
    def __init__(self, qid:int, pid:int,
                 priority:int, time:int) -> None:
        self.qid = qid
        self.pid = pid
        self.priority = priority
        self.time = time