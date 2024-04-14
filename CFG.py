import random

class CFG:
    def __init__(self):
        self.rules = {}

    def add_rule(self, non_terminal, productions):
        if non_terminal not in self.rules:
            self.rules[non_terminal] = []
        self.rules[non_terminal].extend(productions)

    def generate(self, symbol):
        if symbol not in self.rules:
            return symbol  # terminal symbol
        else:
            expansion = random.choice(self.rules[symbol])
            result = ""
            for token in expansion:
                result += self.generate(token)
            return result

# Example usage:
grammar = CFG()
grammar.add_rule("S", [["NP", "VP"]])
grammar.add_rule("NP", [["Det", "N"], ["NP", "PP"]])
grammar.add_rule("PP", [["P", "NP"]])
grammar.add_rule("VP", [["V", "NP"], ["VP", "PP"]])
grammar.add_rule("Det", [["the"], ["a"]])
grammar.add_rule("N", [["cat"], ["dog"]])
grammar.add_rule("P", [["on"], ["under"]])
grammar.add_rule("V", [["chased"], ["ate"]])

print(grammar.generate("S"))

