import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

def get_wifi_profiles():
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8')
        profiles = [line.split(":")[1].strip() for line in result.split('\n') if "All User Profile" in line]
        return profiles
    except subprocess.CalledProcessError:
        return []

def get_wifi_key(profile_name):
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8')
        key_content = [line.split(":")[1].strip() for line in result.split('\n') if "Key Content" in line]
        return key_content[0] if key_content else "Key not found."
    except subprocess.CalledProcessError:
        return "Error retrieving the key."

def show_wifi_key():
    selected_profile = wifi_profiles.get(wifi_profiles.curselection())
    if selected_profile:
        wifi_key = get_wifi_key(selected_profile)
        messagebox.showinfo("Wi-Fi Key", f"Password:\n{wifi_key}")
    else:
        messagebox.showwarning("Warning", "Please select a Wi-Fi network.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Shahaf Key Retriever")
    root.geometry("400x300")  # Fixed size of 400x300 pixels

    wifi_profiles = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12))
    wifi_profiles.pack(padx=10, pady=10)

    refresh_button = tk.Button(root, text="Show Network List", font=("Helvetica", 12), command=lambda: wifi_profiles.insert(tk.END, *get_wifi_profiles()))
    refresh_button.pack(pady=5)

    get_key_button = tk.Button(root, text="Get Wi-Fi Password", font=("Helvetica", 12), command=show_wifi_key)
    get_key_button.pack(pady=5)

    root.mainloop()
