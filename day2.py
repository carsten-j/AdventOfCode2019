# https://github.com/Dementophobia/advent-of-code-2019
import utilities


def compute(program, verb=None, noun=None):

    program[1] = verb if verb != None else program[1]
    program[2] = noun if noun != None else program[2]

    for pointer in range(0, len(program), 4):

        instruction = program[pointer]
        if instruction == 99:
            return program
        parameter1 = program[program[pointer + 1]]
        parameter2 = program[program[pointer + 2]]
        idx = program[pointer + 3]

        program[idx] = (
            parameter1 + parameter2 if (instruction == 1) else parameter1 * parameter2
        )


@utilities.timer
def computer_v1(program, verb=None, noun=None):
    output = compute(program, verb=verb, noun=noun)
    return output[0]


@utilities.timer
def computer_v2(program):
    for verb in range(100):
        for noun in range(100):
            result = compute(program[:], verb=verb, noun=noun)
            if result[0] == 19690720:
                return 100 * verb + noun
