### using mingus and midiutil packages

from midiutil import MIDIFile
from mingus.core import chords

TREBLE_NOTES = [64, 65, 67, 69, 71, 72, 74, 76, 77] # e4, f4, g4, a4, b4, c5, d5, e5, f5

def index_to_note(i):
    note = 0
    note = TREBLE_NOTES[i]
    return note

def state_to_notes(state):
    # assuming state is given as string of numbers
    # returns it as midi-base note
    notes = [0,0,0,0,0,0,0,0,0]
    state_list = list(str(state))
    print(state_list)
    for i in range(0,len(state_list)):
        if state_list[i] == "1":
            notes[i] = index_to_note(i)
        elif state_list[i] == "0":
            notes[i] = 0
    print(notes)
    return notes

# imagine a quantum circuit's classical output is represented by string of 0,1
#ex_output = "001001001" should give g, c, f

def final_output(q_state):
    track = 0
    channel = 0
    time = 0 # in beats
    duration = 4 # in beats
    tempo = 120 # in bpm
    volume = 100 # 0-127, as per midi standard

    MyMIDI = MIDIFile(1) # one track, defaults to format 1 (tempo track created automatically)
    MyMIDI.addTempo(track, time, tempo)

    for i, pitch in enumerate(state_to_notes(q_state)):
        if pitch != 0:
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)

    with open("ex_out_1.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)