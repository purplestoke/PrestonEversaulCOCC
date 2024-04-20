import re


class WFQ:
    def __init__(self, filename):
        self.filename = filename
        self.prem = r"P [a-zA-Z]+"
        self.econ = r"E [a-zA-Z]+"
        self.stan = r"S [a-zA-Z]+"
        self.premQ = []
        self.econQ = []
        self.stanQ = []
    
    def createQueues(self):
        with open(self.filename, "r") as f:
            for line in f:
                line.strip()
                # FIND PREMIUM
                if re.match(self.prem, line):
                    cleanLine= line.replace('P', "", 1).strip()
                    self.premQ.append(cleanLine)
                # FIND ECONOMY
                elif re.match(self.econ, line):
                    cleanLine = line.replace('E', "", 1).strip()
                    self.econQ.append(cleanLine)
                # FIND STANDARD
                elif re.match(self.stan, line):
                    cleanLine = line.replace("S", "", 1).strip()
                    self.stanQ.append(cleanLine)
                else:
                    pass
        return 
    
    def processQueues(self):
        while self.premQ or self.econQ or self.stanQ:
            # PROCESS PREMIUM
            for i in range(3):
                if self.premQ:
                    print(f"Premium processed: {self.premQ.pop(0)}")

            # PROCESS ECONOMY
            for i in range(2):
                if self.econQ:
                    print(f"Economy processed: {self.econQ.pop(0)}")

            # PROCESS STANDARD
            if self.stanQ:
                print(f"Standard processed: {self.stanQ.pop(0)}")
        print("All Queues Processed!")
        return

# RUNNING IT
WFQIns = WFQ("inputQueue.txt")
WFQIns.createQueues()
WFQIns.processQueues()




