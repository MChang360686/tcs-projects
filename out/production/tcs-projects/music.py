from mingus.core import notes, chords, scales
from mingus.containers import Note
from midiutil import MIDIFile
import random

bpm = 92
midi = MIDIFile(1)
midi.addTempo(0, 0, bpm)
midi.addProgramChange(0, 0, 0, 0)       # Piano (optional)

time = 0

# Arpeggio over C major chords
chord_names = ["Cmaj7", "Am7", "Fmaj7", "G7"]
durations   = [4, 4, 4, 4]

for chord_name, chord_dur in zip(chord_names, durations):
    chord = chords.from_shorthand(chord_name)           # e.g. ['C','E','G','B']
    
    # Play broken chord (arpeggio up → down)
    pattern = chord + chord[::-1][1:]                   # C E G B → G E C
    random.shuffle(pattern)                             # add some variation
    
    for i, note_name in enumerate(pattern * 2):         # repeat pattern twice
        n = Note(note_name, octave=4 + (i // 6))        # slowly go up octave
        pitch = n.to_midi_note()
        
        vel = 100 if i % 2 == 0 else 80                 # slight dynamic
        
        midi.addNote(0, 0, pitch, time, 0.5, vel)
        time += 0.5

with open("arpeggio_example.mid", "wb") as f:
    midi.writeFile(f)

print("Created arpeggio_example.mid")