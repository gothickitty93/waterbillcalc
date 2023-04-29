import tkinter as tk

def update_output(*args):
    try:
        prev_reading = float(prev_reading_entry.get())
        new_reading = float(new_reading_entry.get())
        wrate = float(wrate_entry.get())
        srate = float(srate_entry.get())
        sratebase = float(sratebase_entry.get())

        usage = new_reading - prev_reading
        sratecalc = usage * srate
        bill_amount = usage * wrate + sratecalc + sratebase

        output_text.set(f"Your water bill amount is: ${bill_amount:.2f}\nWater used: {usage:.2f}")

    except ValueError:
        output_text.set("Please enter valid numbers for all fields.")

root = tk.Tk()
root.title("Water Bill Calculator")

# Input fields
prev_reading_entry = tk.Entry(root)
prev_reading_entry.grid(row=0, column=1)
tk.Label(root, text="Previous Reading:").grid(row=0, column=0, sticky="e")

new_reading_entry = tk.Entry(root)
new_reading_entry.grid(row=1, column=1)
tk.Label(root, text="Current Reading:").grid(row=1, column=0, sticky="e")

wrate_entry = tk.Entry(root)
wrate_entry.grid(row=2, column=1)
tk.Label(root, text="Water Cost per 1,000's:").grid(row=2, column=0, sticky="e")

srate_entry = tk.Entry(root)
srate_entry.grid(row=3, column=1)
tk.Label(root, text="Sewer Cost per 1,000's:").grid(row=3, column=0, sticky="e")

sratebase_entry = tk.Entry(root)
sratebase_entry.grid(row=4, column=1)
tk.Label(root, text="Sewer Cost Base:").grid(row=4, column=0, sticky="e")

# Output field
output_text = tk.StringVar()
output_text.set("Enter values to calculate your water bill.")
output_label = tk.Label(root, textvariable=output_text, anchor="w", justify="left")
output_label.grid(row=6, column=0, columnspan=2)

# Binding updates
prev_reading_entry.bind("<KeyRelease>", update_output)
new_reading_entry.bind("<KeyRelease>", update_output)
wrate_entry.bind("<KeyRelease>", update_output)
srate_entry.bind("<KeyRelease>", update_output)
sratebase_entry.bind("<KeyRelease>", update_output)

root.mainloop()
