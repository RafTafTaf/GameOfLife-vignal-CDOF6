# GameOfLife-vignal-CDOF6
creation of the game of life on python
## Description

**Game of Life** is a terminal-based Python implementation of John Conway's famous cellular automaton. This project simulates the evolution of cells on a grid, following simple rules of survival and reproduction. The initial grid is randomly generated, and the simulation runs indefinitely until the user stops it manually.

Key features:
- A randomly initialized grid with configurable density for live cells.
- A clean, dynamic terminal display.
- Simple rules of cell evolution:
  - A live cell with 2 or 3 neighbors survives.
  - A dead cell with exactly 3 neighbors becomes alive.
  - All other cells die or remain dead.

This project is a fun way to explore emergent patterns and chaos in a minimalistic terminal environment.

---

## How to Run the Project

### Prerequisites

- Python 3.6 or newer.
- A terminal or command prompt with basic Python support.

### Steps to Run

1. Clone or download the repository:
   ```bash
   git clone https://github.com/dianevrb/GameOfLife-vignal-CDOF6.git
   cd GameOfLife-vignal-CDOF6
   ```

2. Run the `main` Python script:
   ```bash
   python main.py
   ```

3. Watch the simulation evolve in your terminal.

4. To exit the simulation, press `Ctrl+C`. The program will terminate gracefully.

---

## How to Contribute

We welcome contributions to improve this project! Here’s how you can get involved:

### Reporting Issues

If you encounter bugs or have suggestions for new features, please open an issue on the [GitHub Issues page](https://github.com/dianevrb/GameOfLife-vignal-CDOF6/issues).

### Making Contributions

1. Fork the repository to your GitHub account:
   ```bash
   git fork https://github.com/dianevrb/GameOfLife-vignal-CDOF6.git
   ```

2. Clone your forked repository:
   ```bash
   git clone https://github.com/dianevrb/GameOfLife-vignal-CDOF6.git
   ```

3. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-or-bugfix-name
   ```

4. Make your changes in the code.

5. Commit and push your changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature-or-bugfix-name
   ```

6. Open a pull request (PR) to the original repository. Provide a clear description of your changes in the PR.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

If you have any questions, feel free to reach out or contribute via GitHub. Enjoy exploring the Game of Life! 😊
