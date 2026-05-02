# study_agent.py

subjects = []
progress = {}

def add_subjects():
    n = int(input("How many subjects? "))
    for i in range(n):
        sub = input(f"Enter subject {i+1}: ")
        subjects.append(sub)
        progress[sub] = 0

def make_plan():
    print("\n📅 Today's Study Plan:")
    for sub in subjects:
        print(f"- Study {sub} for 1 hour")

def update_progress():
    sub = input("Which subject did you study? ")
    if sub in progress:
        progress[sub] += 1
        print(f"✅ Progress updated for {sub}")
    else:
        print("❌ Subject not found")

def show_progress():
    print("\n📊 Progress:")
    for sub, val in progress.items():
        print(f"{sub}: {val} sessions completed")

def main():
    add_subjects()
    
    while True:
        print("\n1. Show Plan\n2. Update Progress\n3. Show Progress\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            make_plan()
        elif choice == "2":
            update_progress()
        elif choice == "3":
            show_progress()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

main()