# Coffee Machine Simulation

This is a Python-based simulation of a coffee machine, implemented as a practice project to enhance my programming skills. The program was written in a single evening, aiming to replicate the functionality of a real coffee machine, following specific requirements.

## Features

- **Menu Options**: Offers three types of coffee - espresso, latte, and cappuccino, each with unique ingredient requirements and costs.
- **Resource Management**: Tracks and manages resources (water, milk, coffee) to ensure sufficient supplies for coffee preparation.
- **Coin Handling**: Accepts multiple denominations of coins, calculates the total amount inserted, and provides change if necessary.
- **Transaction Processing**: Ensures users pay the correct amount for their drink, provides feedback if insufficient funds are inserted, and adds profits to the machine's funds.
- **Reports**: Generates a detailed report on the machine's current resource levels and cash reserves.
- **Shutdown Option**: Includes a secret `off` command for maintainers to turn off the machine.
- **Interactive Cycles**: Continuously prompts users for new orders or commands after each action.

## Files

1. **`coffee_data.py`**: Contains the data structures defining the menu, initial resources, and coin values.
2. **`coffee_machine.py`**: Implements the `coffeeMachine` class, encapsulating the logic for order processing, payment handling, brewing, and reporting.
3. **`main.py`**: Provides the entry point for running the simulation.

## How It Works

1. Users are prompted to select a coffee type, request a report, or turn off the machine.
2. If a coffee type is chosen:
   - The program checks if sufficient resources are available.
   - Users are prompted to insert coins to match the cost of the selected drink.
   - Once payment is processed, the coffee is brewed, resources are updated, and any necessary change is returned.
3. The cycle repeats until the machine is turned off.

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/vadikzhuk/coffee_machine.git
1. Run the program:
   ```bash
   python3 main.py

## Requirements
This program was developed with the following specifications in mind:
- Adequate resource checking and feedback.
- Coin processing and transaction verification.
- Resource and profit tracking with detailed reporting.

These requirements align with the detailed instructions provided in the Coffee Machine Program Requirements PDF document.

## Purpose
This project was created to improve my understanding of Python classes, dictionaries, and interactive input handling. The functionality mimics a real coffee machine, making it a practical and enjoyable exercise.
