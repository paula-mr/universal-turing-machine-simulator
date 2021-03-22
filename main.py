# Autora: Paula Mara Ribeiro

INITIAL_SYMBOL = '1'
EMPTY_SYMBOL = '11'

DIR_RIGHT = '1'
DIR_LEFT = '11'

MAX_LOOPS = 1000
MAX_TAPE_SIZE = 1000

def main():
    mt_input = input('Insira a MT: ')
    result = process_mt(mt_input)
    print(result)


def process_mt(mt_input):
    tape_one, tape_two, tape_three = initialize_tapes(mt_input)

    cont = 0
    approved = False
    tape_two_head = 0
    while cont < MAX_LOOPS:
        current_symbol = get_corresponding_symbol(tape_two, tape_two_head)
        current_state = remove_initial_and_final_symbols(tape_three)
        transition_index = find_transition(tape_one, current_state, current_symbol)

        if current_symbol == EMPTY_SYMBOL or transition_index == -1:
            approved = is_final_state(tape_one, current_state)
            break
        else:
            new_state, new_symbol, direction = get_transition_info(tape_one, transition_index)
            tape_three = update_tape_three(new_state)
            tape_two = update_tape_two(tape_two, tape_two_head, new_symbol)
            tape_two_head = move_tape_two(tape_two_head, direction)
            if len(tape_two) >= MAX_TAPE_SIZE:
                return 'Rejeitada -> excedeu o tamanho da fita ' + str(cont) 
        cont += 1
    
    return 'Aprovada' if approved else 'Rejeitada -> entrou em loop' if cont == MAX_LOOPS else 'Rejeitada'


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


def get_corresponding_symbol(word, tape_two_head):
    word = remove_initial_and_final_symbols(word)
    symbols = word.split('0')
    if tape_two_head >= len(symbols):
        return EMPTY_SYMBOL
    return symbols[tape_two_head]


def remove_initial_and_final_symbols(tape):
    return tape[1:len(tape)-2]


def move_tape_two(symbol_count, direction):
    if direction == DIR_RIGHT:
        return symbol_count + 1
    else:
        return symbol_count - 1


def update_tape_three(new_state):
    return INITIAL_SYMBOL + new_state + EMPTY_SYMBOL


def update_tape_two(tape_two, tape_two_head, new_symbol):
    tape_two = remove_initial_and_final_symbols(tape_two)
    symbols = tape_two.split('0')
    symbols[tape_two_head] = new_symbol
    tape_two = '0'.join(symbols)
    return INITIAL_SYMBOL + tape_two + EMPTY_SYMBOL


if __name__ == "__main__":
    main()