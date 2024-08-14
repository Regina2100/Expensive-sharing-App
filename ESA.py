import tkinter as tk
from tkinter import messagebox

class ExpenseSharingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Sharing App")

        self.friends = []

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Add Friend Section
        self.friend_label = tk.Label(self.root, text="Enter Friend Name:")
        self.friend_label.pack(pady=5)

        self.friend_entry = tk.Entry(self.root)
        self.friend_entry.pack(pady=5)

        self.add_friend_button = tk.Button(self.root, text="Add Friend", command=self.add_friend)
        self.add_friend_button.pack(pady=5)

        self.friends_listbox = tk.Listbox(self.root)
        self.friends_listbox.pack(pady=5)

        # Add Expense Section
        self.amount_label = tk.Label(self.root, text="Enter Total Amount:")
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        self.split_button = tk.Button(self.root, text="Split Bills", command=self.split_bills)
        self.split_button.pack(pady=5)

        # Track Payments Section
        self.paid_label = tk.Label(self.root, text="Enter Name of Paid Friend:")
        self.paid_label.pack(pady=5)

        self.paid_entry = tk.Entry(self.root)
        self.paid_entry.pack(pady=5)

        self.track_button = tk.Button(self.root, text="Track Payments", command=self.track_payments)
        self.track_button.pack(pady=5)

        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.pack(pady=5)

    def add_friend(self):
        friend_name = self.friend_entry.get().strip().capitalize()
        if friend_name:
            if friend_name not in self.friends:
                self.friends.append(friend_name)
                self.friends_listbox.insert(tk.END, friend_name)
                self.friend_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Duplicate Entry", f"{friend_name} is already in the list.")
        else:
            messagebox.showwarning("Input Error", "Friend name cannot be empty.")

    def split_bills(self):
        total_amount_str = self.amount_entry.get().strip()
        if not total_amount_str:
            messagebox.showwarning("Input Error", "Total amount cannot be empty.")
            return

        try:
            total_amount = float(total_amount_str)
            if total_amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid positive number for the amount.")
            return

        if len(self.friends) == 0:
            messagebox.showwarning("No Friends", "Please add at least one friend.")
            return

        amount_per_person = total_amount / len(self.friends)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "Splitted Amount:\n")
        for friend in self.friends:
            self.results_text.insert(tk.END, f"{friend}: ₹{amount_per_person:.2f}\n")

    def track_payments(self):
        paid_name = self.paid_entry.get().strip().capitalize()
        if not paid_name:
            messagebox.showwarning("Input Error", "Paid friend name cannot be empty.")
            return

        if paid_name not in self.friends:
            messagebox.showwarning("Invalid Name", f"{paid_name} is not in the list of friends.")
            return

        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"{paid_name} has paid.\n")
        unpaid_friends = [friend for friend in self.friends if friend != paid_name]
        self.results_text.insert(tk.END, "Remaining Unpaid Friends:\n")
        for friend in unpaid_friends:
            self.results_text.insert(tk.END, f"{friend}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseSharingApp(root)
    root.mainloop()
