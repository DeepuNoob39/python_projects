import sys

def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                raise ValueError
            return amount
        except ValueError:
            print("Enter valid amount")
            
def get_currency(label):
    currencies = ("USD", "INR", "EURO")
    while True:
        currency = input(f"Enter {label} Currency(USD/INR/EURO): ").upper().strip()
        
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
  

def conversion_all(amount, source_currency, target_currency):
    rates = {"USD" : {"EURO" : 0.85, "INR" : 88.05},
            "INR" : {"USD" : 0.011, "EURO" : 0.0096},
            "EURO" : {"USD" : 1.18, "INR" : 103.76}}
    
    out = {}
    
    for j in rates[source_currency].keys():
        x =amount * rates[source_currency][j]
        out.update({j : x})
    return out

def permission1(amount, source_currency, result_all):
    list_of_all_conversions = []
    while True:
        perm1 = input(f"Do you want a conversion of {amount} {source_currency} to all currencies available right now?(y/n) ").lower().strip()
        if perm1 == "y":
            for i,j in result_all.items():
                list_of_all_conversions.append(f"{amount} {source_currency} equals to {j} {i}")
            return list_of_all_conversions
        elif perm1 == "n":
            return
        else:
            print("Please enter a valid input from (y/n)")
            
def terminate():
    while True:
        terminate_answer = input("Do you want to terminate the program?(y/n) ").lower().strip()
        if terminate_answer == "y":
            return True
        elif terminate_answer == "n":
            return
        else:
            print("Please enter a valid input from (y/n)")
    

def main():
    count = 0
    history =[]
    try:
        while True:
            count += 1
            amount = get_amount()
            source_currency = get_currency("Source")
            target_currency = get_currency("Target")
            
            result = conversion(amount, source_currency, target_currency)
            print(f"{amount} {source_currency} equals to {result} {target_currency}")
            
            result_all = conversion_all(amount, source_currency, target_currency)
            
            
            
            history.append(f"{amount} {source_currency} equals to {result} {target_currency}")
            
            all_conversions = permission1(amount, source_currency, result_all)
            if all_conversions is not None:
                for i in all_conversions:
                    print(i)
            
            
            if count > 1:
                permission2 = input("Do you want to see the most recent conversions you made?(y/n) ").lower().strip()
                if permission2 == "y":
                    reversed_history = reversed(history)
                    for i in reversed_history:
                        print(i)
                        
            if terminate():
                break
    except KeyboardInterrupt:
        sys.exit()  
    
if __name__ == "__main__":
    main()