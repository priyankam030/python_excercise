from random import randint

class Train:
   
    def __init__(self, trainNo, frm, to):
        self.trainNo = trainNo
        self.frm = frm
        self.to = to

    def book(self):
        print(f"Ticket is booked in train no: {self.trainNo} from {self.frm} to {self.to}")
        
        
    def getstatus(self):
        print(f"train no: {self.trainNo} is running on time")
        
    def getfare(self):
        print(f"Ticket fare in train no: {self.trainNo} from {self.frm} to {self.to} is {randint(222, 5555)}")
        
    
bookTicket = Train(12345, "lko", "ddu")

bookTicket.book()
bookTicket.getfare()
bookTicket.getstatus()

bookTicket1 = Train(12456,"pune", "ddu")
bookTicket1.book()
bookTicket1.getfare()
bookTicket1.getstatus()

