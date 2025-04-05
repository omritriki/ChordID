import tkinter as tk
from tkinter import messagebox
from main import findNotes, findFirstNonMuted, findChordType


def identify_chord():
    frets = [entry.get() for entry in fret_entries]

    # Validate input
    if not all(f.isdigit() or f.upper() == 'X' for f in frets):
        messagebox.showerror("Input Error", "Frets must be numbers or 'X'")
        return

    # Convert to proper format
    frets = [int(f) if f.isdigit() else 'X' for f in frets]

    # Find notes (with duplicates, maintaining string order)
    notes_with_duplicates = findNotes(frets, tuning_var.get())

    # Find root note and chord type
    unique_notes = list(dict.fromkeys([note for note in notes_with_duplicates if note != 'X']))
    root_note = findFirstNonMuted(notes_with_duplicates)
    chord_type = findChordType(unique_notes)

    # Display result
    chord_label.config(text=f"Chord: {root_note} {chord_type}")
    notes_label.config(text=f"Notes: {', '.join(notes_with_duplicates)}")


def reset_fields():
    for entry in fret_entries:
        entry.delete(0, tk.END)
    chord_label.config(text="Chord:")
    notes_label.config(text="Notes:")


def quit_app():
    root.destroy()


# Create main window
root = tk.Tk()
root.title("Guitar Chord Identifier")
root.geometry("400x300")

# Tuning selection
tk.Label(root, text="Tuning:").pack()
tuning_options = ["EADGBE", "DADGAD", "Drop D", "Open G", "Open D"]
tuning_var = tk.StringVar(value=tuning_options[0])  # Default tuning
tuning_menu = tk.OptionMenu(root, tuning_var, *tuning_options)
tuning_menu.pack()

# Fret input
fret_entries = []
tk.Label(root, text="Enter frets (low E to high E, 'X' for mute):").pack()
fret_frame = tk.Frame(root)
fret_frame.pack()
for _ in range(6):
    entry = tk.Entry(fret_frame, width=3)
    entry.pack(side=tk.LEFT, padx=2)
    fret_entries.append(entry)

# Buttons
identify_btn = tk.Button(root, text="Identify Chord", command=identify_chord)
identify_btn.pack(pady=5)
reset_btn = tk.Button(root, text="Reset", command=reset_fields)
reset_btn.pack()
quit_btn = tk.Button(root, text="Quit", command=quit_app)
quit_btn.pack(pady=5)

# Output labels
chord_label = tk.Label(root, text="Chord:")
chord_label.pack()
notes_label = tk.Label(root, text="Notes:")
notes_label.pack()

# Run the application
root.mainloop()
