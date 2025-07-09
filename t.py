def menu():
    print("Welcome To Bethesda Restaurant")
    print("1. Breakfast")
    print("2. Lunch")

def handle_selection(selected_value):
    if selected_value == 1:
        print("You have selected Breakfast.")
        print("Pancakes @ Shs20,000.")
        print("Omelette and Toast @ Shs20,000.")
        print("Cake @ Shs20,000.")
        print("All come with a side of Black Tea or Milk Tea.")
    elif selected_value == 2:
        print("You have selected Lunch.")
        print("Beans @ Shs20,000.")
        print("Chicken @ Shs20,000.")
        print("Liver @ Shs25,000.")
        print("All Dishes come with a side of Rice, Chips or Matooke and a cold drink.")
    else:
        print("Please enter the correct selection")

def main():
    menu()
    selected_value = int(input("Please make a choice:"))
    handle_selection(selected_value)

if __name__ == "__main__":
    main() 



