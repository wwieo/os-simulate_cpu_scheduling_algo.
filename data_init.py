import json
from model import Queue, Process


class ori_data():
    def queue():
        with open('test_data.json' , 'r') as reader:
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
        with open('test_data.json' , 'r') as reader:
            ori_json = json.loads(reader.read())
        process_ori = ori_json["process"]
        process_list = []

        for i in range(0, len(process_ori)):
            for q in range(0, len(process_ori[i])):
                p = process_ori[i][q]
                process = Process(qid=i+1, pid=q+1,
                                  priority=p["priority"], time=p["time"])
        return process_list