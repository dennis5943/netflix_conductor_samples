from __future__ import print_function
from conductor.ConductorWorker import ConductorWorker,TaskStatus

def task_5(task):

    print('================================================')
    print('task_5:接到工作',task)
    
    return ConductorWorker.task_result(
        status=TaskStatus.COMPLETED,
        output= {"status":"Send OK","valAddOne":30},
        logs=['one','two','tree']
    )

class Task6Worker(ConductorWorker):
    def __init__(self, server_url, thread_count, polling_interval, worker_id=None):
        super().__init__(server_url, thread_count, polling_interval, worker_id)

        self.maxCount = 3
        pass

    def task_6(self,task):
        print('================================================')
        print("callback after 20 sec,remain counts:",self.maxCount)

        if self.maxCount:
            res = ConductorWorker.task_result(
                    status=TaskStatus.IN_PROGRESS,
                    output= {"status":"Send OK","valAddOne":30,"maxCount":self.maxCount},
                    logs=['one','two','tree']
                )
            res['callbackAfterSeconds'] = 20
            self.maxCount -= 1
        else:
            res = ConductorWorker.task_result(
                    status=TaskStatus.COMPLETED,
                    output= {"status":"Send OK","valAddOne":30,"maxCount":self.maxCount},
                    logs=['one','two','tree']
                )
            res['callbackAfterSeconds'] = 20
        return res

def main():
    print('Starting Kitchensink workflows')
    cc = ConductorWorker('http://localhost:8080/api', 1, 0.1)
    cc.start('task_5', task_5, False)
    
    task6 = Task6Worker('http://localhost:8080/api', 1, 0.1)
    task6.start('task_6', task6.task_6, True)

if __name__ == '__main__':
    main()
