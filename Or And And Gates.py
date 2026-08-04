import random

def logic_gate_simulation():
    A = random.randint(0, 1)
    B = random.randint(0, 1)

    and_result = A and B
    or_result = A or B

    print("Input A:", A)
    print("Input B:", B)
    print("AND Gate Output:", and_result)
    print("OR Gate Output:", or_result)

logic_gate_simulation()
