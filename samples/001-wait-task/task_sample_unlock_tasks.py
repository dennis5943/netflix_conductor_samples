import requests
import json

res = requests.get("http://localhost:8080/api/workflow/running/system_task_test",headers={"accept":"*/*"})
if res.status_code == 200:
    wids = json.loads(res.text)

def unlockWaitTask(wid):
    res = requests.get("http://localhost:8080/api/workflow/{}?includeTasks=true".format(wid),headers={"accept":"*/*"})
    tasks = [{
                "workflowInstanceId":x['workflowInstanceId'] ,
                "taskId":x['taskId']
            }
            for x in json.loads(res.text)['tasks'] if x['referenceTaskName'] == 'wait_task' and x['status'] == 'IN_PROGRESS']

    for task in tasks:
        data = {
                "workflowInstanceId": task['workflowInstanceId'],
                "taskId": task['taskId'],
                "reasonForIncompletion" : "If failed, reason for failure",
                "callbackAfterSeconds": 0,
                "status": "COMPLETED",
                "outputData": {
                    "result":"OKOK"
                }
            }
        headers = {"accept": "text/plain" ,"Content-Type": "application/json"}

        res = requests.post('http://localhost:8080/api/tasks',data=json.dumps(data),headers=headers)
        print(res.status_code,data,headers)

for wid in wids:
    unlockWaitTask(wid)


"""
Ending a WAIT
To conclude a WAIT task, there are three endpoints that can be used. You'll need the workflowId, taskRefName or taskId and the task status (generally COMPLETED or FAILED).

POST /api/tasks
POST api/queue/update/{workflowId}/{taskRefName}/{status}
POST api/queue/update/{workflowId}/task/{taskId}/{status}


curl -X 'POST' \
  'http://localhost:8080/api/tasks' \
  -H 'accept: text/plain' \
  -H 'Content-Type: application/json' \
  -d '{
    "workflowInstanceId": "6dc0a4a2-3d5c-4c77-89e3-b2b480455e08",
    "taskId": "86aa325a-b718-4771-908e-98b2be233047",
    "reasonForIncompletion" : "If failed, reason for failure",
    "callbackAfterSeconds": 0,
    "status": "COMPLETED",
    "outputData": {
        "result":"OKOK"
    }

}'
"""