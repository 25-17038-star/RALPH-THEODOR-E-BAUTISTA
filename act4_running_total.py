total = 0
count = 0

while True:
    price = float(input("Price (0 to stop): "))
    if price == 0:
        break
    total += price
    count += 1

print(f"Items: {count}  Total: {total:.2f}")
print(f"Average: {total / count:.2f}" if count else "Average: 0.00")
