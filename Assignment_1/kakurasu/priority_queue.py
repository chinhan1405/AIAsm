class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def push(self, item: tuple):
        self.queue.append(item)
        self.queue.sort(key=lambda x: x[0])
    
    def pop(self) -> tuple:
        return self.queue.pop(0)
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0