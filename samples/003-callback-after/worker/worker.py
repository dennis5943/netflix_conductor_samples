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

def task_6(task):
    print('================================================')
    print("callback after 60 sec",task)
    
    return ConductorWorker.task_result(
        status=TaskStatus.IN_PROGRESS,
        output= {"status":"Send OK","valAddOne":30},
        logs=['one','two','tree'],
        reasonForIncompletion='',
        callbackAfterSeconds=10
    )

def main():
    print('Starting Kitchensink workflows')
    cc = ConductorWorker('http://localhost:8080/api', 1, 0.1)
    cc.start('task_5', task_5, False)
    cc.start('task_6', task_6, True)

if __name__ == '__main__':
    main()
