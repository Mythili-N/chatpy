
import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
import re
import time
import threading

class SimpleChatbot:
    def __init__(self, name):
        self.name = name
        self.memory = {}
        
        # Define response patterns
        self.patterns = [
            (r'hi|hello|hey', self.greet),
            (r'what is your name', lambda _: f"My name is {self.name}!"),
            (r'how are you', lambda _: "I'm doing well, thank you! How about you?"),
            (r'my name is (.*)', self.remember_name),
            (r'what is my name', self.recall_name),
            (r'what time is it', lambda _: f"The current time is {time.strftime('%H:%M')}"),
            (r'what day is it', lambda _: f"Today is {time.strftime('%A, %B %d, %Y')}"),
            (r'bye|goodbye', lambda _: "Goodbye! It was nice chatting with you!"),
        ]
        
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more.",
            "I don't have a response for that yet.",
        ]
    
    def greet(self, _):
        return random.choice([
            f"Hello! I'm {self.name}. How can I help you today?",
            f"Hi there! I'm {self.name}. Nice to meet you!",
            f"Hey! I'm {self.name}. What's on your mind?"
        ])
    
    def remember_name(self, message):
        name_match = re.search(r'my name is (.*)', message, re.IGNORECASE)
        if name_match:
            name = name_match.group(1).strip()
            self.memory['user_name'] = name
            return f"Nice to meet you, {name}! I'll remember your name."
        return "I didn't catch your name. Could you tell me again?"
    
    def recall_name(self, _):
        return f"Your name is {self.memory['user_name']}!" if 'user_name' in self.memory else "I don't think you've told me your name yet."
    
    def respond(self, message):
        message = message.lower().strip()
        for pattern, response_func in self.patterns:
            if re.search(pattern, message, re.IGNORECASE):
                return response_func(message)
        return random.choice(self.default_responses)

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.chatbot = SimpleChatbot("ChatPy")
        
        self.root.title("ChatPy - Simple AI Chatbot")
        self.root.geometry("600x500")
        self.root.minsize(400, 400)
        
        self.chat_frame = tk.Frame(root)
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.chat_history = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_history.pack(fill=tk.BOTH, expand=True)
        
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        self.input_field = tk.Entry(self.input_frame)
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)
        
        self.display_bot_message(self.chatbot.greet(""))
        self.input_field.focus_set()
    
    def send_message(self, event=None):
        message = self.input_field.get().strip()
        if message:
            self.display_user_message(message)
            self.input_field.delete(0, tk.END)
            threading.Thread(target=self.process_message, args=(message,)).start()
    
    def process_message(self, message):
        time.sleep(0.5)
        response = self.chatbot.respond(message)
        self.display_bot_message(response)
        if re.search(r'bye|goodbye', message, re.IGNORECASE):
            time.sleep(1)
            self.root.after(0, self.show_goodbye_message)
    
    def show_goodbye_message(self):
        messagebox.showinfo("Goodbye", "Thank you for chatting with ChatPy!")
    
    def display_user_message(self, message):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, "You: ", "user")
        self.chat_history.insert(tk.END, f"{message}\n\n")
        self.chat_history.see(tk.END)
        self.chat_history.config(state=tk.DISABLED)
    
    def display_bot_message(self, message):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, f"{self.chatbot.name}: ", "bot")
        self.chat_history.insert(tk.END, f"{message}\n\n")
        self.chat_history.see(tk.END)
        self.chat_history.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
