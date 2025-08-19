# drawn-number
A Python script that generates a tuple of five random numbers and displays the highest and lowest values.

# 🎲 Random Number Min/Max Finder

A non-interactive Python script that generates a tuple of five random numbers and then identifies the highest and lowest values within that set.

## Features

* **Random Number Generation**: Creates a tuple of five random integers, with each integer being between 1 and 5.
* **Min/Max Analysis**: Automatically finds and displays the minimum and maximum values from the generated tuple using Python's built-in `min()` and `max()` functions.
* **Simulated Delay**: Uses `time.sleep()` to create a brief 1-second pause to simulate a "generation" process.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `drawn_number.py`).
3.  Run the script from your terminal:
    ```sh
    python drawn_number.py
    ```
4.  The script will run automatically, display the list of generated numbers, and then show the highest and lowest values.

### Example Output

```sh
> python drawn_number.py
Generating 5 numbers...
(3, 5, 1, 5, 2)
The highest value was: 5
The lowest value was: 1
```
