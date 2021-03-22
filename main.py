import sys
import os

INITIAL_SYMBOL = '1'
EMPTY_SYMBOL = '11'

DIR_RIGHT = '1'
DIR_LEFT = '11'


def find_transition(tape_one, state, symbol):
    f_s = '00' + state + '0' + symbol + '0'
    index_transition = tape_one.find(f_s)
    return -1 if index_transition == -1 else index_transition + len(f_s)


def get_transition_info(tape_one, transition_index):
    transition = tape_one[transition_index:len(tape_one)]
    transition = transition.split('00')[0]
    new_state, new_symbol, direction = transition.split('0')
    return new_state, new_symbol, direction


def is_final_state(tape_one, state):
    final_states = tape_one[1:len(tape_one)].split('00')[0] # get final states
    final_states = final_states.split('0')
    return state in final_states


def get_corresponding_symbol(word, symbol_count):
    symbols = word.split('0')
    if symbol_count >= len(symbols):
        return EMPTY_SYMBOL
    return symbols[symbol_count]

def move_tape_two(symbol_count, direction):
    if direction == DIR_RIGHT:
        return symbol_count + 1
    else:
        return symbol_count - 1


ex1 = '1110010111011011101001011011101101001011110111011110100101111101110111110100110110111011010011011101110111010011011111011101111101000111011111'
ex2 = '111001011101101110100101101110110100101111011101111010010111110111011111010011011011101101001101110111011101001101111101110111110100011101111'
ex3 = '110010111011011101001011110110111101001101110101111011001101111010111011000111101111011101111'
ex4 = '110010111011011101001011110101111010011011101011110110011011110101110110001111011110111'

def main(argv):
    mt_input = ex3
    tape_one = INITIAL_SYMBOL + mt_input + EMPTY_SYMBOL
    _, word = mt_input.split('000')
    tape_two = INITIAL_SYMBOL + word + EMPTY_SYMBOL
    tape_three = INITIAL_SYMBOL + '1' + EMPTY_SYMBOL

    cont = True
    approved = False
    symbol_count = 0
    index_tape_two = 1
    while cont:
        r_a = get_corresponding_symbol(tape_two[1:len(tape_two)-2], symbol_count)
        r_e = tape_three[1:len(tape_three)-2]
        transition_index = find_transition(tape_one, r_e, r_a)
        if r_a == EMPTY_SYMBOL:
            cont = False
            approved = is_final_state(tape_one, r_e)
        elif transition_index == -1:
            cont = False
            approved = is_final_state(tape_one, r_e)
        else:
            new_state, new_symbol, direction = get_transition_info(tape_one, transition_index)
            tape_three = INITIAL_SYMBOL + new_state + EMPTY_SYMBOL
            index_tape_two += len(r_a)+1
            tape_two = tape_two[:index_tape_two] + new_symbol + tape_two[index_tape_two+len(r_a):]
            symbol_count = move_tape_two(symbol_count, direction)

    print('Aprovada' if approved else 'Rejeitada')


if __name__ == "__main__":
    main(sys.argv[1:])