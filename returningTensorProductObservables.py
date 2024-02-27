import pennylane as qml
import pennylane.numpy as np

dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev)
def simple_circuit(angle):

    """
    In this function:
        * Prepare the Bell state |Phi+>.
        * Rotate the first qubit around the y-axis by angle
        * Measure the tensor product observable Z0xZ1.

    Args:
        angle (float): how much to rotate a state around the y-axis.

    Returns:
        Union[tensor, float]: the expectation value of the Z0xZ1 observable.
    """

    # Bell state
    qml.Hadamard(0)
    qml.CNOT([0, 1])

    qml.RY(angle, 0)

    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1))
