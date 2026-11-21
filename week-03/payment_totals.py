import os
import my_tools

# This looks for the course materials folder you already have
DATA_PATH = "../ostad-de-bootcamp-main/module-02/data/raw_sales.txt"

def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]

def main():
    totals = {}
    counts = {}

    for line in read_lines(DATA_PATH):
        # Assuming the file is pipe-separated. If it's comma-separated, change "|" to ","
        parts = line.split("|") 
        if len(parts) < 7:
            continue

        if parts[6].strip().lower() == "cancelled":
            continue

        method = parts[4].strip().lower()
        amount = my_tools.clean_amount(parts[5])

        totals[method] = totals.get(method, 0) + amount
        counts[method] = counts.get(method, 0) + 1

    print("payment ধরে হিসাব (বাতিল বাদে)")
    print()

    grand = 0.0
    for method, subtotal in totals.items():
        print(f"{method:<18}{counts[method]}টা   {my_tools.taka(subtotal)}")
        grand += subtotal

    print()
    print(f"সব মিলিয়ে: {my_tools.taka(grand)}")

if __name__ == "__main__":
    main()