# Simple Calculator (Python)

A tiny, interactive command‑line calculator written in Python.

## Overview
This script prompts for two numbers and an operation, then prints the result. It demonstrates basic input handling, control flow with `match`/`case`, and simple error handling.

## Features
- Basic operations: addition, subtraction, multiplication, division
- Case‑insensitive operation selection (`A/a`, `S/s`, `M/m`, `D/d`)
- Guards against non‑numeric input
- Division‑by‑zero protection

## Requirements
- Python 3.10+ (uses `match`/`case` syntax)

## Usage
From the project directory, run:

```bash
python calculator.py
```

Follow the prompts:

```
Welcome :-)
Enter first number:  10
Enter second number:  5
Press following for:
 A or a = Addition
 S or s = Subtraction
 M or m = Multiplication
 D or d = Division
 op = a
Answer =  15.0
Thank You for using this calculator
```

### Error Handling
- If either number is not a valid numeric value, the program prints an error and exits.
- Division by zero is prevented with a friendly message.
- If an unsupported operation is chosen, the program asks you to choose a correct operation.

## File Structure
- `calculator.py`: Main CLI calculator script
- `README.md`: This documentation

## License
MIT
