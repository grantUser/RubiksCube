# RubiksCube

## Overview

This Python program simulates a Rubik's Cube and provides basic functionality to manipulate and display its state. It serves as a simulator rather than a solver, allowing users to perform standard Rubik's Cube moves and check the cube's state.

## Usage

1. **Initialization**: Create a Rubik's Cube object using the `RubiksCube` class.

    ```python
    cube = RubiksCube()
    ```

2. **Display**: To display the current state of the Rubik's Cube, use the `display` method.

    ```python
    cube.display()
    ```

3. **Moves**: The following methods perform standard Rubik's Cube moves:

    - `move_U()`: Perform the U (up) move.
    - `move_U_prime()`: Perform the U' (up prime) move.
    - `move_R()`: Perform the R (right) move.
    - `move_R_prime()`: Perform the R' (right prime) move.
    - `move_L()`: Perform the L (left) move.
    - `move_L_prime()`: Perform the L' (left prime) move.
    - `move_D()`: Perform the D (down) move.
    - `move_D_prime()`: Perform the D' (down prime) move.
    - `move_F()`: Perform the F (front) move.
    - `move_F_prime()`: Perform the F' (front prime) move.
    - `move_B()`: Perform the B (back) move.
    - `move_B_prime()`: Perform the B' (back prime) move.

4. **Check Completion**: To check if the Rubik's Cube is solved, use the `is_complete` method.

    ```python
    if cube.is_complete():
        print("The Rubik's Cube is solved!")
    else:
        print("The Rubik's Cube is not yet solved.")
    ```

## Example

```python
# Create a Rubik's Cube
cube = RubiksCube()

# Display the initial state
print("Initial state:")
cube.display()

# Perform a sequence of moves
cube.move_U()
cube.move_R()
cube.move_F_prime()

# Display the updated state
print("\nState after moves:")
cube.display()

# Check if the cube is solved
if cube.is_complete():
    print("\nThe Rubik's Cube is solved!")
else:
    print("\nThe Rubik's Cube is not yet solved.")
