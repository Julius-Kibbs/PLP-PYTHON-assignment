# this is the fucntion responsible for calculating the discount on an item
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else :
        return price

# this is where we take input from the user
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after applying the discount is: Tshs{discount_price:.2f}")