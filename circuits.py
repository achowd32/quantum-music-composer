from qiskit import *
from qiskit.quantum_info import Statevector

import midi_conversion

class CircuitGrid:
    def __init__(self, num_qubits, num_gates):
        self.num_qubits = num_qubits
        self.num_gates = num_gates
        self.grid = [["" for i in range(num_qubits)] for j in range(num_gates)]
    
    def set_gate(self, xPos, yPos, gateVal):
        curGrid = self.grid
        curGrid[xPos][yPos] = gateVal

    def get_gate(self, xPos, yPos):
        return self.grid[xPos][yPos]
    
    def compile(self):
        QC = QuantumCircuit(self.num_qubits)
        for x in range(self.num_gates):
            for y in range(self.num_qubits):
                if self.get_gate(x, y) == "H":
                    QC.h(y)
                elif self.get_gate(x, y) == "X":
                    QC.x(y)
                elif self.get_gate(x, y) == "Z":
                    QC.z(y)
        quantum_state = Statevector(QC)
        return quantum_state

    def print_state(self):
        quantum_state = self.compile()
        for i, j in enumerate(quantum_state):
            prob = (j.real ** 2) + (j.imag ** 2)
            print("{0:09b}".format(i) + ":" + "{0:0.5f}".format(prob))

    def measure(self):
        quantum_state = self.compile()
        measurement_bitstring = quantum_state.sample_memory(1)[0]
        formatted_bitstring = str(measurement_bitstring)
        print(formatted_bitstring)
        return formatted_bitstring

    def output_chord(self):
        measured_state = self.measure()
        midi_conversion.final_output(measured_state)
