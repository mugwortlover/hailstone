class HailstoneData:
    def __init__(self):
        self.nums_checked = []
        self.speeds = []


    def add(self, num, speed):
        if self.contains(num):
            return
        
        if len(self.nums_checked) == 0:
            self.nums_checked.append(num)
            self.speeds.append(speed)
        else:
            i = 0
            while i < len(self.nums_checked) and num > self.nums_checked[i]:
                i += 1
            self.nums_checked.insert(i, num)
            self.speeds.insert(i, speed)


    def contains(self, num):
        def rec(low, high):
            if low == high:
                return False
            
            mid = (low + high) // 2
            
            if num < self.nums_checked[mid]:
                return rec(low, mid)
            elif self.nums_checked[mid] < num:
                return rec(mid + 1, high)
            else:
                return True
        
        return rec(0, len(self.nums_checked))
    
    def get_speed(self, num):
        ind = self.nums_checked.index(num)
        return self.speeds[ind]