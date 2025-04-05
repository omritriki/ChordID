from enum import Enum
from src.data.chordFormulas import chordFormulas  # Adjusted import path

class Root(Enum):
    E = 0
    F = 1
    Fsharp = 2
    G = 3
    Gsharp = 4
    A = 5
    Asharp = 6
    B = 7
    C = 8
    Csharp = 9
    D = 10
    Dsharp = 11

def findRoot(fret_value):
    return Root(fret_value % 12).name

def findNotes(frets, tuning_intervals):
    return [
        findRoot(tuning_intervals[i] + fret) if fret != 'X' else 'X'
        for i, fret in enumerate(frets)
    ]

def findFirstNonMuted(notes):
    for note in notes:
        if note != 'X':
            return note
    return "No root found"

def get_intervals(notes):
    # Remove muted strings and duplicates while preserving order
    filtered_notes = list(dict.fromkeys(note for note in notes if note != 'X'))
    
    if not filtered_notes:
        return []  # Return an empty list if no valid notes are found

    # Calculate intervals relative to the root note
    root_value = Root[filtered_notes[0]].value
    intervals = [(Root[note].value - root_value) % 12 for note in filtered_notes]
    return sorted(intervals)

def findChordType(notes):
    chord_intervals = get_intervals(notes)
    if not chord_intervals:
        return "Unknown"  # No valid intervals found

    # Find the root note (first non-muted note)
    root_note = notes[0] if notes[0] != 'X' else findFirstNonMuted(notes)

    # Get the chord name from the chordFormulas dictionary
    chord_name = chordFormulas.get(tuple(chord_intervals), 'Unknown')

    # Prepend the root note to the chord name
    if chord_name != 'Unknown':
        chord_name = f"{root_note} {chord_name}"

    # Detect slash chords only if the bass note is different from the root
    if notes[0] != root_note and notes[0] != 'X':
        chord_name += f" / {notes[0]}"

    return chord_name