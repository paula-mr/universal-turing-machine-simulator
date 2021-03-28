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
    tape_two_head = 1
    while cont < MAX_LOOPS:
        current_symbol = get_corresponding_symbol(tape_two, tape_two_head)
        current_state = tape_three
        transition_found, new_state, new_symbol, direction = find_transition(tape_one, current_state, current_symbol)

        if not transition_found:
            approved = is_final_state(tape_one, current_state)
            break
        else:
            tape_three = update_tape_three(new_state)
            tape_two = update_tape_two(tape_two, tape_two_head, new_symbol)
            tape_two_head = move_tape_two(tape_two_head, direction)

            if len(tape_two) >= MAX_TAPE_SIZE:
                return 'Rejeitada -> excedeu o tamanho da fita ' + str(cont) 
        cont += 1
    
    return 'Aprovada' if approved else 'Rejeitada -> entrou em loop' if cont == MAX_LOOPS else 'Rejeitada'


def initialize_tapes(mt_input):
    tape_one = INITIAL_SYMBOL + '0' + mt_input + '0' + EMPTY_SYMBOL
    _, word = mt_input.split('000')
    tape_two = INITIAL_SYMBOL + '0' + word + '0' + EMPTY_SYMBOL
    tape_three = '1'

    return tape_one, tape_two, tape_three


def find_transition(tape_one, state, symbol):
    start_transition = tape_one.find('00')
    end_transition = tape_one.find('000')

    transitions = tape_one[start_transition:end_transition]

    f_s = '00' + state + '0' + symbol + '0'
    index_transition = transitions.find(f_s)
    
    if index_transition == -1:
        return False, 0, 0, 0
    else:
        index_transition += len(f_s)
        transition = transitions[index_transition:end_transition]
        transition = transition.split('00')[0]
        new_state, new_symbol, direction = transition.split('0')
    return True, new_state, new_symbol, direction


def is_final_state(tape_one, state):
    final_states = tape_one[1:len(tape_one)].split('00')[0] # get final states
    final_states = final_states.split('0')
    return state in final_states


def get_corresponding_symbol(word, tape_two_head):
    symbols = word.split('0')
    if tape_two_head >= len(symbols):
        return EMPTY_SYMBOL
    return symbols[tape_two_head]


def move_tape_two(symbol_count, direction):
    if direction == DIR_RIGHT:
        return symbol_count + 1
    else:
        return symbol_count - 1


def update_tape_three(new_state):
    return new_state


def update_tape_two(tape_two, tape_two_head, new_symbol):
    symbols = tape_two.split('0')
    symbols[tape_two_head] = new_symbol
    tape_two = '0'.join(symbols)
    return tape_two


if __name__ == "__main__":
    main()