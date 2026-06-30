# Soccer Player Performance Tracker

A beginner-friendly Python project that records soccer players' performance by storing the number of goals scored in each match. The program generates a summary table and allows users to view detailed statistics for each player.

## Features

- Register multiple soccer players
- Record goals scored in each match
- Calculate the total number of goals
- Store player information using dictionaries
- Store multiple players using a list
- Display a summary table
- View detailed match-by-match statistics

## Technologies Used

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/soccer-player-performance-tracker.git
```

2. Navigate to the project folder:

```bash
cd soccer-player-performance-tracker
```

3. Run the script:

```bash
python main.py
```

## Example

### Input

```text
Name: Neymar
How many matches did Neymar play? 3

Goals scored in match 1: 2
Goals scored in match 2: 0
Goals scored in match 3: 1
```

### Output

```text
Code  Name         Goals          Total
==================================================
0     Neymar      [2, 0, 1]         3
==================================================

Show data for which player? 0

Performance report for Neymar:
Match 1: 2 goal(s)
Match 2: 0 goal(s)
Match 3: 1 goal(s)
```

## Learning Objectives

This project demonstrates:

- Dictionaries
- Lists
- Nested data structures
- Dictionary copying with `copy()`
- List copying with slicing (`[:]`)
- Loops (`for` and `while`)
- `enumerate()`
- Data organization and reporting

## Data Structure

Each player is stored as:

```python
{
    "name": "Neymar",
    "goals": [2, 0, 1],
    "total": 3
}
```

All players are stored inside a list:

```python
players = [
    {
        "name": "Neymar",
        "goals": [2, 0, 1],
        "total": 3
    },
    {
        "name": "Vinicius",
        "goals": [1, 1],
        "total": 2
    }
]
```
