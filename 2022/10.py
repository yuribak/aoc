f = "2022/input/" + __file__.split('/')[-1].split('.')[0]

with open(f) as fin:
    data = [_.strip().split() for _ in fin]

class AOC(object):

    def __init__(self, data) -> None:
        self.X = 1
        self.C = 0
        self.P = 0
        self.data = data
        self.buff = []
        self.S =0

    def tick(self):
        self.C += 1
        print('#' if self.X-1 <= self.P <=self.X+1 else '.', end='')
        if self.C in range(20,len(self.data)*2, 40):
            self.S += self.C*self.X
        self.P = (self.P+1)%40        
        if not self.P:
            print()
        if self.buff:
            self.X += self.buff.pop(0)
            self.C += 1
        else:
            self.C += 1
            c, *v = self.data.pop(0)
            if c == 'addx':
                self.buff.append(int(v[0]))

    def run(self):
        while self.data:
            self.tick()
        return self.S

    
AOC(data).run()
        
