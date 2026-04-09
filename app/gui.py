import tkinter as tk
from tkinter import messagebox, ttk

try:
    from .storage import load_config, add_website, delete_website, set_startup
    from .startup import enable_startup, disable_startup
except ImportError:
    from storage import load_config, add_website, delete_website, set_startup
    from startup import enable_startup, disable_startup

class SimpleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Startup-Tabs")
        self.geometry("520x420")
        self.minsize(480, 360)

        config = load_config()
        self.startup_enabled = config.get("startup_enabled", True)
        self.startup_toggle_btn = None

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

        ttk.Button(button_row, text="Delete", command=lambda: self.delete_button(task_list)).pack(side="left", padx=8)
        self.startup_toggle_btn = ttk.Button(
            button_row,
            text=self._startup_button_label(),
            command=self.startup_button,
        )
        self.startup_toggle_btn.pack(side="right")

        self.refresh(task_list)
		
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

    def delete_button(self, tasks):
        selection = tasks.curselection()
        if selection:
            item = tasks.get(selection)
            delete_website(item)
            self.refresh(tasks)

    def _startup_button_label(self):
        return "On" if self.startup_enabled else "Off"

    def startup_button(self):
        self.startup_enabled = not self.startup_enabled
        set_startup(self.startup_enabled)

        if self.startup_enabled:
            enable_startup()
        else:
            disable_startup()
            
        if self.startup_toggle_btn is not None:
            self.startup_toggle_btn.config(text=self._startup_button_label())

    def refresh(self, tasks):
        tasks.delete(0, tk.END)
        config = load_config()
        for web in config["websites"]:
             tasks.insert(tk.END, web)

def launch_app():
    app = SimpleApp()
    app.mainloop()