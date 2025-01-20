import pandas as pd
from datetime import datetime

# Load the menu from a CSV file
menu_file = 'menu.csv'  # Default menu file
while True:
    try:
        menu = pd.read_csv(menu_file)
        break  # Exit loop if the file is successfully read
    except FileNotFoundError:
        print(f"Error: {menu_file} not found.")
        menu_file = input("Please provide a valid file path: ")

menu.set_index('Item', inplace=True)
print("Welcome to Python Restaurant")
print("Menu:")
print(menu)

# Initialize order details and feedback list
order_total = 0
order_details = []
feedback_list = []

while True:
    item = input("Enter the name of the item you want to order: ").capitalize()
    if item in menu.index:
        quantity = int(input(f"How many '{item}' do you want to order? "))
        price_per_item = menu.loc[item, 'Price']
        total_price = price_per_item * quantity
        order_total += total_price
        # Capture the current date and time
        order_time = datetime.now()
        order_details.append({
            'Item': item,
            'Quantity': quantity,
            'Price per Item': price_per_item,
            'Total Price': total_price,
            'Order Time': order_time
        })
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Sorry, '{item}' is not available.")
    
    another_order = input("Do you want to add another item? (yes/no): ").lower()
    if another_order != 'yes':
        break

# Convert order details to a DataFrame
order_df = pd.DataFrame(order_details)

# Ask for discount and tip
discount = float(input("Enter discount percentage (if any): "))
tip = float(input("Enter tip amount (if any): "))

# Calculate total amount
final_total = order_total * (1 - discount / 100) + tip

# Calculate tax
tax = order_total * 0.10  # 10% tax
final_total_with_tax = final_total + tax

# Save order summary to Excel
order_df.to_excel('order_summary.xlsx', index=False)

print("\nOrder Summary:")
print(order_df)
print(f"Total amount to pay: {order_total} Rs")
print(f"Discount: {discount}%")
print(f"Tip: {tip} Rs")
print(f"Tax: {tax} Rs")
print(f"Final total after discount, tip, and tax: {final_total_with_tax} Rs")

# Collect customer feedback
feedback = input("Please provide your feedback on your dining experience: ")
feedback_list.append({'Order Time': order_time, 'Feedback': feedback})

# Optionally, save feedback to a CSV file
feedback_df = pd.DataFrame(feedback_list)
feedback_df.to_csv('customer_feedback.csv', index=False)