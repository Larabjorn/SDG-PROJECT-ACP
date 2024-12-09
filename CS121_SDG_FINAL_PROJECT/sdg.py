import csv
from datetime import datetime

class FuelTracker:
    def __init__(self):
        self.logs = []

    def add_fuel_entry(self):
        try:
            date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ").strip()
            date = date if date else datetime.now().strftime("%Y-%m-%d")
            mileage = float(input("Enter the mileage (in km): ").strip())
            fuel_added = float(input("Enter the fuel added (in liters): ").strip())
            price = float(input("Enter the total price (in currency): ").strip())

            entry = {
                "date": date,
                "mileage": mileage,
                "fuel_added": fuel_added,
                "price": price,
            }
            self.logs.append(entry)
            print("Fuel entry added successfully!")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    def view_logs(self):
        if not self.logs:
            print("No fuel logs available.")
            return
        for idx, log in enumerate(self.logs, start=1):
            print(f"{idx}. Date: {log['date']}, Mileage: {log['mileage']} km, "
                  f"Fuel Added: {log['fuel_added']} liters, Price: {log['price']}")

    def calculate_efficiency(self):
        if len(self.logs) < 2:
            print("Not enough data to calculate efficiency.")
            return
        efficiencies = []
        for i in range(1, len(self.logs)):
            distance = self.logs[i]["mileage"] - self.logs[i - 1]["mileage"]
            fuel = self.logs[i]["fuel_added"]
            if fuel > 0:
                efficiency = distance / fuel
                efficiencies.append(efficiency)
                print(f"Trip {i}: {efficiency:.2f} km/l")
        if efficiencies:
            avg_efficiency = sum(efficiencies) / len(efficiencies)
            print(f"Average Efficiency: {avg_efficiency:.2f} km/l")

    def total_expenses(self):
        total = sum(log["price"] for log in self.logs)
        print(f"Total Fuel Expenses: {total:.2f}")

    def save_to_csv(self, filename="fuel_logs.csv"):
        if not self.logs:
            print("No data to save.")
            return
        keys = self.logs[0].keys()
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.logs)
        print(f"Fuel logs saved to {filename}")

# Main Menu for User Interaction
if __name__ == "__main__":
    tracker = FuelTracker()

    while True:
        print("\nFuel Tracker Menu:")
        print("1. Add Fuel Entry")
        print("2. View Logs")
        print("3. Calculate Efficiency")
        print("4. Show Total Expenses")
        print("5. Save Logs to CSV")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            tracker.add_fuel_entry()
        elif choice == "2":
            tracker.view_logs()
        elif choice == "3":
            tracker.calculate_efficiency()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            tracker.save_to_csv()
        elif choice == "6":
            print("Exiting Fuel Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
