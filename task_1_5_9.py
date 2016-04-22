class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        for num in a:
            self.buffer.append(num)
            if len(self.buffer) == 5:
                print(sum(self.buffer))
                self.buffer[:] = []
    
    def get_current_part(self):
        return self.buffer

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # [1, 2, 3]
buf.add(4, 5, 6) # print(15)
buf.get_current_part() # [6]
buf.add(7, 8, 9, 10) # print(40) 
buf.get_current_part() # []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) 
buf.get_current_part() # [1]
