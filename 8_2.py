
class Digits:
    def __init__(self):
        self.digits = []
        self.screens = []
        with open('data/8.txt', 'r') as f:

            for line in f:
                self.digits.append(line.split('|')[0].strip().split(' '))
                self.screens.append(line.split('|')[1].strip().split(' '))

        self.res = 0

        for digits, screen in zip(self.digits, self.screens):
            self.res  += self.get_vals(digits, screen)

        print('Result: ', int(self.res))


    def get_first_four(self, digits):
        translator = {}

        for digit in digits:
            if len(digit) == 2:
                translator[1] = digit
            elif len(digit) == 3:
                translator[7] = digit
            elif len(digit) == 4:
                translator[4] = digit
            elif len(digit) == 7:
                translator[8] = digit

        return translator

    def exclude_parts(self, digit, parts):

        for part in parts:

            if part not in digit:
                return part, True

        return '', False

    def get_number(self, numbers, tr_rev):
        val = 0
        multi = 1000
        
        for number in numbers:
            nice = ''.join(sorted(number))
            val += tr_rev[nice] * multi
            multi /= 10

        return val

    def get_vals(self, digits, screen):
        suma = 0
        translator = self.get_first_four(digits)
        translator = self.get_rest(digits, translator)
        clean = {}

        for key in translator:
            key_sorted = translator[key]
            key_sorted = ''.join(sorted(key_sorted))
            clean[key] = key_sorted

        reverted =  {clean[key]:key for key in clean}
        suma = self.get_number(screen, reverted)

        return suma

    def get_rest(self, digits, translator):
        horizontal = [part for part in translator[4] if part not in translator[1]]

        for digit in digits:
            if len(digit) == 6:
                _, val = self.exclude_parts(digit, horizontal)
                if val:
                    translator[0] = digit
                    continue
                pg, val = self.exclude_parts(digit, translator[1])
                if val:
                    translator[6] = digit
                    continue
                translator[9] = digit

        for digit in digits:
            if len(digit) == 5:
                _, val0 = self.exclude_parts(digit, translator[1])
                if not val0:
                    translator[3] = digit
                    continue
                pg, _ = self.exclude_parts(translator[6], translator[8])
                _, val = self.exclude_parts(digit, pg)
                if val:
                    translator[5] = digit
                    continue
                translator[2] = digit

        return translator
                    
dig = Digits()
