
class Queue(object):
    def __init__(self, qid:int, qtype:str, 
                 run_limit:int, time_quantum:int) -> None:
        self.qid = qid
        self.qtype = qtype
        self.run_limit = run_limit
        self.time_quantum = time_quantum

class Process(object):
    def __init__(self, pid:int, priority:int, export: bool,
                 time:int, run_times:int, status:str) -> None:
        self.pid = pid
        self.priority = priority
        self.export = export
        self.time = time
        self.run_times = run_times
        self.status = status