import json
from model import Queue, Process

class ori_data():

    def queue():
        with open("test_data.json", 'r') as reader:
            ori_json = json.loads(reader.read())
        queue_ori = ori_json["queue"]
        queue_list = []

        for i in range(0, len(queue_ori)):
            q = queue_ori[i]
            queue = Queue(qid=i+1, qtype=q["qtype"],
                          run_limit=q["run_limit"], time_quantum=q["time_quantum"])
            queue_list.append(queue)
        return queue_list

    def process():
        with open("test_data.json", 'r') as reader:
            ori_json = json.loads(reader.read())
        process_ori = ori_json["process"]
        process_queue = []
        x = 1
        for i in range(0, len(process_ori)):
            process_list = []
            for q in range(0, len(process_ori[i])):
                p = process_ori[i][q]
                process = Process(pid=x, priority=p["priority"], export=False,
                                  time=p["time"], run_times=0, status=("PID:"+str(x)+"  "))
                process_list.append(process)
                x+=1
            process_queue.append(process_list)
        return process_queue