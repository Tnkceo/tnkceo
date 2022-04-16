import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-3390465781637-3386827202886-xZBG6m7MhuSbpPpfIGCta7XJ"
 
post_message(myToken,"#stock","TnkCeo hellow!!")
