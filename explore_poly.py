# author : alexis louis
# desc : displays combinatorial of superimposed triads for various st offsets

import numpy as np
import pandas as pd

intervals = np.array(['1', 'm2', 'M2', 'm3', 'M3', '4', 'T', '5', 'm6', 'M6', 'm7', 'M7'])
values = np.arange(len(intervals))
formulas = {'major' : [0,4,7], 'minor' : [0,3,7], 'augmented' : [0,4,8], 'diminished' : [0,3,6]}

indexes = []
chords = []
chords_names = []
for first_chord in ['major', 'minor']:
    for second_chord in ['major', 'minor']:
        for semitones_up in np.arange(1,12):
            poly_chord_val = np.unique(np.concatenate(
                [np.take(values, formulas[first_chord]), 
                 np.take(np.roll(values, -semitones_up), formulas[second_chord])]))
            poly_chord = np.take(intervals, poly_chord_val)
            chords.append(poly_chord)
            chords_names.append(chord.Chord(poly_chord_val.tolist()).commonName)
            indexes.append((first_chord, second_chord, semitones_up))
            
inter_pres = {}
inter_pres['chords_names'] = chords_names
for i in intervals:
    inter_pres[str(i)] = [bool(np.isin(i, c)) for c in chords]
    
index = pd.MultiIndex.from_tuples(indexes, names=['first chord', 'second chord', 'position in st'])
chord_map = pd.DataFrame(inter_pres, index=index, columns = intervals.tolist() + ['chords_names'])

print(chord_map)
