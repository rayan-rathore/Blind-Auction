# 🕶️ Blind Auction Project (Python)

A command-line **Blind Auction** program built using Python.  
The project allows multiple users to place secret bids, validates inputs, clears the screen between bidders for anonymity, and determines the highest bidder at the end.

---

## 🚀 Features

- 👤 Validates bidder names (no empty input)
- 💰 Ensures bid amounts are positive integers
- 🕶️ Anonymous bidding by clearing the screen between bidders
- 📊 Stores bids using a Python dictionary
- 🏆 Automatically determines the highest bidder
- 😊 User-friendly CLI with emojis for better experience

---

## 🧠 Concepts Used

- Python functions
- `while` loops
- Dictionaries
- Input validation
- Exception handling (`try / except`)
- Function return values
- Clean code structure

---

## 🧪 How It Works

1. The program displays a logo and welcome message
2. Each bidder enters:
   - Their name
   - Their bid amount
3. The screen clears before the next bidder (blind auction)
4. When bidding ends, the program:
   - Displays all bids
   - Announces the winner with the highest bid

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Clone the repository or copy the code
3. Run the file:
   ```bash
   python blind_auction.py

🏆 Sample Output
🏁 Welcome to the Blind Auction 🕶️💰
-----------------------------------
📊 Auction Results
------------------
All bidders: {'Alice': 500, 'Bob': 750, 'Charlie': 600}
The winner is 'Bob' with a highest bid of '₹ 750'
Well played! Congratulations 'Bob'!

📌 What I Learned

How to structure programs using functions

Why returning values from functions is important

How to validate user input properly

How to handle real-world edge cases like invalid data

Writing readable and user-friendly CLI programs
