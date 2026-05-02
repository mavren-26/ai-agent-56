#Run Chat Loop
while True:
    user = input("You: ")
    if user == "exit":
        break
    
    reply = agent(user)
    print("AI:", reply)
    