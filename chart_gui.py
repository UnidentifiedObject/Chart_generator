import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from chart import create_chart
from tkinter import ttk

current_fig = None
selected_color = None  # Store user-selected color

def choose_color():
    global selected_color
    color = colorchooser.askcolor(title="Choose Chart Color")[1]  # [1] returns hex
    if color:
        selected_color = color
        color_label.config(text=f"Selected: {color}")

def generate_chart():
    global current_fig, selected_color

    categories_input = entry_categories.get()
    values_input = entry_values.get()
    chart_type = chart_type_var.get().lower()

    title = entry_title.get()
    xlabel = entry_xlabel.get()
    ylabel = entry_ylabel.get()

    categories = [item.strip() for item in categories_input.split(',')]
    values = [item.strip() for item in values_input.split(',')]

    if len(categories) != len(values):
        messagebox.showerror("Input Error", "Number of categories and values must match.")
        return

    try:
        values_float = [float(v) for v in values]
    except ValueError:
        messagebox.showerror("Input Error", "Values must be numbers.")
        return

    try:
        fig = create_chart(
            categories,
            values_float,
            chart_type,
            title=title if title else None,
            xlabel=xlabel if xlabel else None,
            ylabel=ylabel if ylabel else None,
            color=selected_color
        )
    except ValueError as e:
        messagebox.showerror("Chart Error", str(e))
        return

    current_fig = fig

    for widget in chart_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    plt.close(fig)

def save_chart():
    global current_fig
    if current_fig is None:
        messagebox.showwarning("No Chart", "Please generate a chart first!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("All files", "*.*")],
        title="Save Chart As"
    )
    if file_path:
        try:
            current_fig.savefig(file_path)
            messagebox.showinfo("Saved", f"Chart saved to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save chart:\n{e}")

# --- GUI SETUP ---

root = tk.Tk()
root.title("Chart Generator")
root.geometry("800x700")
style = ttk.Style()
style.theme_use("vista")

ttk.Label(root, text="Categories (comma-separated):").pack()
entry_categories = ttk.Entry(root, width=50)
entry_categories.pack()

ttk.Label(root, text="Values (comma-separated):").pack()
entry_values = ttk.Entry(root, width=50)
entry_values.pack()

ttk.Label(root, text="Chart Type:").pack()
chart_type_var = tk.StringVar(root)
chart_type_var.set("bar")
ttk.OptionMenu(root, chart_type_var, "bar", "bar", "pie", "line").pack()

# Optional Fields
ttk.Label(root, text="Chart Title (optional):").pack()
entry_title = ttk.Entry(root, width=50)
entry_title.pack()

ttk.Label(root, text="X-Axis Label (optional):").pack()
entry_xlabel = ttk.Entry(root, width=50)
entry_xlabel.pack()

ttk.Label(root, text="Y-Axis Label (optional):").pack()
entry_ylabel = ttk.Entry(root, width=50)
entry_ylabel.pack()

ttk.Button(root, text="Choose Chart Color", command=choose_color).pack(pady=5)
color_label = ttk.Label(root, text="No color selected")
color_label.pack()

ttk.Button(root, text="Generate Chart", command=generate_chart).pack(pady=10)
ttk.Button(root, text="Save Chart", command=save_chart).pack(pady=5)

chart_frame = ttk.Frame(root)
chart_frame.pack()

def on_closing():
    root.destroy()
    import sys
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
