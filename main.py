# Autora: Paula Mara Ribeiro

INITIAL_SYMBOL = '1'
EMPTY_SYMBOL = '11'

DIR_RIGHT = '1'
DIR_LEFT = '11'


def main():
    mt_input = input('Insira a MT: ')
    result = process_mt(mt_input)
    print(result)


def process_mt(mt_input):
    tape_one, tape_two, tape_three = initialize_tapes(mt_input)

    cont = 0
    finished = False
    approved = False
    tape_two_head = 0
    index_tape_two = 1
    while cont < 1000 and not finished:
        r_a = get_corresponding_symbol(tape_two, tape_two_head)
        r_e = remove_initial_and_final_symbols(tape_three)
        transition_index = find_transition(tape_one, r_e, r_a)
        if r_a == EMPTY_SYMBOL or transition_index == -1:
            finished = True
            approved = is_final_state(tape_one, r_e)
        else:
            new_state, new_symbol, direction = get_transition_info(tape_one, transition_index)
            tape_three = INITIAL_SYMBOL + new_state + EMPTY_SYMBOL
            index_tape_two, tape_two = update_tape_two(r_a, tape_two, index_tape_two, new_symbol)
            tape_two_head = move_tape_two(tape_two_head, direction)
        cont += 1

    return 'Aprovada' if approved else 'Rejeitada -> entrou em loop' if cont == 1000 else 'Rejeitada'


def initialize_tapes(mt_input):
    tape_one = INITIAL_SYMBOL + mt_input + EMPTY_SYMBOL
    _, word = mt_input.split('000')
    tape_two = INITIAL_SYMBOL + word + EMPTY_SYMBOL
    tape_three = INITIAL_SYMBOL + '1' + EMPTY_SYMBOL

    return tape_one, tape_two, tape_three


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
    word = remove_initial_and_final_symbols(word)
    symbols = word.split('0')
    if symbol_count >= len(symbols):
        return EMPTY_SYMBOL
    return symbols[symbol_count]


def remove_initial_and_final_symbols(tape):
    return tape[1:len(tape)-2]


def move_tape_two(symbol_count, direction):
    if direction == DIR_RIGHT:
        return symbol_count + 1
    else:
        return symbol_count - 1


def update_tape_two(r_a, tape_two, index_tape_two, new_symbol):
    index_tape_two += len(r_a)+1
    tape_two = tape_two[:index_tape_two] + new_symbol + tape_two[index_tape_two+len(r_a):]
    return index_tape_two, tape_two


if __name__ == "__main__":
    main()