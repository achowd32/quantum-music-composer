# QHarmony
Version 0.0.2

## Description
QHarmony is an interactive game that merges quantum computing with music composition. Players create quantum circuits, where each gate corresponds to a note on the treble clef.
Upon measurement, the measured state is represented as its corresponding chord, which is output in an mp3 file!

## Installation and Controls
As of now, you can play QHarmony by cloning or downloading this repository, and calling the ```main.py``` file from your command line.
Ensure you have the following libraries installed:```qiskit```, ```pygame```, ```midiutil```, ```mingus```.
<br/> <br/>
Move around on the circuit using WASD. Press X to place an X-gate, Z to place a Z-gate, and H to place a Hadamard gate.
Press 1 to print (to the terminal) a representation of the circuit's current quantum state, formatted as (measurement: probability).
Press 2 to print (to the terminal) a measurement of the circuit.
Press 3 to output (to your directory) an mp3 file corresponding to a measured state of the circuit.

## To-Dos and Planned Features
- Output the notes printed on the treble clef in another mp3
- Output measurements within the Pygame window
- Play mp3 within Pygame instead of outputting to directory
- Improve GUI for treble clef
- Main menu and tutorial
- Package as an executable
