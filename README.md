# ChordID

ChordID is a Python-based tool designed to help guitar enthusiasts learn and identify chords. Whether you're a beginner trying to understand chord structures or an advanced player exploring alternate tunings, ChordID provides an interactive way to identify chords based on fretboard input.

**Note:** This project is a work in progress (WIP). Features and functionality are being actively developed and improved.

## Features

- **Interactive GUI**: Identify chords using a graphical interface with the help of `tkinter`.
- **Command-Line Mode**: Use the terminal to input fret positions and get chord information.
- **Support for Alternate Tunings**: Choose from popular tunings like Standard, Drop D, DADGAD, Open G, and more.
- **Detailed Chord Analysis**: Displays the root note, chord type, and notes played on each string.
- **Customizable**: Easily extend the chord formulas and tuning options.

## How It Works

1. **Input Frets**: Enter the fret positions for each string (use `X` for muted strings).
2. **Select Tuning**: Choose a tuning from the available options.
3. **Identify Chord**: The tool calculates the notes and identifies the chord type based on predefined formulas.
4. **Learn and Explore**: Use the output to understand chord structures and experiment with different tunings.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- `tkinter` library (comes pre-installed with most Python distributions)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ChordID.git
   cd ChordID
   ```

2. Run the GUI application:
   ```bash
   python GUI.py
   ```

3. Alternatively, run the command-line version:
   ```bash
   python main.py
   ```

## Usage

### GUI Mode

1. Launch the GUI by running `GUI.py`.
2. Select a tuning from the dropdown menu.
3. Enter fret positions for each string (use `X` for muted strings).
4. Click "Identify Chord" to see the chord name and notes.
5. Use the "Reset" button to clear inputs or "Quit" to exit the application.

### Command-Line Mode

1. Run `main.py` in your terminal.
2. Follow the prompts to select a tuning and input fret positions.
3. View the identified chord and notes in the terminal.
4. Enter new frets or quit the program.

## Example

### Input:
- Tuning: Standard (EADGBE)
- Frets: `3 2 0 0 0 3` (G Major chord)

### Output:
- Chord: G Major
- Notes: G, B, D, G, B, G

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.


Happy playing! 🎸