class CNICDFA:
    def __init__(self):
        # Define the states of the DFA
        # Dear students you have to add fail state in code to complete this task
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4','q4-' ,'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11','q11-', 'q12','q13'}

        # Define the alphabet (input symbols)
        self.alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-'}

        # Define the transitions of the DFA as a dictionary of dictionaries
        self.transitions = {
            'q0': {'0': 'q1', '1': 'q1', '2': 'q1', '3': 'q1', '4': 'q1', '5': 'q1', '6': 'q1', '7': 'q1', '8': 'q1', '9': 'q1'},
            'q1': {'0': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2'},
            'q2': {'0': 'q3', '1': 'q3', '2': 'q3', '3': 'q3', '4': 'q3', '5': 'q3', '6': 'q3', '7': 'q3', '8': 'q3', '9': 'q3'},
            'q3': {'0': 'q4', '1': 'q4', '2': 'q4', '3': 'q4', '4': 'q4', '5': 'q4', '6': 'q4', '7': 'q4', '8': 'q4', '9': 'q4'},
            'q4': {'0': 'q4-', '1': 'q4-', '2': 'q4-', '3': 'q4-', '4': 'q4-', '5': 'q4-', '6': 'q4-', '7': 'q4-', '8': 'q4-',
                   '9': 'q4-'},
            'q4-': {'-': 'q5'},
            'q5': {'0': 'q6', '1': 'q6', '2': 'q6', '3': 'q6', '4': 'q6', '5': 'q6', '6': 'q6', '7': 'q6', '8': 'q6', '9': 'q6'},
            'q6': {'0': 'q7', '1': 'q7', '2': 'q7', '3': 'q7', '4': 'q7', '5': 'q7', '6': 'q7', '7': 'q7', '8': 'q7', '9': 'q7'},
            'q7': {'0': 'q8', '1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
            'q8': {'0': 'q9', '1': 'q9', '2': 'q9', '3': 'q9', '4': 'q9', '5': 'q9', '6': 'q9', '7': 'q9', '8': 'q9', '9': 'q9'},
            'q9': {'0': 'q10', '1': 'q10', '2': 'q10', '3': 'q10', '4': 'q10', '5': 'q10', '6': 'q10', '7': 'q10', '8': 'q10', '9': 'q10'},
            'q10': {'0': 'q11', '1': 'q11', '2': 'q11', '3': 'q11', '4': 'q11', '5': 'q11', '6': 'q11', '7': 'q11',
                   '8': 'q11', '9': 'q11'},
            'q11': {'0': 'q11-', '1': 'q11-', '2': 'q11-', '3': 'q11-', '4': 'q11-', '5': 'q11-', '6': 'q11-', '7': 'q11-',
                    '8': 'q11-', '9': 'q11-'},
            'q11-': {'-': 'q12'},
            'q12': {'1': 'q13', '0': 'q13', '2': 'q13', '3': 'q13', '4': 'q13', '5': 'q13', '6': 'q13', '7': 'q13', '8': 'q13', '9': 'q13'},
            'q13': {'0': 'q13', '1': 'q13', '2': 'q13', '3': 'q13', '4': 'q13', '5': 'q13', '6': 'q13', '7': 'q13', '8': 'q13', '9': 'q13'}
        }

        # Define the initial state
        self.initial_state = 'q0'

        # Define the accepting states
        self.accepting_states = {'q13'}

    def is_valid_cnic(self, cnic):
        current_state = self.initial_state

        # Iterate over the characters in the input CNIC
        for char in cnic:
            # Check if the character is in the alphabet
            if char not in self.alphabet:
                return False

            # Transition to the next state based on the current state and input character
            current_state = self.transitions.get(current_state, {}).get(char)
            if current_state is None:
                return False

        # Check if the final state is an accepting state
        return current_state in self.accepting_states

# Example usage:
cnic_dfa = CNICDFA()

print(cnic_dfa.is_valid_cnic("97014-3233412-556"))  #Add fail state to control it Output: True
print(cnic_dfa.is_valid_cnic("A7104-3234212-6"))  # Output: False (Invalid first digit)
print(cnic_dfa.is_valid_cnic("37104-3234212-5"))  # Output: False (Invalid check digit)
print(cnic_dfa.is_valid_cnic("37104-32A4212-6"))  # Output: False (Invalid character)
print(cnic_dfa.is_valid_cnic("37104-3234212"))    # Output: False (Incomplete CNIC)
