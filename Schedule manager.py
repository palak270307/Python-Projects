from datetime import datetime, timedelta  # timedelta represents the difference (duration) between two dates or times.

tasks = []
print("Welcome to the Schedule Manager!🗓️")

n = int(input("How many tasks would you like to schedule?: "))
for i in range(n):
    task_name = input(f"Enter the name of task {i+1}:") # Asks user to input task name.
    task_datetime = input(f"Enter the date and time for '{task_name}' (YYYY/MM/DD HH:MM): ") # Asks user to input task time.
    tasks.append((task_name, task_datetime)) # Appends task name and time as a tuple to the tasks list.

    try:
        deadline = datetime.strptime(task_datetime, "%Y/%m/%d %H:%M")  # Converts string to datetime object. 
    except ValueError:
        print("⚠️ Invalid date format. Please use YYYY/MM/DD HH:MM.")
        continue

    tasks.sort(key=lambda x: datetime.strptime(x[1], "%Y/%m/%d %H:%M")) # Sorts tasks by datetime.
    print("\n📅 Your Scheduled Tasks:")

    for t in tasks:
        time_left = deadline - datetime.now()
        days = time_left.days
        hours = time_left.seconds // 3600
        if time_left > timedelta(0):
            print(f"🟢 {t[0]} - Time left: {days} days, {hours} hours")
        else:
            print(f"🔴 {t[0]} - Deadline passed")
        print(f"   Scheduled for: {t[1]}")
    print()
print("All tasks scheduled successfully! ✅")
print("Remember to check your schedule regularly! 📆")
