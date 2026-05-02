def quiz():
    print("\n🧠 Quick Quiz Time!")
    questions = {
        "What is 2 + 2?": "4",
        "Capital of India?": "Delhi"
    }

    for q, ans in questions.items():
        user = input(q + " ")
        if user.lower() == ans.lower():
            print("✅ Correct")
        else:
            print(f"❌ Wrong (Answer: {ans})")