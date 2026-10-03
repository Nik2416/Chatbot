
from tkinter import *


import tkinter as tk
import threading
from datetime import datetime

from chat import get_response


# ==============================================
# COLORS AND CONFIGURATION
# ==============================================

BG = "#F7F5FC"
SIDEBAR = "#211B3A"
PURPLE = "#7957D5"
PURPLE_HOVER = "#6342BC"
WHITE = "#FFFFFF"
TEXT = "#302A43"
MUTED = "#928BA5"
BORDER = "#E9E4F2"
BOT_AVATAR = "#EAE2FF"
USER_BUBBLE = "#7957D5"

# ==============================================
# MAIN APPLICATION
# ==============================================

class BotGUI:

    def __init__(self, root):

        self.root = root

        self.root.title("Bot | AI Assistant")
        self.root.geometry("1100x720")
        self.root.minsize(760, 520)
        self.root.configure(bg=BG)

        self.busy = False

        self.create_interface()
        self.show_welcome()

    # ==========================================
    # CREATE INTERFACE
    # ==========================================

    def create_interface(self):

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # --------------------------------------
        # SIDEBAR
        # --------------------------------------

        sidebar = tk.Frame(
            self.root,
            bg=SIDEBAR,
            width=235
        )

        sidebar.grid(row=0, column=0, sticky="ns")
        sidebar.grid_propagate(False)

        # Logo and branding

        logo_area = tk.Frame(
            sidebar,
            bg=SIDEBAR
        )

        logo_area.pack(
            fill="x",
            padx=22,
            pady=(30, 38)
        )

        tk.Label(
            logo_area,
            text="✦",
            font=("Segoe UI", 25, "bold"),
            bg=PURPLE,
            fg=WHITE,
            width=2,
            height=1
        ).pack(side="left", padx=(0, 12))

        brand = tk.Frame(
            logo_area,
            bg=SIDEBAR
        )

        brand.pack(side="left")

        tk.Label(
            brand,
            text="BOT",
            font=("Segoe UI", 19, "bold"),
            bg=SIDEBAR,
            fg=WHITE
        ).pack(anchor="w")

        tk.Label(
            brand,
            text="AI ASSISTANT",
            font=("Segoe UI", 8, "bold"),
            bg=SIDEBAR,
            fg="#C3B5F2"
        ).pack(anchor="w")

        # New conversation button

        self.make_sidebar_button(
            sidebar,
            "＋   New conversation",
            self.clear_chat,
            active=True
        )

        # Sidebar section heading

        tk.Label(
            sidebar,
            text="YOUR ASSISTANT",
            font=("Segoe UI", 9, "bold"),
            bg=SIDEBAR,
            fg="#AFA5CB"
        ).pack(
            anchor="w",
            padx=24,
            pady=(35, 12)
        )

        # Sidebar actions

        actions = [
            ("✦   Ask a question", "question"),
            ("◉   General conversation", "conversation"),
            ("❔   Help", "help")
        ]

        for label, action in actions:

            tk.Button(
                sidebar,
                text=label,
                font=("Segoe UI", 10),
                bg=SIDEBAR,
                fg="#E9E4F5",
                activebackground="#382E54",
                activeforeground=WHITE,
                relief="flat",
                bd=0,
                anchor="w",
                padx=22,
                pady=13,
                cursor="hand2",
                command=lambda a=action: self.sidebar_action(a)
            ).pack(
                fill="x",
                padx=10,
                pady=2
            )

        # Bottom card

        bottom_card = tk.Frame(
            sidebar,
            bg="#302747",
            padx=15,
            pady=16
        )

        bottom_card.pack(
            side="bottom",
            fill="x",
            padx=16,
            pady=22
        )

        tk.Label(
            bottom_card,
            text="✦  YOUR AI COMPANION",
            font=("Segoe UI", 9, "bold"),
            bg="#302747",
            fg="#D8CCFF"
        ).pack(anchor="w")

        tk.Label(
            bottom_card,
            text="A little conversation\ncan go a long way.",
            font=("Segoe UI", 9),
            bg="#302747",
            fg="#D8D1E7",
            justify="left"
        ).pack(
            anchor="w",
            pady=(8, 0)
        )

        # --------------------------------------
        # MAIN CONTENT
        # --------------------------------------

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        main.grid_rowconfigure(1, weight=1)
        main.grid_columnconfigure(0, weight=1)

        # --------------------------------------
        # HEADER
        # --------------------------------------

        header = tk.Frame(
            main,
            bg=WHITE,
            height=85,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        header.grid_propagate(False)

        header_left = tk.Frame(
            header,
            bg=WHITE
        )

        header_left.pack(
            side="left",
            padx=25,
            pady=15
        )

        tk.Label(
            header_left,
            text="Bot",
            font=("Segoe UI", 17, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(anchor="w")

        status = tk.Frame(
            header_left,
            bg=WHITE
        )

        status.pack(
            anchor="w",
            pady=(3, 0)
        )

        tk.Label(
            status,
            text="●",
            font=("Segoe UI", 9),
            bg=WHITE,
            fg="#26B879"
        ).pack(side="left")

        tk.Label(
            status,
            text="  AI assistant",
            font=("Segoe UI", 9),
            bg=WHITE,
            fg=MUTED
        ).pack(side="left")

        tk.Button(
            header,
            text="Clear chat  ↺",
            font=("Segoe UI", 9, "bold"),
            bg="#F1EDFC",
            fg=PURPLE,
            activebackground="#E4DCF9",
            relief="flat",
            bd=0,
            padx=14,
            pady=9,
            cursor="hand2",
            command=self.clear_chat
        ).pack(
            side="right",
            padx=22
        )

        # --------------------------------------
        # CHAT AREA
        # --------------------------------------

        chat_area = tk.Frame(
            main,
            bg=BG
        )

        chat_area.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(15, 5)
        )

        chat_area.grid_rowconfigure(0, weight=1)
        chat_area.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            chat_area,
            bg=BG,
            highlightthickness=0
        )

        scrollbar = tk.Scrollbar(
            chat_area,
            orient="vertical",
            command=self.canvas.yview
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        self.canvas.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.messages = tk.Frame(
            self.canvas,
            bg=BG
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.messages,
            anchor="nw"
        )

        self.messages.bind(
            "<Configure>",
            self.update_scroll
        )

        self.canvas.bind(
            "<Configure>",
            self.resize_messages
        )

        # --------------------------------------
        # INPUT AREA
        # --------------------------------------

        input_area = tk.Frame(
            main,
            bg=BG
        )

        input_area.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(8, 10)
        )

        input_area.grid_columnconfigure(0, weight=1)

        input_box = tk.Frame(
            input_area,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        input_box.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        input_box.grid_columnconfigure(0, weight=1)

        self.entry = tk.Entry(
            input_box,
            font=("Segoe UI", 11),
            bg=WHITE,
            fg=TEXT,
            insertbackground=PURPLE,
            relief="flat",
            bd=0
        )

        self.entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(18, 8),
            pady=17
        )

        self.placeholder = "Message Bot..."

        self.entry.insert(0, self.placeholder)
        self.entry.config(fg=MUTED)

        self.entry.bind(
            "<FocusIn>",
            self.clear_placeholder
        )

        self.entry.bind(
            "<FocusOut>",
            self.restore_placeholder
        )

        self.entry.bind(
            "<Return>",
            self.send_message
        )

        self.send_button = tk.Button(
            input_box,
            text="Send  ➤",
            font=("Segoe UI", 10, "bold"),
            bg=PURPLE,
            fg=WHITE,
            activebackground=PURPLE_HOVER,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            padx=20,
            pady=11,
            cursor="hand2",
            command=self.send_message
        )

        self.send_button.grid(
            row=0,
            column=1,
            padx=(5, 10),
            pady=8
        )

        tk.Label(
            input_area,
            text="Bot is an AI assistant. Responses may not always be accurate.",
            font=("Segoe UI", 8),
            bg=BG,
            fg=MUTED
        ).grid(
            row=1,
            column=0,
            pady=(8, 0)
        )

    # ==========================================
    # SIDEBAR BUTTON
    # ==========================================

    def make_sidebar_button(
        self,
        parent,
        text,
        command,
        active=False
    ):

        button = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold"),
            bg=PURPLE if active else SIDEBAR,
            fg=WHITE,
            activebackground=PURPLE_HOVER,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            anchor="w",
            padx=15,
            pady=13,
            cursor="hand2",
            command=command
        )

        button.pack(
            fill="x",
            padx=15
        )

    # ==========================================
    # WELCOME SCREEN
    # ==========================================

    def show_welcome(self):

        self.add_message(
            "bot",
            "Hey there! 👋 I'm Bot, your AI assistant."
        )

        self.add_message(
            "bot",
            "I'm here to chat with you and answer your "
            "questions. What would you like to talk "
            "about today?"
        )

        self.add_suggestions()

    # ==========================================
    # SUGGESTION BUTTONS
    # ==========================================

    def add_suggestions(self):

        wrapper = tk.Frame(
            self.messages,
            bg=BG
        )

        wrapper.pack(
            fill="x",
            padx=8,
            pady=(8, 16)
        )

        tk.Label(
            wrapper,
            text="GET STARTED",
            font=("Segoe UI", 8, "bold"),
            bg=BG,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(0, 9)
        )

        suggestions = [
            "Hello!",
            "What is your name?",
            "What can you do?"
        ]

        for question in suggestions:

            tk.Button(
                wrapper,
                text="✦  " + question,
                font=("Segoe UI", 9),
                bg=WHITE,
                fg=PURPLE,
                activebackground="#EEE8FC",
                relief="flat",
                bd=0,
                highlightbackground=BORDER,
                highlightthickness=1,
                padx=13,
                pady=10,
                cursor="hand2",
                command=lambda q=question: self.ask_question(q)
            ).pack(
                anchor="w",
                pady=4
            )

    # ==========================================
    # DISPLAY CHAT MESSAGE
    # ==========================================

    def add_message(self, sender, message):

        row = tk.Frame(
            self.messages,
            bg=BG
        )

        row.pack(
            fill="x",
            padx=5,
            pady=8
        )

        is_user = sender == "user"

        row.grid_columnconfigure(1, weight=1)

        # Avatar

        avatar = tk.Label(
            row,
            text="YOU" if is_user else "✦",
            font=("Segoe UI", 8, "bold"),
            bg=PURPLE if is_user else BOT_AVATAR,
            fg=WHITE if is_user else PURPLE,
            width=4 if is_user else 3,
            height=2
        )

        # Bubble

        bubble_color = USER_BUBBLE if is_user else WHITE

        bubble = tk.Frame(
            row,
            bg=bubble_color,
            highlightbackground=(
                bubble_color if is_user else BORDER
            ),
            highlightthickness=1,
            padx=14,
            pady=10
        )

        tk.Label(
            bubble,
            text=message,
            font=("Segoe UI", 10),
            bg=bubble_color,
            fg=WHITE if is_user else TEXT,
            justify="left",
            wraplength=430
        ).pack(anchor="w")

        timestamp = datetime.now().strftime("%I:%M %p")

        tk.Label(
            bubble,
            text=timestamp,
            font=("Segoe UI", 8),
            bg=bubble_color,
            fg="#E7DFFF" if is_user else MUTED
        ).pack(
            anchor="e",
            pady=(6, 0)
        )

        if is_user:

            bubble.grid(
                row=0,
                column=1,
                sticky="e"
            )

            avatar.grid(
                row=0,
                column=2,
                padx=(10, 0),
                sticky="n"
            )

        else:

            avatar.grid(
                row=0,
                column=0,
                padx=(0, 10),
                sticky="n"
            )

            bubble.grid(
                row=0,
                column=1,
                sticky="w"
            )

        self.root.after(50, self.scroll_to_bottom)

    # ==========================================
    # SCROLLING
    # ==========================================

    def update_scroll(self, event=None):

        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

    def resize_messages(self, event):

        self.canvas.itemconfigure(
            self.canvas_window,
            width=event.width
        )

    def scroll_to_bottom(self):

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    # ==========================================
    # INPUT PLACEHOLDER
    # ==========================================

    def clear_placeholder(self, event=None):

        if self.entry.get() == self.placeholder:

            self.entry.delete(0, tk.END)
            self.entry.config(fg=TEXT)

    def restore_placeholder(self, event=None):

        if not self.entry.get().strip():

            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg=MUTED)

    # ==========================================
    # SEND MESSAGE
    # ==========================================

    def send_message(self, event=None):

        if self.busy:
            return "break"

        message = self.entry.get().strip()

        if not message or message == self.placeholder:
            return "break"

        # Display user's message

        self.add_message("user", message)

        self.entry.delete(0, tk.END)
        self.entry.config(fg=TEXT)

        # Disable sending while Bot is responding

        self.busy = True

        self.send_button.config(
            text="Thinking...",
            state="disabled"
        )

        # Run prediction in the background

        threading.Thread(
            target=self.process_message,
            args=(message,),
            daemon=True
        ).start()

        return "break"

    # ==========================================
    # PROCESS BOT RESPONSE
    # ==========================================

    def process_message(self, message):

        try:
            response = get_response(message)

            if not response:
                response = "I'm not sure how to answer that yet."

        except Exception as error:

            print("Chatbot error:", error)

            response = (
                "Sorry, something went wrong. "
                "Please try again."
            )

        # Update the GUI on the main thread

        self.root.after(
            0,
            lambda: self.finish_response(str(response))
        )

    def finish_response(self, response):

        self.add_message("bot", response)

        self.busy = False

        self.send_button.config(
            text="Send  ➤",
            state="normal"
        )

        self.entry.focus_set()

    # ==========================================
    # QUICK ACTIONS
    # ==========================================

    def sidebar_action(self, action):

        questions = {
            "question": "Can you help me with a question?",
            "conversation": "Hello! Let's have a conversation.",
            "help": "What can you help me with?"
        }

        self.ask_question(questions[action])

    def ask_question(self, question):

        if self.busy:
            return

        self.entry.delete(0, tk.END)
        self.entry.insert(0, question)
        self.entry.config(fg=TEXT)

        self.send_message()

    # ==========================================
    # CLEAR CHAT
    # ==========================================

    def clear_chat(self):

        for widget in self.messages.winfo_children():
            widget.destroy()

        self.show_welcome()

        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.placeholder)
        self.entry.config(fg=MUTED)


# ==============================================
# START APPLICATION
# ==============================================

if __name__ == "__main__":

    root = tk.Tk()

    app = BotGUI(root)

    root.mainloop()

