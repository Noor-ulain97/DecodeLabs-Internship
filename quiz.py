import tkinter as tk
from tkinter import ttk, messagebox


questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["5", "8", "10", "15"],
        "answer": "8"
    }
]


root = tk.Tk()
root.title("Advanced Quiz App")
root.geometry("600x450")


score = 0
q_index = 0
time_left = 10
user_name = ""

# ---------------- FRAMES ----------------
start_frame = tk.Frame(root)
quiz_frame = tk.Frame(root)
result_frame = tk.Frame(root)

for frame in (start_frame, quiz_frame, result_frame):
    frame.place(relwidth=1, relheight=1)

# ---------------- START SCREEN ----------------
tk.Label(start_frame, text="Welcome to Quiz App", font=("Arial", 20, "bold")).pack(pady=20)

name_entry = tk.Entry(start_frame, font=("Arial", 14))
name_entry.pack(pady=10)
name_entry.insert(0, "Enter your name")

def start_quiz():
    global user_name
    user_name = name_entry.get()
    start_frame.forget()
    quiz_frame.lift()
    load_question()

tk.Button(start_frame, text="Start Quiz", font=("Arial", 14), command=start_quiz).pack(pady=20)


question_label = tk.Label(quiz_frame, text="", font=("Arial", 14), wraplength=500)
question_label.pack(pady=20)

timer_label = tk.Label(quiz_frame, text="Time: 10", font=("Arial", 12))
timer_label.pack()

progress = ttk.Progressbar(quiz_frame, length=300, mode="determinate")
progress.pack(pady=10)

buttons = []


def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time: {time_left}")
        root.after(1000, countdown)
    else:
        next_question()


def load_question():
    global q_index, time_left

    if q_index < len(questions):
        q = questions[q_index]

        question_label.config(text=q["question"])

        for i in range(4):
            buttons[i].config(
                text=q["options"][i],
                state="normal"
            )

        progress["value"] = (q_index / len(questions)) * 100

        time_left = 10
        timer_label.config(text="Time: 10")
        countdown()

    else:
        show_result()


def check_answer(selected):
    global score
    correct = questions[q_index]["answer"]

    if selected == correct:
        score += 1

    next_question()


def next_question():
    global q_index
    q_index += 1
    load_question()

def show_result():
    quiz_frame.forget()
    result_frame.lift()

    percent = int((score / len(questions)) * 100)

    tk.Label(result_frame,
             text=f"{user_name}, your result:",
             font=("Arial", 18, "bold")).pack(pady=20)

    tk.Label(result_frame,
             text=f"Score: {score}/{len(questions)}",
             font=("Arial", 16)).pack(pady=10)

    tk.Label(result_frame,
             text=f"Percentage: {percent}%",
             font=("Arial", 16)).pack(pady=10)

    if percent >= 70:
        msg = "Excellent 🏆"
    elif percent >= 40:
        msg = "Good 👍"
    else:
        msg = "Try Again 📘"

    tk.Label(result_frame, text=msg, font=("Arial", 16)).pack(pady=10)

    tk.Button(result_frame, text="Restart", command=restart).pack(pady=10)

def restart():
    global score, q_index
    score = 0
    q_index = 0
    result_frame.forget()
    start_frame.lift()

for i in range(4):
    btn = tk.Button(
        quiz_frame,
        text="",
        width=30,
        font=("Arial", 12),
        command=lambda i=i: check_answer(buttons[i].cget("text"))
    )
    btn.pack(pady=5)
    buttons.append(btn)


start_frame.lift()
root.mainloop()