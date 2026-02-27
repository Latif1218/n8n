import requests

user_message = "Hi, Can you tell me about black holes in 3-4 lines?"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/047d4b03-b718-495f-b8b3-5b2383aeaf46"

response = requests.post(url, json=request_message)
print("Status Code:", response.status_code)

print(response.json()[0]["output"])