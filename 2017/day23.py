
def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True


class Execution_v2:
    a, b, c, d, e, f, g, h = 1, 6700, 67, 0, 0, 0, 0, 0

    def __str__(self):
        return f'a:{self.a}, b:{self.b}, c:{self.c}, d:{self.d}, e:{self.e}, f:{self.f}, g:{self.g}, h:{self.h}, '

    def block1(self):
        # mutates [g, f, e]
        # uses [d, e, b]
        self.g = self.d * self.e - self.b
        if self.g == 0:
            self.f = 0
        self.e += 1
        self.g = self.e - self.b
        print(f'BLOCK 1, {str(self)}')

    def block1_imp(self):
        while self.e != self.b:
            if self.d * self.e == self.b:
                self.f = 0
            self.e += 1
            # print(f'BLOCK 1 IMP, {str(self)}')
        self.g = 0

    def block2(self):
        self.e = 2

        self.block1_imp()

        self.d += 1
        self.g = self.d - self.b
        print(f'BLOCK 2, {str(self)}')

    def block2_imp(self):
        while self.d != self.b:
            self.e = 2
            self.block1_imp()
            self.d += 1
            print(f'BLOCK 2 IMP, {str(self)}')
        self.g = 0

    def block2_imp2(self):
        if not is_prime(self.b):
            self.f = 0

    def block3(self):
        self.f = 1
        self.d = 2

        self.block2_imp2()

        if self.f == 0:
            self.h += 1
        if self.b == self.c:
            return self.h
        self.b += 17

    def execute(self):
        self.b += 100000
        self.c = self.b + 17000
        while True:
            h = self.block3()
            if h:
                return h


if __name__ == '__main__':
    import profile
    ex = Execution_v2()
    print(ex.execute())
