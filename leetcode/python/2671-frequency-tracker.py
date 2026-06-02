from collections import Counter


class FrequencyTrackerFirstAttempt:
    def __init__(self):
        self.arr = []

    def add(self, number: int) -> None:
        self.arr.append(number)

    def deleteOne(self, number: int) -> None:
        # O(n) in average case
        if number in self.arr:
            # Also O(n) in worst case
            self.arr.remove(number)

    def hasFrequency(self, frequency: int) -> bool:
        c = Counter(self.arr)
        return frequency in c.values()


class FrequencyTracker:
    def __init__(self):
        self.num_count = {}
        self.freq_count = {}

    def add(self, number: int) -> None:
        count = self.num_count.get(number, 0)
        # If the number has been stored already. we need to adjust freq_count
        if count > 0:
            self.freq_count[count] -= 1
            if self.freq_count[count] == 0:
                del self.freq_count[count]
        updated_count = count + 1
        self.num_count[number] = updated_count
        self.freq_count[updated_count] = self.freq_count.get(updated_count, 0) + 1

    def deleteOne(self, number: int) -> None:
        count = self.num_count.get(number, 0)
        if count == 0:
            return
        self.freq_count[count] -= 1
        if self.freq_count[count] == 0:
            del self.freq_count[count]
        updated_count = count - 1
        self.num_count[number] = updated_count
        if updated_count > 0:
            self.freq_count[updated_count] = self.freq_count.get(updated_count, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count.get(frequency, 0) > 0
