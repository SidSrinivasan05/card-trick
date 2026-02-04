# 📦 Card Trick – Algorithmic Card Position Forcing

A Python project that models a mathematical *card trick* using configurable pile folding.  
Given a deck size and number of piles, this program finds the sequence of pile folds required to **force a card to a chosen position**, regardless of where it starts.

The core idea is to model the deck as a list of positions, then explore all possible sequences of pile orderings to find one that guarantees convergence to the desired index.

---

## 🧠 What It Does

This repository includes:

- A **search algorithm** (`search_until_converged`) that uses breadth‑first search (BFS) over states to find minimal sequences of folds.
- A **fold operation** that simulates splitting the deck into piles and stacking them.
- A simple **command‑line interface** to enter deck size, number of piles, and the target position.
- A convergence test to check when the chosen card’s position becomes *determined* under all possible initial positions.

This can be used to explore why certain card tricks (e.g., the classic 21-card trick) always force a card into a specific position.

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/SidSrinivasan05/card-trick.git
cd card-trick

## Requirements

```
pip install numpy
```


## Usage

Run the script:

```
python main.py
```

You will be prompted for:

n — number of cards (must be divisible by p)

p — number of piles

s — position you want to force (1-indexed)

Example input:

```
How many cards are you playing with?
> 51
How many piles do you want to split the cards into?
> 3
Where do you want the card to end up? (1 to 51)
> 26
```

The program will print:

Number of steps to reach convergence

The fold sequence (pile indices)

The final array mapping (which card positions end up where)

If no forcing sequence exists, it will report failure.
