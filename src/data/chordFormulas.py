# ===================================================================================================
#                                       ChordID - Chord Formulas
#                                            Omri Triki
#                                       Guitar Learning Tool
#                                               2025
# ===================================================================================================
# Description:
#   This module contains the chord formulas and tuning options used in the ChordID project. It defines
#   the intervals for various chord types and provides a dictionary of common guitar tunings.
# Inputs:
#   - None (used as a static data module).
# Outputs:
#   - `chordFormulas`: A dictionary mapping intervals to chord names.
#   - `tuningOptions`: A dictionary of common guitar tunings and their intervals.
# ===================================================================================================


chordFormulas = {
        (0, 4, 7): 'Major',
        (0, 3, 7): 'Minor',
        (0, 4, 7, 11): 'Major 7',
        (0, 3, 7, 10): 'Minor 7',
        (0, 4, 7, 10): 'Dominant 7',
        (0, 3, 6): 'Diminished',
        (0, 3, 6, 9): 'Diminished 7',
        (0, 3, 6, 10): 'Half-Diminished (m7♭5)',
        (0, 4, 8): 'Augmented',
        (0, 4, 7, 2): 'Add9',  # 9th -> 2
        (0, 3, 7, 2): 'Minor Add9',  # 9th -> 2
        (0, 4, 7, 5): 'Add11',  # 11th -> 5
        (0, 2, 7): 'Sus2',
        (0, 5, 7): 'Sus4',
        (0, 7): 'Power',
        (0, 5, 7, 10): '7sus4',

        # Extended chords (mod 12 applied)
        (0, 4, 7, 10, 2): 'Dominant 9',  # 9th -> 2
        (0, 4, 7, 11, 2): 'Major 9',  # 9th -> 2
        (0, 3, 7, 10, 2): 'Minor 9',  # 9th -> 2
        (0, 4, 7, 10, 2, 5): 'Dominant 11',  # 9th -> 2, 11th -> 5
        (0, 4, 7, 11, 2, 5): 'Major 11',  # 9th -> 2, 11th -> 5
        (0, 3, 7, 10, 2, 5): 'Minor 11',  # 9th -> 2, 11th -> 5
        (0, 4, 7, 10, 2, 9): 'Dominant 13',  # 9th -> 2, 13th -> 9
        (0, 4, 7, 11, 2, 9): 'Major 13',  # 9th -> 2, 13th -> 9
        (0, 3, 7, 10, 2, 9): 'Minor 13',  # 9th -> 2, 13th -> 9

        # Altered chords (mod 12 applied)
        (0, 4, 8, 10): 'Augmented 7 (7#5)',
        (0, 4, 7, 10, 1): '7♭9',  # ♭9 -> 13 mod 12 = 1
        (0, 4, 7, 10, 3): '7#9',  # 9 -> 15 mod 12 = 3
        (0, 4, 7, 10, 8): '7♭13',  # ♭13 -> 20 mod 12 = 8
        (0, 4, 7, 10, 6): '7♯11',  # ♯11 -> 18 mod 12 = 6
        (0, 4, 7, 10, 1, 6): '7♭9♯11',
        (0, 4, 7, 10, 1, 8): '7♭9♭13',
        (0, 4, 7, 10, 3, 8): '7#9♭13',

        # Suspended chords
        (0, 5, 7, 2): 'Sus4 Add9',
        (0, 2, 7, 5): 'Sus2 Add4',

        # Quartal chords
        (0, 5, 10): 'Quartal Triad',
        (0, 5, 10, 3): 'Quartal 7',

        # Other variations
        (0, 3, 6, 9, 2): 'Diminished 9',
        (0, 4, 8, 11): 'Augmented Major 7',
        (0, 3, 6, 10, 2): 'Half-Diminished 9',
        (0, 4, 7, 11, 6): 'Major 7♯11',
        (0, 4, 7, 11, 8): 'Major 7♭13',
        (0, 3, 7, 10, 6): 'Minor 7♯11',
        (0, 3, 7, 10, 8): 'Minor 7♭13',
        (0, 4, 7, 10, 2, 6): 'Dominant 9♯11',
        (0, 4, 7, 10, 2, 8): 'Dominant 9♭13',
        (0, 4, 7, 10, 2, 5, 9): 'Dominant 13♯11',
        (0, 4, 7, 10, 2, 5, 8): 'Dominant 13♭13',

        # Slash Chords (Common Variations)
        (0, 4, 7, 11): 'Major/Root',  # C/C
        (1, 4, 7): 'Major/♭2',        # C/D♭
        (2, 4, 7): 'Major/2',         # C/D
        (3, 4, 7): 'Major/♭3',        # C/E♭
        (4, 4, 7): 'Major/3',         # C/E
        (5, 4, 7): 'Major/4',         # C/F
        (6, 4, 7): 'Major/♭5',        # C/G♭
        (7, 4, 7): 'Major/5',         # C/G
        (8, 4, 7): 'Major/♭6',        # C/A♭
        (9, 4, 7): 'Major/6',         # C/A
        (10, 4, 7): 'Major/♭7',       # C/B♭
        (11, 4, 7): 'Major/7',        # C/B

        # Common Minor Slash Chords
        (0, 3, 7): 'Minor/Root',      # Cm/C
        (2, 3, 7): 'Minor/2',         # Cm/D
        (3, 3, 7): 'Minor/♭3',        # Cm/E♭
        (7, 3, 7): 'Minor/5',         # Cm/G
        (8, 3, 7): 'Minor/♭6',        # Cm/A♭
        (10, 3, 7): 'Minor/♭7',       # Cm/B♭

        # Common Seventh Slash Chords
        (5, 4, 7, 10): 'Dominant7/4',  # C7/F
        (7, 4, 7, 10): 'Dominant7/5',  # C7/G
        (2, 4, 7, 11): 'Major7/2',     # CMaj7/D
        (7, 4, 7, 11): 'Major7/5',     # CMaj7/G
        (2, 3, 7, 10): 'Minor7/2',     # Cm7/D
        (7, 3, 7, 10): 'Minor7/5',     # Cm7/G

        # Popular Slash Chord Progressions
        (4, 7, 11, 2): 'Major7/3',     # CMaj7/E
        (5, 9, 0, 4): 'Major/4',       # C/F
        (7, 11, 2, 5): 'Major/5',      # C/G
        (9, 0, 4, 7): 'Major/6',       # C/A
    }

# Tuning options
tuningOptions = {
    "Standard": (0, 5, 10, 15, 19, 24),  # E A D G B E
    "Drop D": (-2, 5, 10, 15, 19, 24),  # D A D G B E
    "DADGAD": (-2, 5, 10, 15, 17, 22),  # D A D G A D
    "Open G": (-2, 5, 10, 14, 17, 22),  # D G D G B D
    "Open D": (-2, 2, 7, 11, 14, 19),   # D A D F# A D
    "Open C": (-4, 0, 7, 12, 16, 19),   # C G C G C E
    "Half Step Down": (-1, 4, 9, 14, 18, 23),  # Eb Ab Db Gb Bb Eb
    "Full Step Down": (-2, 3, 8, 13, 17, 22)   # D G C F A D
}