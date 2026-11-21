def clean_amount(text):
    """Remove ৳ and commas, return as a float."""
    return float(text.replace("৳", "").replace(",", "").strip())

def taka(amount):
    """1240.5 -> '৳1240.50'"""
    return f"৳{amount:.2f}"

if __name__ == "__main__":
    print(clean_amount(" ৳ 1,240.50 "))    # 1240.5
    print(taka(1240.5))                     # ৳1240.50