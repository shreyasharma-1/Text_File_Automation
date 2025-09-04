"""
You had saved the items and their price details in a text file, which you
purchased yesterday from a nearby super market.

You need to know:

1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?

5. What is the final amount did you pay after the discount?

Help yourself by writing a python code to do this. Include necessary code to
handle the possible exceptions.

Note:

. Data is stored in a text file Purchase-1.txt.

. Each line contains one item's details.

. Item name and price is separated by a space.

. You have to enter the file name during run time.

Sample input 1:

Purchase-1.txt

Chocolate 50

Biscuit 35

Icecream 50
(blank line)
Discount 5

Sample output 1:

Enter the file name: Purchase-1

No of items purchased: 3

No of free items: 0

Amount to pay: 135

Discount given: 5

Final amount paid: 130

Sample input 2:

Purchase-1.txt

Chocolate 50

Biscuit 35

Icecream 50

Rice 100

Chicken 250

(blank line)

Perfume Free

Soup Free

(blank line)
Discount 80

Sample output 2:

Enter the file name: Purchase-1

No of items purchased: 5

No of free items: 2

Amount to pay: 485

Discount given: 80

Final amount paid: 405
"""


try:
    fileName = input("Enter the file name: ") + ".txt"
    with open(fileName, "r") as file:
        lines = file.readlines()

    totalAmount = 0
    discountAmount = 0
    purchasedItemCount = 0
    freeItemCount = 0

    for line in lines:
        if line.strip() == "":
            continue
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        item, price = parts
        if price.lower() == "free":
            freeItemCount += 1
        elif item.lower() == "discount":
            discountAmount += int(price)
        else:
            totalAmount += int(price)
            purchasedItemCount += 1

    finalAmount = totalAmount - discountAmount

    print(f"No of items purchased: {purchasedItemCount}")
    print(f"No of free items: {freeItemCount}")
    print(f"Amount to pay: {totalAmount}")
    print(f"Discount given: {discountAmount}")
    print(f"Final amount paid: {finalAmount}")

except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Invalid data found in the file.")
except Exception as e:
    print("An error occurred:", str(e))
