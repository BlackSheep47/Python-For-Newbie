print(" ____  ______    ___  ___ ___  _____      _____ __ __   ___   ____  ")
print("|    ||      |  /  _]|   |   |/ ___/     / ___/|  |  | /   \ |    \ ")
print(" |  | |_|  |_||    _]|  \_/  |\__  |     \__  ||  _  ||  O  ||   _/ ")
print(" |  |   |  |  |   [_ |   |   |/  \ |     /  \ ||  |  ||     ||  |   ")
print(" |  |   |  |  |     ||   |   |\    |     \    ||  |  ||     ||  |   ")
print("|____|  |__|  |_____||___|___| \___|      \___||__|__| \___/ |__| ")



iteams = []
prices = []
total = 0

while True:
    iteam = input("Enter iteam to buy (q to quit): ")
    if iteam.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {iteam}: $"))
        iteams.append(iteam)
        prices.append(price)
        
        
print("|  |  | /   \ |  |  ||    \        /  ] /    ||    \|      |")
print("|  |  ||     ||  |  ||  D  )      /  / |  o  ||  D  )      |")
print("|  ~  ||  O  ||  |  ||    /      /  /  |     ||    /|_|  |_|")
print("|___, ||     ||  :  ||    \     /   \_ |  _  ||    \  |  |  ")
print("|     ||     ||     ||  .  \    \     ||  |  ||  .  \ |  |  ")
print("|____/  \___/  \__,_||__|\_|     \____||__|__||__|\_| |__|  ")

for iteam in iteams:
    print(iteam)
    
for price in prices:
    total = total + price
    

print(f"Total Amount : ${total}")


    

