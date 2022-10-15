#Nicky Julyatrika Sari NIM L200200101
#Modul 8
#Nomer 4

class Queue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist.pop(0)
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[-1]

class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def getFrontMost(self):
        x = 0
        while self.qlist[x].priority != 0:
            x+=1
        return self.qlist[x].item
    def getRearMost(self):
        a = []
        for i in self.qlist:
            a.append(i.priority)
        print (self.qlist[a.index(max(a))].item)
        
class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority
        
M = Queue()
M.enqueue(38)
M.enqueue(12)
M.enqueue(45)
M.enqueue(23)
M.enqueue(4)

N = PriorityQueue()
N.enqueue("Jeruk", 3)
N.enqueue("Tomat", 5)
N.enqueue("Mangga", 0)
N.enqueue("Duku", 2)
N.enqueue("Pepaya", 1)

