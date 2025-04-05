# ===================================================================================================
#                                             ChordID
#                                            Omri Triki
#                                       Guitar Learning Tool
#                                               2025
# ===================================================================================================
# Description:
#   This script serves as the main entry point for the ChordID project. It allows users to input
#   fret positions and select a tuning to identify guitar chords. The tool calculates the root note,
#   chord type, and notes played on each string.
# Inputs:
#   - User input for tuning selection.
#   - User input for fret positions (6 strings, with 'X' for muted strings).
# Outputs:
#   - The identified chord name (e.g., "E Minor").
#   - The notes played on each string.
# ===================================================================================================


from utils.inputUtils import get_tuning_input, get_frets_input
from utils.chordUtils import findNotes, findChordType

def main():
    # Get tuning input with validation
    tuning = get_tuning_input()

    while True:
        # Get frets input with validation
        frets = get_frets_input()

        # Find notes (with duplicates, maintaining string order)
        notes_with_duplicates = findNotes(frets, tuning)

        # Find and display the root note and chord type
        print(notes_with_duplicates)
        chord_type = findChordType(notes_with_duplicates)

        print("\nChord: " + chord_type)
        print("Notes (by string): " + ", ".join(notes_with_duplicates))

        # Ask if the user wants to continue
        choice = input("\nEnter 'q' to quit or press Enter to enter new frets: ").strip().lower()
        if choice == 'q':
            break

if __name__ == '__main__':
    main()