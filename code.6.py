#Agent Logic (Decision Making)
memory = load_memory()

def agent(user_input):
    if "plan" in user_input.lower():
        return chat_with_ai("Create a study plan for " + user_input)
    
    elif "progress" in user_input.lower():
        return str(memory)
    
    elif "studied" in user_input.lower():
        subject = user_input.split()[-1]
        memory[subject] = memory.get(subject, 0) + 1
        save_memory(memory)
        return f"Progress saved for {subject}"
    
    else:
        return chat_with_ai(user_input)
    