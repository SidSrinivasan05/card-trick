📦 Card Trick – Algorithmic Card Position Forcing

A Python project that models a mathematical card trick using configurable pile folding.
Given a deck size and number of piles, this program finds the sequence of pile folds required to force a card to a chosen position, regardless of where it starts.

The core idea is to model the deck as a list of positions, then explore all possible sequences of pile orderings to find one that guarantees convergence to the desired index.

🧠 What It Does

This repository includes:

A search algorithm (search_until_converged) that uses breadth‑first search (BFS) over states to find minimal sequences of folds.

A fold operation that simulates splitting the deck into piles and stacking them.

A simple command‑line interface to enter deck size, number of piles, and the target position.

A convergence test to check when the chosen card’s position becomes determined under all possible initial positions.

This can be used to explore why certain card tricks (e.g., the classic 21‑card trick) always force a card into a specific position.

📥 Installation

Clone the repository:

git clone https://github.com/SidSrinivasan05/card-trick.git
cd card-trick


Create a virtual environment (optional, recommended):

python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows


Install requirements (if any):

pip install -r requirements.txt


If a requirements file is not included yet, the only required dependency is numpy.
You can install it manually:
pip install numpy

🚀 Usage

Run the script:

python main.py


You will be prompted for:

n — number of cards (must be divisible by p)

p — number of piles to split into

s — position you want to force

Example input:

How many cards are you playing with?
> 51
How many piles do you want to split the cards into?
> 3
Where do you want the card to end up? (1 to 51)
> 26


The program will explore every fold sequence and print:

Number of steps to reach convergence

The fold sequence (pile indices)

The final array mapping (which card positions end up where)

If no forcing sequence exists, it will report failure.

🧮 How It Works
Fold Operation

The deck is represented as a list of integers indicating positions.
Splitting into p piles rearranges the mapping of initial positions to new positions.

The fold function takes:

fold(arr, f, n, p)


arr: current mapping of positions

f: which pile index is being placed on top

n: total cards

p: number of piles

It returns the new mapping after the fold.

Convergence

The trick is considered to “force” the target position if, for every possible starting index, the final position of the card is the same — i.e., the mapping array becomes constant at that index.

The BFS explores all sequences of folds and returns the shortest one that achieves this.

🤓 Example Projects

This approach generalizes the math behind many card tricks — for example:

The 21‑card trick converges to the middle card

In some configurations, forcing arbitrary positions is impossible

You can modify the code to explore other card trick variants or visualize the permutation behavior.

🧪 Testing

Here are some examples worth testing:

n	p	target	Status
21	3	11	Should converge (classic card trick)
51	3	26	Should converge (center)
51	3	1	Impossible to force
40	4	10	Check if forcing exists
🛠 Future Improvements

Add visualizations of state space and convergence

Support interactive mode to visualize pile splits

Add more fold strategies or randomization

Export sequences as animation or SVG

📜 License

Add your preferred license here (MIT, GPL, etc.).
If none currently, consider adding one so others can use your work.

📌 Summary

This project explores the mathematics behind card tricks by modeling permutations and searching for forcing sequences. It’s both a fun programming challenge and an example of how combinatorics can be applied to classic puzzles.

Let me know if you want me to tailor the README with actual code snippets from the repository or a badge section with build/tests statuses!
