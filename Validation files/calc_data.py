import pickle
import numpy
import glob
from music21 import instrument, note, stream, chord, converter
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Activation

def generate():  
    with open('data/notes', 'rb') as filepath:
        notes = pickle.load(filepath)
    pitchnames = sorted(set(item for item in notes))
    n_vocab = len(set(notes))
    thefile = open('uniqe_notes.txt', 'w')
    for item in pitchnames:
         thefile.write("%s\n" % item)
    print(len(notes))

    prepare_sequences(notes, pitchnames, n_vocab, True)
    #model = create_network(normalized_input, n_vocab)
    #prediction_output = generate_notes(model, network_input, pitchnames, n_vocab)
    #create_midi(prediction_output)


def prepare_sequences(notes, pitchnames, n_vocab, whattodo):
    """ Prepare the sequences used by the Neural Network """
    # map between notes and integers and back
    

    if whattodo:
        note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

        sequence_length = 50
        network_input = []
        output = []

        for i in notes:
            network_input.append(note_to_int[i])

        thefile = open('intnoted_notes.txt', 'w')
        for item in network_input:
             thefile.write("%s\n" % item)

        a=numpy.bincount(network_input)
        thefile = open('occ_note.txt', 'w')
        for item in a:
             thefile.write("%s\n" % item)    
    else:
        prepare_song(note_to_int)



    return ()





            



generate()