export APIHOST=localhost:8080

echo "$APIHOST"

# remove exist workflow first
curl -X 'DELETE' \
  "http://$APIHOST/api/metadata/workflow/callback_after_test/1" \
  -H 'accept: */*'


# create workflow
curl -X 'POST' \
  "http://$APIHOST/api/metadata/workflow" \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "callback_after_test",
  "description": "延遲測試",
  "version": 1,
  "tasks": [
    {
      "name": "task_5",
      "taskReferenceName": "send-reqeust",
      "inputParameters": {},
      "type": "SIMPLE",
      "decisionCases": {},
      "defaultCase": [],
      "forkTasks": [],
      "startDelay": 0,
      "joinOn": [],
      "optional": false,
      "defaultExclusiveJoinTask": [],
      "asyncComplete": false,
      "loopOver": []
    },
    {
      "name": "task_6",
      "taskReferenceName": "wait-response",
      "inputParameters": {
        "valAddOne": "${send-reqeust.output.valAddOne}"},
      "type": "SIMPLE",
      "decisionCases": {},
      "defaultCase": [],
      "forkTasks": [],
      "startDelay": 0,
      "joinOn": [],
      "optional": false,
      "defaultExclusiveJoinTask": [],
      "asyncComplete": false,
      "callbackAfterSeconds": 10,
      "loopOver": []
    }
  ],
  "inputParameters": [],
  "outputParameters": {},
  "schemaVersion": 2,
  "restartable": true,
  "workflowStatusListenerEnabled": false,
  "ownerEmail": "example@email.com",
  "timeoutPolicy": "ALERT_ONLY",
  "timeoutSeconds": 0,
  "variables": {},
  "inputTemplate": {}
}'

echo 'initialzation complete'