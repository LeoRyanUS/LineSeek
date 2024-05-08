import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pyperclip

class LineTrackPro:
    def __init__(self, master):
        self.master = master
        master.title("LineSeek")

        # Style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TLabel', font=('Arial', 10))

        self.app_name_label = ttk.Label(master, text="LineSeek", font=("Arial", 12))
        self.app_name_label2 = ttk.Label(master, text="By: LeoRyanUS", font=("Arial", 8))

        self.app_name_label.grid(row=0, column=0, columnspan=2, pady=(0, 5))
        self.app_name_label2.grid(row=0, column=1, columnspan=2, pady=(0, 5))

        self.label = tk.Label(master, text="Select a text file:", font=("Arial", 10, "bold"))
        self.label.grid(row=1, column=0, pady=(0, 3), sticky="e")

        self.browse_button = ttk.Button(master, text="Browse", command=self.browse_file, width=8)
        self.browse_button.grid(row=1, column=1, pady=(0, 3), sticky="w")

        self.display_text = tk.Text(master, height=1, width=20)
        self.display_text.grid(row=2, column=0, columnspan=2, padx=5, pady=(0, 3))

        self.copy_line_button = ttk.Button(master, text="Copy Line", command=self.copy_line)
        self.copy_line_button.grid(row=3, column=0, columnspan=2, pady=(0, 3))

        self.lines_counter_label = ttk.Label(master, text="Total Lines: 0", anchor="w")
        self.lines_counter_label.grid(row=4, column=0, columnspan=2, pady=(0, 10), sticky="ew")

        self.total_clicks_counter_label = ttk.Label(master, text="Total Clicks: 0", anchor="w")
        self.total_clicks_counter_label.grid(row=5, column=0, columnspan=2, sticky="ew")

        self.current_line_index = 0
        self.file_lines = []
        self.total_clicks_counter = 0

        # Center all elements within the graphical interface
        for child in master.winfo_children():
            child.grid_configure(padx=10, pady=5)
        master.update_idletasks()

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, 'r') as file:
                self.file_lines = file.readlines()
            self.lines_counter_label.config(text=f"Total Lines: {len(self.file_lines)}")

    def copy_line(self):
        if self.file_lines:
            if self.current_line_index >= len(self.file_lines):
                self.current_line_index = 0  # Restart from the beginning
            line = self.file_lines[self.current_line_index]
            pyperclip.copy(line.strip())  # Copy current line to clipboard
            self.display_text.delete('1.0', tk.END)  # Clear previous content
            self.display_text.insert(tk.END, line)
            self.current_line_index += 1
            self.total_clicks_counter += 1
            self.total_clicks_counter_label.config(text=f"Total Clicks: {self.total_clicks_counter}")

root = tk.Tk()
app = LineTrackPro(root)
root.mainloop()
