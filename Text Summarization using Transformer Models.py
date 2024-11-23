
from tkinter import Tk, Label, Text, Button, Scrollbar, END, VERTICAL
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text():
    input_text = text_input.get("1.0", END).strip()
    if input_text:
        try:
           
            summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)
            summary_output.delete("1.0", END)  
            summary_output.insert(END, summary[0]['summary_text'])  
        except Exception as e:
            summary_output.delete("1.0", END)
            summary_output.insert(END, f"Error: {str(e)}")
    else:
        summary_output.delete("1.0", END)
        summary_output.insert(END, "Please enter some text to summarize.")
app = Tk()
app.title("Text Summarizer")
app.geometry("800x600")
app.resizable(True, True)
Label(app, text="Enter Text to Summarize:", font=("Arial", 14)).pack(pady=10)
text_input = Text(app, wrap="word", height=10, font=("Arial", 12))
text_input.pack(padx=10, pady=5, fill="both", expand=True)
scrollbar_input = Scrollbar(app, orient=VERTICAL, command=text_input.yview)
text_input.configure(yscrollcommand=scrollbar_input.set)
scrollbar_input.pack(side="right", fill="y")
Button(app, text="Summarize", font=("Arial", 14), bg="#4CAF50", fg="white", command=summarize_text).pack(pady=10)
Label(app, text="Summary Output:", font=("Arial", 14)).pack(pady=10)
summary_output = Text(app, wrap="word", height=10, font=("Arial", 12), bg="#f9f9f9", state="normal")
summary_output.pack(padx=10, pady=5, fill="both", expand=True)
scrollbar_output = Scrollbar(app, orient=VERTICAL, command=summary_output.yview)
summary_output.configure(yscrollcommand=scrollbar_output.set)
scrollbar_output.pack(side="right", fill="y")
app.mainloop()
