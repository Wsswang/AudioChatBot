import os
import openai
import json
import pyttsx3
import AudioRecognition as AR
import AudioRecord as AC
import ApiKey as AK

existingFiles = os.listdir("CHAT")


maxFileNum = 100 #Maximum recorded chat number
maxchat = 100 



for chatFileIndex in range(maxFileNum):
    fileName = "CHAT"+ str(chatFileIndex).zfill(4)+".txt"
    if not fileName in existingFiles:
        print("Current chat "+fileName)
        break
        

openai.api_key = AK.API
maxchat = 100


engine = pyttsx3.init()

M = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hi"}
    ]

for i in range(maxchat):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages= M)

    chatContent = response['choices'][0]['message']['content']
    chatMessage = response['choices'][0]['message']

    M.append(dict(chatMessage))
    
    print("ChatGPT:", chatContent)

    engine.say(chatContent)
    engine.runAndWait()
    
    filepath = "AUDIOCHAT/AudioChat.wav"

    AC.record_audio(filepath)

    
    userText = AR.audioRecog(filepath)
    print("You: " + userText)
    userMessage = {"role": "user", "content": userText}
    M.append(dict(userMessage))
    txtfile = open("CHAT/"+fileName,"a+",encoding='utf-8')
    txtfile.write("ChatGPT:"+ chatContent+"\n")
    txtfile.write("You:"+ userText+"\n")
    txtfile.close()
print("Chat finished")

