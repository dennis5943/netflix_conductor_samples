from __future__ import print_function
from conductor.ConductorWorker import ConductorWorker,TaskStatus


def task_before_wait(task):
    print('================================================')
    print('task_before_wait:接到工作',task)
    
    forkTasks = [{"name": "task_1", "taskReferenceName": "task_1_1", "type": "SIMPLE"},{"name": "sub_workflow_4", "taskReferenceName": "wf_dyn", "type": "SUB_WORKFLOW", "subWorkflowParam": {"name": "sub_flow_1"}}];
    input = {'wait_task': {}, 'wf_dyn': {}}
    return {'status': 'COMPLETED', 'output': {'mod': 5, 'taskToExecute': 'wait_task', 'oddEven': 0, 'dynamicTasks': forkTasks, 'inputs': input}, 'logs': ['one','two']}

def wait_task(task):
    print('================================================')
    print('wait_task:接到工作',task)
    
    forkTasks = [{"name": "task_1", "taskReferenceName": "task_1_1", "type": "SIMPLE"},{"name": "sub_workflow_4", "taskReferenceName": "wf_dyn", "type": "SUB_WORKFLOW", "subWorkflowParam": {"name": "sub_flow_1"}}];
    input = {'wait_task': {}, 'wf_dyn': {}}
    return {'status': 'COMPLETED', 'output': {'mod': 5, 'taskToExecute': 'wait_task', 'oddEven': 0, 'dynamicTasks': forkTasks, 'inputs': input}, 'logs': ['one','two']}


def main():
    hosturl = "http://192.168.1.3"
    print('Starting Kitchensink workflows')
    cc = ConductorWorker('{}:8080/api'.format(hosturl), 1, 0.1)
    cc.start('task_before_wait',task_before_wait, False)
    cc.start('wait_task',wait_task, True)
    

if __name__ == '__main__':
    main()
    print('process end')