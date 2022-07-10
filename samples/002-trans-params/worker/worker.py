from __future__ import print_function
from conductor.ConductorWorker import ConductorWorker,TaskStatus

def task_5(task):

    print('================================================')
    print('task_5:接到工作',task)
    
    return ConductorWorker.task_result(
        status=TaskStatus.COMPLETED,
        output= {'workflow_input': int(task["inputData"]["workflow_input"]), 'valAddOne': 1 + int(task["inputData"]["workflow_input"])},
        logs=['one','two','tree']
    )

def task_6(task):
    print('================================================')
    print('workflow_input is ',task["inputData"]["workflow_input"])
    print('valAddOne from task 5 output is ',task["inputData"]["valAddOne"])
    
    return ConductorWorker.task_result(
        status=TaskStatus.COMPLETED,
        output= {'valAddOne': int(task["inputData"]["valAddOne"])},
        logs=['one','two','tree']
    )

def main():
    print('Starting Kitchensink workflows')
    cc = ConductorWorker('http://localhost:8080/api', 1, 0.1)
    cc.start('task_5', task_5, False)
    cc.start('task_6', task_6, True)

if __name__ == '__main__':
    main()
