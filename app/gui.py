import tkinter as tk
from tkinter import ttk


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

		ttk.Button(entry_row, text="Add Website").pack(side="left", padx=(8, 0))

		list_frame = ttk.Frame(container)
		list_frame.pack(fill="both", expand=True)

		task_list = tk.Listbox(list_frame, height=12, activestyle="dotbox")
		task_list.pack(side="left", fill="both", expand=True)

		scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=task_list.yview)
		scrollbar.pack(side="right", fill="y")
		task_list.configure(yscrollcommand=scrollbar.set)

		button_row = ttk.Frame(container)
		button_row.pack(fill="x", pady=(12, 0))

		ttk.Button(button_row, text="Edit").pack(side="left")
		ttk.Button(button_row, text="Delete").pack(side="left", padx=8)
		ttk.Button(button_row, text="On").pack(side="right")


def launch_app():
	app = SimpleApp()
	app.mainloop()
	
if __name__ == "__main__":
    launch_app()