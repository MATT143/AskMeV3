import json,requests
from .models import MasterTasks

def statusCallbackRequestPayload(obj):
    requestPayload={"quest_id":obj.quest_id,"solution":obj.answer}
    return requestPayload

def StatusCallBack(obj):
    request=json.dumps(statusCallbackRequestPayload(obj))
    url='http://localhost:8000/post/solution/sync'
    response=requests.post(url=url, data=request, headers={'Content-type': 'application/json'})
    return response



