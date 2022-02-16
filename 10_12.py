
class Chunks:
    def __init__(self):
        file = '10.txt'
        lines = [line.strip() for line in open(file, 'r')]
        self.pairs = { '(':')', '[':']', '<':'>', '{':'}'}
        self.point_dict_corrupted = {')':3, ']':57, '}':1197, '>':25137}
        self.point_dict_incomplete = {')':1, ']':2, '}':3, '>':4}
        self.corrupted = []
        self.incomplete = []
        self.calculate(lines, 'corrupted')
        self.calculate(lines, 'incomplete')

    def check_for_incomplete(self, line):
        stack = []
        inc = []
        for sign in line:
            if sign in self.pairs.keys():
                stack.append(sign)
            else:
                popped = stack.pop()
                if sign == self.pairs[popped]:
                    continue
                return
        for sign in stack[::-1]:
            inc.append(self.pairs[sign])
        self.incomplete.append(inc)

    def line_score(self, line):
        score = 0
        for sign in line:
            score = score * 5 + self.point_dict_incomplete[sign]
        return score

    def check_for_corrupted(self, line):
        stack = []
        for sign in line:
            if sign in self.pairs.keys():
                stack.append(sign)
            else:
                popped = stack.pop()
                if sign == self.pairs[popped]:
                    continue
                self.corrupted.append(sign)
    
    def score_corrupted(self):
        points = 0
        for sign in self.corrupted:
            points += self.point_dict_corrupted[sign]
        print('Solution for first part: ', points)

    def score_incomplete(self):
        scores = []
        for line in self.incomplete:
            scores.append(self.line_score(line))
        scores.sort()
        points = scores[int((len(scores)-1)/2)]
        print('Solution for sec part: ', points)

     
    def calculate(self, lines, func):
        calc = getattr(self, 'check_for_'+func)
        for line in lines:
            calc(line)
        get_score = getattr(self, 'score_'+func)
        get_score()

ch = Chunks()
