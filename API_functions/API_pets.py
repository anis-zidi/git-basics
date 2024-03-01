import requests

def getPetById(url):
    response = requests.get(url,verify=False)
    return response

def postAPIDate(url, body):
    headers = {"Content-Type" : "application/json"}
    return requests.post(url,json=body, headers=headers)
