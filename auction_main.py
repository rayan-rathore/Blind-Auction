from art import logo
print(logo)

bid_data = {}

def valid_name():
    while True:
        person_name = input("👤 what is your name? \n").strip()
        if person_name != '':
            return person_name
        else:
            print("❌ Invalid input. Please type valid name.")

def valid_bid():
    while True:
        try:
            bid_amount = int(input("💰 what is your bid amount? \n"))
            if bid_amount > 0:
                return bid_amount
            else:
                print("⚠️ Bid must be greater than 0.")
        except ValueError:
            print("❌ Please enter a valid number. without any symbol or letter.")

def get_winner(bid_data):
    highest_bid = 0
    winner = ''
    for bidders in bid_data:
        bid_amount = bid_data[bidders]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidders
    return winner, highest_bid

print("🏁 Welcome to the Blind Auction 🕶️💰")
print("-" * 35)

while True:
    person_name= valid_name()
    bid_amount = valid_bid()

    bid_data[person_name] = bid_amount

    ask_again = input("🙋 are there any other bidders? type 'yes' or 'no' \n").lower()
    if ask_again == 'yes' or ask_again == "y":
        print("\n" * 200)
    else:
        break

    get_winner(bid_data)

winner, highest_bid = get_winner(bid_data)
print("\n📊 Auction Results")
print("-" * 20)

print(f"All bidders: {bid_data}")
print(f"The winner is '{winner}' with a highest bid of '₹ {highest_bid}'.")

print(f"Well played! Congratulations '{winner}'!")


