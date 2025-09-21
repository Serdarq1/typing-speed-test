import tkinter as tk
from timeit import default_timer as timer
import random

class SpeedTyping:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title('Speed Typing Test')
        self.tk.geometry("600x350")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Speed typing improves accuracy and efficiency.",
            "Python is a powerful programming language."
        ]
        self.start_time = None
        self.setup_ui()
        self.reset_test()
        self.tk.mainloop()
    
    def setup_ui(self):
        """Sets up the UI"""
        self.sentence = random.choice(self.sentences).lower()
        self.label_sentence = tk.Label(self.tk, text=self.sentence, font=("Arial", 14), wraplength=500)
        self.label_sentence.pack()
        self.label_prompt = tk.Label(self.tk, text="Type the above sentence:", font=("Arial", 12))
        self.label_prompt.pack()

        self.entry = tk.Entry(self.tk, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.check_result())

        self.button_done = tk.Button(self.tk, text='Try Again', command=self.reset_test, width=12)
        self.button_done.pack()

        self.calculate_button = tk.Button(self.tk, text='Check', command=self.check_result, width=12)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.tk, text='', font=('Arial', 12))
        self.result_label.pack(pady=20)

        self.start_time = timer()
    
    def check_result(self):
        """Checks if the sentence and the input matches"""
        typed_text = self.entry.get()
        if typed_text == self.sentence:
            end_time = timer()
            time_taken = round(end_time - self.start_time, 2)
            words = len(self.sentence.split())
            wpm = round((words / time_taken) * 60, 2)
            msg = (
                f"Time: {time_taken:.2f}s   |   WPM: {wpm:.2f}%"
            )
            self.result_label.config(text=msg)
        else:
            self.result_label.config(text='Incorrect Typing.')
        
    def reset_test(self):
        """Resets the test"""
        self.sentence = random.choice(self.sentences)
        self.label_sentence.config(text=self.sentence)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = timer()

SpeedTyping()