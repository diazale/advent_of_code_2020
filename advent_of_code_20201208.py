"""
Three operations:
acc: increases global "accumulator" value and executes instruction below
jmp: jumps to new instruction relative to itself
nop: does nothing and moves to instruction below
"""

f = open("input_20201208.txt", "r")
instructions = [line.strip("\n") for line in f.readlines() if line.strip()]
f.close()

# Part 1: What is the value of the accumulator immediately before any instruction is executed twice?
# Track visited and current indices and see if there are any shared values?
visited_indices = []

def parse_instruction(instruction_):
    return instruction_.split()[0], int(instruction_.split()[1].strip(" +"))

def navigate_instructions(instructions_, position_, acc):
    try:
        if not position_ in visited_indices:
            visited_indices.append(position_)
            # Figure out what to do
            parse_instruction(instructions_[position_])
            instruction, increment = parse_instruction(instructions_[position_])

            if instruction[0]=="acc":
                # Increase accumulator and move to next line
                acc+=instruction[1]
                #print("ACC:", acc)
                navigate_instructions(instructions_, position_ + 1, acc)
            elif instruction[0]=="jmp":
                # Jump ahead by the value
                navigate_instructions(instructions_, position_ + increment, acc)
            elif instruction[0]=="nop":
                navigate_instructions(instructions_, position_+ 1, acc)
        else:
            print("final acc", acc)
    except:
        # lazy solution, but if we hit an index error this brings up the final acc
        print("********final acc", acc)

navigate_instructions(instructions, 0, 0)

# Part 2: Switch jmp/nop pairs so that the list never enters an infinite loop
# Strategy: Create a copy of the list
# Then change each one and see the acc when we run out of instructions
for i in range(0, len(instructions)):
    new_instructions = instructions.copy()
    visited_indices = []

    if parse_instruction(instructions[i])[0]=="jmp":
        new_instructions[i] = new_instructions[i].replace("jmp","nop")
        navigate_instructions(new_instructions, 0, 0)
    elif parse_instruction(instructions[i])[0]=="nop":
        new_instructions[i] = new_instructions[i].replace("nop", "jmp")
        navigate_instructions(new_instructions, 0, 0)