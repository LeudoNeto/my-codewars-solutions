class Miner:
    def __init__(self, xp=0):
        self.level = 1
        self.xp = xp
        if xp > 0:
            for x,y in EXPERIENCE.items():
                if xp >= y:
                    self.level = x
    
    def mine(self, rock):
        if self.level == 40:
            return 'You swing your pick at the rock.'
        if self.level < ROCKS[rock][0]:
            return f'You need a mining level of {ROCKS[rock][0]} to mine {rock}.'
        else:
            self.xp += ROCKS[rock][1]
            if self.xp >= EXPERIENCE[self.level+1]:
                self.level += 1
                return f'Congratulations, you just advanced a Mining level! Your mining level is now {self.level}.'
            else:
                return 'You swing your pick at the rock.'