import tkinter as tk
from tkinter import ttk
import json
import os

# Define Paths
DICT_FILE = 'dictionary/kaikki.org-dictionary-English-words.jsonl'
INDEX_FILE = 'index.json'

# --- SAFE DATA LOADING ---
try:
    with open(INDEX_FILE, 'r') as f:
        INDEX_DATA = json.load(f)
except Exception as e:
    with open("debug.log", "w") as f: f.write(f"CRITICAL STARTUP ERROR: {str(e)}")
    INDEX_DATA = {}

def pynch_search(event=None):
    query = entry_box.get().lower().strip()
    if not query: return
    
    if query not in INDEX_DATA:
        update_result(f"'{query}' not found.")
        return

    try:
        # Use a context manager to ensure the file closes immediately
        with open(DICT_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            f.seek(INDEX_DATA[query])
            line = f.readline()
            if not line: return
            
            entry = json.loads(line)
            # Safe extraction
            pos = entry.get('pos', 'N/A')
            senses = entry.get('senses', [])
            defs = []
            for s in senses:
                for gloss in s.get('glosses', []):
                    defs.append(f"• {gloss}")
            
            output = f"WORD: {query.upper()}\nPOS: {pos}\n\nDEFINITIONS:\n" + "\n\n".join(defs)
            update_result(output)
            
    except Exception as e:
        update_result(f"Error reading file: {str(e)}")

def update_result(text):
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, text)
    result_text.config(state=tk.DISABLED)

# --- UI Setup ---
root = tk.Tk()
root.title("Pynch - Ghost Dictionary")
root.geometry("500x500")
root.configure(bg="#2c3e50")

tk.Label(root, text="Pynch Dictionary", bg="#2c3e50", fg="white", font=("Segoe UI", 16, "bold")).pack(pady=10)
entry_box = tk.Entry(root, width=40, font=("Segoe UI", 12))
entry_box.pack(pady=5)
entry_box.bind('<Return>', pynch_search)
ttk.Button(root, text="Search", command=pynch_search).pack(pady=10)

result_text = tk.Text(root, height=15, width=55, font=("Segoe UI", 11), bg="#34495e", fg="white", padx=10, pady=10, relief=tk.FLAT)
result_text.pack(pady=10)
result_text.config(state=tk.DISABLED)

# Keeps the window open even if errors occur during startup
root.mainloop()