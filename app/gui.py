import tkinter as tk
from tkinter import messagebox, ttk

try:
    from .storage import load_config, add_website, edit_website, delete_website, set_startup
except ImportError:
    from storage import load_config, add_website, edit_website, delete_website, set_startup

class SimpleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Startup-Tabs")
        self.geometry("520x420")
        self.minsize(480, 360)

        self._build_ui()

    def _build_ui(self):
        container = ttk.Frame(self, padding=16)
        container.pack(fill="both", expand=True)

        title = ttk.Label(container, text="Startup-Tabs", font=("Segoe UI", 16, "bold"))
        title.pack(pady=(0, 12), anchor="center")

        entry_row = ttk.Frame(container)
        entry_row.pack(fill="x", pady=(0, 12))

        entry = ttk.Entry(entry_row)
        entry.pack(side="left", fill="x", expand=True)

        ttk.Button(entry_row, text="Add Website", command=lambda: self.add_button(entry, task_list)).pack(side="left", padx=(8, 0))

        list_frame = ttk.Frame(container)
        list_frame.pack(fill="both", expand=True)

        task_list = tk.Listbox(list_frame, height=12, activestyle="dotbox")
        task_list.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=task_list.yview)
        scrollbar.pack(side="right", fill="y")
        task_list.configure(yscrollcommand=scrollbar.set)

        button_row = ttk.Frame(container)
        button_row.pack(fill="x", pady=(12, 0))

        #ttk.Button(button_row, text="Edit", command=self.edit_button()).pack(side="left")
        ttk.Button(button_row, text="Delete", command=self.delete_button()).pack(side="left", padx=8)
        ttk.Button(button_row, text="On", command=self.startup_button()).pack(side="right")
		
    def add_button(self, entry, tasks):
        text = entry.get().strip()
        if not text:
            messagebox.showerror("Input Error", "Please enter a website URL.")
            return
        if not text.startswith(("http://", "https://")):
            text = "https://" + text
			
        print(text)
        add_website(text)
        self.refresh(tasks)
        entry.delete(0, tk.END)

    def delete_button(self):
        pass
	
    def edit_button(self):
        pass
	
    def startup_button(self):
        pass
	
    def refresh(self, tasks):
        config = load_config()
        for web in config["websites"]:
             tasks.insert(tk.END, web)

def launch_app():
    app = SimpleApp()
    app.mainloop()
	
if __name__ == "__main__":
    launch_app()
