import tkinter as tk
from tkinter import ttk, messagebox
from collections import defaultdict
import matplotlib.pyplot as plt
import json
import os
from datetime import datetime, timedelta

class FuelTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("EcoDrive")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        self.entries = []
        self.station_data = defaultdict(list)
        
        self.enable_efficiency = tk.BooleanVar(value=True)
        self.enable_comparison = tk.BooleanVar(value=True)
        self.enable_graphs = tk.BooleanVar(value=True)

        self.load_data()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.create_add_entry_tab()
        self.create_analysis_tab()
        self.create_view_history_tab()

    def create_add_entry_tab(self):
        """Create the Add Entry tab."""
        self.add_entry_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.add_entry_tab, text="Add Entry")

        self.add_entry_tab.grid_rowconfigure(0, weight=1)
        self.add_entry_tab.grid_rowconfigure(2, weight=1)
        self.add_entry_tab.grid_columnconfigure(0, weight=1)
        self.add_entry_tab.grid_columnconfigure(2, weight=1)

        form_frame = ttk.Frame(self.add_entry_tab)
        form_frame.grid(row=1, column=1, padx=20, pady=20)

        # Customer Name
        ttk.Label(form_frame, text="Customer Name:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.customer_name_var = tk.StringVar()
        self.customer_name_entry = ttk.Entry(form_frame, textvariable=self.customer_name_var)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Date
        ttk.Label(form_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.date_var = tk.StringVar()
        self.date_dropdown = ttk.Combobox(
            form_frame, textvariable=self.date_var, values=self.get_last_30_days(), state="readonly"
        )
        self.date_dropdown.grid(row=1, column=1, padx=10, pady=5)
        self.date_dropdown.set("Select Date")
        
        # Manual date entry
        self.date_manual_entry = ttk.Entry(form_frame)
        self.date_manual_entry.grid(row=1, column=2, padx=10, pady=5)
        self.date_manual_entry.insert(0, "Or type manually")

        # Mileage
        ttk.Label(form_frame, text="Mileage (km):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.mileage_var = tk.StringVar()
        self.mileage_dropdown = ttk.Combobox(
            form_frame, textvariable=self.mileage_var, values=[str(i) for i in range(50, 501, 10)], state="readonly"
        )
        self.mileage_dropdown.grid(row=2, column=1, padx=10, pady=5)
        self.mileage_dropdown.set("Select Mileage")

        # Manual mileage entry
        self.mileage_manual_entry = ttk.Entry(form_frame)
        self.mileage_manual_entry.grid(row=2, column=2, padx=10, pady=5)
        self.mileage_manual_entry.insert(0, "Or type manually")

        # Fuel Added
        ttk.Label(form_frame, text="Fuel Added (liters):").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.fuel_var = tk.StringVar()
        self.fuel_dropdown = ttk.Combobox(
            form_frame, textvariable=self.fuel_var, values=[str(i) for i in range(1, 101)], state="readonly"
        )
        self.fuel_dropdown.grid(row=3, column=1, padx=10, pady=5)
        self.fuel_dropdown.set("Select Fuel")

        # Manual fuel entry
        self.fuel_manual_entry = ttk.Entry(form_frame)
        self.fuel_manual_entry.grid(row=3, column=2, padx=10, pady=5)
        self.fuel_manual_entry.insert(0, "Or type manually")

        # Price
        ttk.Label(form_frame, text="Price (currency):").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        self.price_var = tk.StringVar()
        self.price_dropdown = ttk.Combobox(
            form_frame, textvariable=self.price_var, values=["1.50", "1.75", "2.00", "2.25", "2.50"], state="readonly"
        )
        self.price_dropdown.grid(row=4, column=1, padx=10, pady=5)
        self.price_dropdown.set("Select Price")

        # Gas Station
        ttk.Label(form_frame, text="Gas Station:").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        self.station_var = tk.StringVar()
        station_options = ["Shell", "Petron", "Petro Gazz", "Phoenix", "Seaoil", "Flying V", "Unioil", "Clean Fuel"]
        self.station_dropdown = ttk.Combobox(
            form_frame, textvariable=self.station_var, values=station_options, state="readonly"
        )
        self.station_dropdown.grid(row=5, column=1, padx=10, pady=5)
        self.station_dropdown.set("Select Station")

        # Manual station entry
        self.station_manual_entry = ttk.Entry(form_frame)
        self.station_manual_entry.grid(row=5, column=2, padx=10, pady=5)
        self.station_manual_entry.insert(0, "Or type manually")

        # Add Entry Button
        add_button = ttk.Button(form_frame, text="Add Entry", command=self.add_entry)
        add_button.grid(row=6, column=0, columnspan=3, pady=20)

    def get_last_30_days(self):
        """Generate a list of the last 30 days."""
        today = datetime.today()
        return [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(30)]

    def add_entry(self):
        """Add a new fuel entry."""
        try:
            customer_name = self.customer_name_var.get()
            date = self.date_manual_entry.get() if self.date_manual_entry.get() != "Or type manually" else self.date_var.get()
            mileage = self.mileage_manual_entry.get() if self.mileage_manual_entry.get() != "Or type manually" else self.mileage_var.get()
            fuel = self.fuel_manual_entry.get() if self.fuel_manual_entry.get() != "Or type manually" else self.fuel_var.get()
            price = self.price_var.get()
            station = self.station_manual_entry.get() if self.station_manual_entry.get() != "Or type manually" else self.station_var.get()

            mileage, fuel, price = float(mileage), float(fuel), float(price)
            if not date or not station or not customer_name:
                raise ValueError("Date, Station, and Customer Name cannot be empty!")

            self.entries.append((customer_name, date, mileage, fuel, price, station))
            self.station_data[station].append(price)

            self.save_data()

            self.clear_fields()

            self.load_history()

            messagebox.showinfo("Success", "Entry added successfully!")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def clear_fields(self):
        """Clear all input fields."""
        self.customer_name_var.set("")
        self.date_dropdown.set("Select Date")
        self.date_manual_entry.delete(0, tk.END)
        self.date_manual_entry.insert(0, "Or type manually")
        
        self.mileage_dropdown.set("Select Mileage")
        self.mileage_manual_entry.delete(0, tk.END)
        self.mileage_manual_entry.insert(0, "Or type manually")
        
        self.fuel_dropdown.set("Select Fuel")
        self.fuel_manual_entry.delete(0, tk.END)
        self.fuel_manual_entry.insert(0, "Or type manually")
        
        self.price_dropdown.set("Select Price")
        
        self.station_dropdown.set("Select Station")
        self.station_manual_entry.delete(0, tk.END)
        self.station_manual_entry.insert(0, "Or type manually")

    def save_data(self):
        """Save entries and station data to a JSON file."""
        with open("fuel_data.json", "w") as f:
            json.dump({"entries": self.entries, "station_data": self.station_data}, f)

    def load_data(self):
        """Load entries and station data from a JSON file."""
        if os.path.exists("fuel_data.json"):
            with open("fuel_data.json", "r") as f:
                data = json.load(f)
                self.entries = data.get("entries", [])
                self.station_data = defaultdict(list, data.get("station_data", {}))

    def create_view_history_tab(self):
        """Create the View History tab."""
        self.view_history_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.view_history_tab, text="View History")

        columns = ("customer_name", "date", "mileage", "fuel", "price", "station")
        self.history_table = ttk.Treeview(
            self.view_history_tab, columns=columns, show="headings", height=20
        )
        self.history_table.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        for col in columns:
            self.history_table.heading(col, text=col.replace("_", " ").capitalize())
            self.history_table.column(col, anchor="center", width=100)

        self.load_history()

        scrollbar = ttk.Scrollbar(self.view_history_tab, orient="vertical", command=self.history_table.yview)
        self.history_table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

    def load_history(self):
        """Load all saved entries into the history table."""
        for row in self.history_table.get_children():
            self.history_table.delete(row)

        for entry in self.entries:
            self.history_table.insert("", "end", values=entry)

    def create_analysis_tab(self):
        """Create the Analysis tab."""
        self.analysis_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.analysis_tab, text="Analysis")

        self.analysis_tab.grid_rowconfigure(0, weight=1)
        self.analysis_tab.grid_rowconfigure(2, weight=1)
        self.analysis_tab.grid_columnconfigure(0, weight=1)
        self.analysis_tab.grid_columnconfigure(2, weight=1)

        analysis_frame = ttk.Frame(self.analysis_tab)
        analysis_frame.grid(row=1, column=1, padx=20, pady=20)

        ttk.Checkbutton(analysis_frame, text="Enable Efficiency Calculation", variable=self.enable_efficiency).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        ttk.Checkbutton(analysis_frame, text="Enable Station Comparison", variable=self.enable_comparison).grid(row=1, column=0, columnspan=2, sticky="w", pady=5)
        ttk.Checkbutton(analysis_frame, text="Enable Graphs", variable=self.enable_graphs).grid(row=2, column=0, columnspan=2, sticky="w", pady=5)

        calc_eff_button = ttk.Button(analysis_frame, text="Calculate Efficiency", command=self.calculate_efficiency)
        calc_eff_button.grid(row=3, column=0, columnspan=2, pady=10)

        compare_button = ttk.Button(analysis_frame, text="Compare Stations", command=self.compare_stations)
        compare_button.grid(row=4, column=0, columnspan=2, pady=10)

        graph_button = ttk.Button(analysis_frame, text="View Graphs", command=self.view_graphs)
        graph_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate_efficiency(self):
        """Calculate and display fuel efficiency."""
        if not self.enable_efficiency.get():
            messagebox.showinfo("Info", "Efficiency calculation is disabled.")
            return

        try:
            if not self.entries:
                raise ValueError("No entries available!")

            total_mileage = sum(entry[2] for entry in self.entries)
            total_fuel = sum(entry[3] for entry in self.entries)

            efficiency = total_mileage / total_fuel
            consumption = total_fuel / total_mileage

            messagebox.showinfo("Fuel Efficiency", f"Efficiency: {efficiency:.2f} km/L\nConsumption: {consumption:.2f} L/km")
        except ValueError as e:
            messagebox.showerror("Error", f"Cannot calculate efficiency: {e}")

    def compare_stations(self):
        """Compare gas stations by average fuel price."""
        if not self.enable_comparison.get():
            messagebox.showinfo("Info", "Station comparison is disabled.")
            return

        try:
            if not self.station_data:
                raise ValueError("No station data available!")

            comparisons = []
            for station, prices in self.station_data.items():
                avg_price = sum(prices) / len(prices)
                comparisons.append(f"{station}: {avg_price:.2f} per unit")

            messagebox.showinfo("Gas Station Comparison", "\n".join(comparisons))
        except ValueError as e:
            messagebox.showerror("Error", f"Cannot compare stations: {e}")

    def view_graphs(self):
        """Plot graphs of gas station prices."""  
        if not self.enable_graphs.get():
            messagebox.showinfo("Info", "Graph viewing is disabled.")
            return

        try:
            if not self.station_data:
                raise ValueError("No data to plot!")

            for station, prices in self.station_data.items():
                plt.plot(prices, label=station)

            plt.title("Fuel Prices by Station")
            plt.xlabel("Entry Number")
            plt.ylabel("Price (Currency)")
            plt.legend()
            plt.show()
        except ValueError as e:
            messagebox.showerror("Error", f"Cannot display graphs: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FuelTracker(root)
    root.mainloop()
