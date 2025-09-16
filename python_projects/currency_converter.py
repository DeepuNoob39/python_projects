def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                raise ValueError
            return amount
        except:
            print("Enter valid amount")
            
def get_currency(label):
    currencies = ("USD", "INR", "EURO")
    while True:
        currency = input(f"Enter {label} Currency(USD/INR/EURO): ").upper()
        
        if currency not in currencies:
            print("Please enter valid input.")
        else:
            return currency
        
def conversion(amount, source_currency, target_currency):
    rates = {"USD" : {"EURO" : 0.85, "INR" : 88.05},
            "INR" : {"USD" : 0.011, "EURO" : 0.0096},
            "EURO" : {"USD" : 1.18, "INR" : 103.76}}
    
    if source_currency == target_currency:
        return amount
    else:
        return amount * rates[source_currency][target_currency]
        
    
    
    





def main():
    amount = get_amount()
    source_currency = get_currency("source")
    target_currency = get_currency("target")
    result = conversion(amount, source_currency, target_currency)
    
    print(f"{amount} {source_currency} equals to {result} {target_currency}")
    
if __name__ == "__main__":
    main()