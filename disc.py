def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return  price - ((discount_percent/100) * price)
    else:
        return price

price = float(input("Enter the priginal price of the item: "))
discount_percent= float(input("enter the discount percentage: "))

selling_price = calculate_discount(price, discount_percent)
print(selling_price)


