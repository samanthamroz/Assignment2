import cashier
import data
import sandwich_maker

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()

def complete_transaction(size):
    if not sandwich_maker_instance.check_resources(recipes[size]["ingredients"]):
        return
    if not cashier_instance.transaction_result(cashier_instance.process_coins(), recipes[size]["cost"]):
        return
    sandwich_maker_instance.make_sandwich(size, recipes[size]["ingredients"])

def main():
    ###  write the rest of the codes ###
    user_input = None

    while True:
        user_input = input("What would you like? (small/medium/large/off/report): ")
        if user_input == "small" or user_input == "medium" or user_input == "large":
            complete_transaction(user_input)
        elif user_input == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} pound(s)")
        elif user_input == "off":
            exit()
        else:
            user_input = input("Please try again.")

if __name__=="__main__":
    main()
