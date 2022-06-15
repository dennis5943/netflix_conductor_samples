import requests

res = requests.post("http://localhost:8080/api/queue/update/40531d26-37d7-4342-8dc7-02892b2d8731/task/wait_task/COMPLETED")
print(res.status_code,res.text)

"""
Ending a WAIT
To conclude a WAIT task, there are three endpoints that can be used. You'll need the workflowId, taskRefName or taskId and the task status (generally COMPLETED or FAILED).

POST /api/tasks
POST api/queue/update/{workflowId}/{taskRefName}/{status}
POST api/queue/update/{workflowId}/task/{taskId}/{status}


http://localhost:5000/api/workflow/ce2ec307-ae02-4dd2-bda6-397263e4477e
http://localhost:5000/api/queue/update/e1a3018e-6078-43b4-a57d-ed617605fc90/wait_task/COMPLETED
http://localhost:5000/api/queue/update/e1a3018e-6078-43b4-a57d-ed617605fc90/task/wait_task/COMPLETED


curl -H "Content-Type: application/json" -X POST http://localhost:5000/api/queue/update/e1a3018e-6078-43b4-a57d-ed617605fc90/wait_task/COMPLETED
"""