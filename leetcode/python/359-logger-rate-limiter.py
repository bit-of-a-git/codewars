from collections import defaultdict


class Logger:
    def __init__(self):
        # We only really need to store one value at a time
        # So I think we can use an int
        self.requests = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.requests[message] <= timestamp:
            self.requests[message] = timestamp + 10
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
