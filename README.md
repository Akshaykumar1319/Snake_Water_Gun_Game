# Snake_Water_Gun_Game
# Snake-Water-Gun Game

## Introduction
This is a simple Python-based command-line game that simulates the classic "Snake-Water-Gun" game. The game randomly selects a choice for the computer, and the user inputs their choice. The game then determines the winner based on predefined rules.

## Rules
- `Snake (1)` beats `Water (-1)`
- `Water (-1)` beats `Gun (0)`
- `Gun (0)` beats `Snake (1)`
- If both the user and the computer choose the same, the game results in a draw.

## How to Play
1. Run the Python script in a terminal or command prompt.
2. Enter your choice when prompted:
   - `s` for Snake
   - `w` for Water
   - `g` for Gun
3. The computer randomly selects a choice.
4. The game displays the computer's choice and the user's choice.
5. The winner is determined based on the rules.

## Installation & Execution
1. Ensure you have Python installed (Python 3 recommended).
2. Save the script as `snake_water_gun.py`.
3. Open a terminal or command prompt and navigate to the script's location.
4. Run the script using the command:
   ```sh
   python snake_water_gun.py
   ```

## Code Explanation
- The script uses Python's `random.choice()` to select a random choice for the computer.
- A dictionary `myDict` maps user inputs (`s`, `w`, `g`) to numerical values.
- Another dictionary `reverseDict` maps numerical values back to their respective names.
- The script compares the user's choice and the computer's choice using conditional statements to determine the winner.
- The result is printed accordingly.

## Example Output
```
Enter Your choice : s
Computer choice Gun
Your choice Snake
You loose!
```

## Future Enhancements
- Add graphical UI for better user experience.
- Implement multiple rounds with score tracking.
- Allow user to play against another human player.

## Author
- Developed by [N.Akshay Kumar]

## License
This project is open-source and free to use.

