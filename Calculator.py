import cal_mod


### Start

print("""
      Welcome to the Calculator Application....
      Please select what you want to do
      """)

while True:
    cal_mod.mainmenu()
    user_selection = int(input("Selection: "))
    if user_selection == 5: 
        break
    
    elif user_selection == 1:
        user_first_addition = int(input("Type the first numbber: "))
        user_second_addition = int(input("Type the second number: "))
        sum = cal_mod.addition(user_first_addition, user_second_addition)
        print(f"{user_first_addition} + {user_second_addition} = {sum}")
        print(input("Press enter to head back to the main menu"))
    
    elif user_selection == 2:
        user_first_subtraction = int(input("Type the first numbber: "))
        user_second_subtraction = int(input("Type the second number: "))
        sum = cal_mod.subtraction(user_first_subtraction, user_second_subtraction)
        print(f"{user_first_subtraction} - {user_second_subtraction} = {sum}")
        print(input("Press enter to head back to the main menu"))
    
    elif user_selection == 3:
        user_first_div = int(input("Type the first numbber: "))
        user_second_div = int(input("Type the second number: "))
        sum = cal_mod.division(user_first_div, user_second_div)
        print(f"{user_first_div} / {user_second_div} = {sum}")
        print(input("Press enter to head back to the main menu"))

    elif user_selection == 4:
        user_first_multi = int(input("Type the first numbber: "))
        user_second_multi = int(input("Type the second number: "))
        sum = cal_mod.multiplication(user_first_multi, user_second_multi)
        print(f"{user_first_multi} x {user_second_multi} = {sum}")
        print(input("Press enter to head back to the main menu"))
    
print("Goodbye")