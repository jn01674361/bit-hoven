import pickle
import numpy
import glob
from music21 import instrument, note, stream, chord, converter
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Activation


for track in glob.glob("midi_songs/*.mid"):
    midi_track = converter.parse(track)
to_be_parsed = 0
notes=[]
different_instruments = instrument.partitionByInstrument(midi_track)

if different_instruments:
    to_be_parsed = different_instruments.parts[0].recurse()
else:
    to_be_parsed = midi_track.flat.notes

for el in to_be_parsed:
    if isinstance(el, note.Note):
        notes.append(str(el.pitch))
    elif isinstance(el,chord.Chord):
        notes.append('.'.join(str(a_note) for a_note in el.normalOrder))
         

        
pitchnames = sorted(set(item for item in notes)) #GÖR OM TILL KLASSISK FOR-LOOP
note_to_int = dict((note, number) for number, note in enumerate(pitchnames))


thefile = open('uniqe_notes_readysong.txt', 'w')
for item in pitchnames:
    thefile.write("%s\n" % item)

sequence_length = 50
network_input = []
output = []

for i in notes:
    network_input.append(note_to_int[i])

    thefile = open('intnoted_notes_readysong.txt', 'w')
    for item in network_input:
        thefile.write("%s\n" % item)

a=numpy.bincount(network_input)
thefile = open('occ_note_readysong.txt', 'w')
for item in a:
    thefile.write("%s\n" % item)  
        
                        

 
