import tkinter as tk
from tkinter import messagebox
import urllib.request
import threading
import os

# --- ARASAKA PROTOCOL COLORS ---
CP_YELLOW = "#FCEE09"  # Night City Yellow
CP_BLACK  = "#060606"  # True Black
CP_CYAN   = "#00F0FF"  # Matrix Cyan
CP_RED    = "#FF003C"  # Danger Red
CP_GRAY   = "#1A1A1B"  # Sub-layer Gray

def patch_link(url):
    """Automated Link Repair Protocol"""
    url = url.replace("gidhub.io", "github.io").strip()
    if "github.com" in url:
        url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    return url

def execute_stream():
    raw_url = url_entry.get()
    target_url = patch_link(raw_url)
    filename = name_entry.get().strip()
    
    try:
        status_var.set(">> [SCANNING TARGET] ...")
        root.update_idletasks()
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(target_url, headers=headers)
        
        with urllib.request.urlopen(req) as response:
            status_var.set(">> [INFILTRATING SERVER] ...")
            with open(filename, 'wb') as out_file:
                out_file.write(response.read())
            
        status_var.set(">> [EXTRACTION COMPLETE]")
        messagebox.showinfo("MOD SECURED", f"FILE: {filename}\nLOCATION: {os.getcwd()}")
    except Exception as e:
        status_var.set(">> [CRITICAL ERROR: 404/TIMED OUT]")
        messagebox.showerror("BREACH FAILED", f"Link Corrupted or Typo Detected:\n{e}")
    finally:
        exec_btn.config(state="normal", bg=CP_YELLOW, text="EXECUTE DOWNLOAD")

def trigger():
    exec_btn.config(state="disabled", bg=CP_GRAY, text="EXTRACTING...")
    threading.Thread(target=execute_stream, daemon=True).start()

# --- CYBER-HUD DESIGN ---
root = tk.Tk()
root.title("HONKAI MOD RAIL DOWNLOADER")
root.geometry("600x420") # Increased height for footer
root.configure(bg=CP_BLACK)

# Top Neon Border
tk.Frame(root, height=2, bg=CP_CYAN).pack(fill="x")

# Main Title
header = tk.Label(root, text="HONKAI MOD RAIL // DOWNLOADER", 
                  font=("Consolas", 18, "bold"), bg=CP_BLACK, fg=CP_YELLOW)
header.pack(pady=20)

# Input: Link
tk.Label(root, text="[ ENTER DATA SOURCE ]", font=("Consolas", 10), bg=CP_BLACK, fg=CP_CYAN).pack()
url_entry = tk.Entry(root, width=65, bg=CP_GRAY, fg=CP_CYAN, insertbackground=CP_CYAN, 
                     highlightthickness=1, highlightbackground=CP_CYAN, border=0, font=("Consolas", 10))
url_entry.pack(pady=10)
url_entry.insert(0, "https://github.com/SHYSOKUN/HonkaiModRail.github.io/blob/main/Unlock%20Star%20Rail%20.zip")

# Input: Filename
tk.Label(root, text="[ DEFINE TARGET NAME ]", font=("Consolas", 10), bg=CP_BLACK, fg=CP_CYAN).pack()
name_entry = tk.Entry(root, width=35, bg=CP_GRAY, fg=CP_CYAN, insertbackground=CP_CYAN, 
                      highlightthickness=1, highlightbackground=CP_CYAN, border=0, font=("Consolas", 10))
name_entry.pack(pady=10)
name_entry.insert(0, "Unlock_Star_Rail.zip")

# Status Line
status_var = tk.StringVar(value=">> SYSTEM: ONLINE")
status_label = tk.Label(root, textvariable=status_var, font=("Consolas", 9, "bold italic"), 
                        bg=CP_BLACK, fg=CP_RED)
status_label.pack(pady=15)

# The "Execute" Button
exec_btn = tk.Button(root, text="EXECUTE DOWNLOAD", bg=CP_YELLOW, fg=CP_BLACK, 
                     font=("Consolas", 14, "bold"), command=trigger, 
                     activebackground=CP_CYAN, activeforeground=CP_BLACK, 
                     borderwidth=0, cursor="hand2", padx=30, pady=10)
exec_btn.pack()

# --- FOOTER SECTION ---
footer_frame = tk.Frame(root, bg=CP_BLACK)
footer_frame.pack(side="bottom", fill="x", pady=10)

# The Copyright Line
copyright_label = tk.Label(footer_frame, text="@Copyright HONKAI MOD RAIL 2026", 
                           font=("Consolas", 8, "bold"), bg=CP_BLACK, fg="#444")
copyright_label.pack()

# Bottom Neon Border
tk.Frame(root, height=2, bg=CP_RED).pack(fill="x", side="bottom")

root.mainloop()
