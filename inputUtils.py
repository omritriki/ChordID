from chordFormulas import tuningOptions

def get_tuning_input():
    print("\nAvailable tunings:")
    for i, tuning in enumerate(tuningOptions.keys(), start=1):
        print(f"    {i}. {tuning}")

    while True:
        try:
            choice = int(input("Select a tuning by number: "))
            if 1 <= choice <= len(tuningOptions):
                return list(tuningOptions.values())[choice - 1]
            else:
                raise ValueError("Invalid choice")
        except ValueError:
            print("Invalid input. Please select a valid tuning number.")

def get_frets_input():
    while True:
        input_frets = input("Enter 6 fret numbers (use 'X' for muted strings): ").split()

        if len(input_frets) != 6:
            print("Please enter exactly 6 fret numbers.")
            continue

        try:
            frets = [
                'X' if fret.upper() == 'X' else int(fret)
                for fret in input_frets
            ]
            if any(fret != 'X' and (fret < 0 or fret > 20) for fret in frets):
                raise ValueError("Fret numbers must be between 0 and 20.")
            return frets
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")