'''
google foo.bar challenge 2.2

This is the solution for challenge 2.2 of the Google foo.bar challenge called
zombit_monitoring.  The premise is like this:
you get a list of two element lists.  the two elements lists represent time
intervals where a zombit is being monitored by minions.  The intervals can overlap
and there can be missing time between monitoring intervals.  The goal is to
count the total number of time units during which the zombit has been monitored
by at least 1 minion.  The catch is that the numbers in the intervals can be as
large as 2**30-1, so simply creating ranges of monitoring units and putting them
in a set or dictionary can cause memory issues. See foo_bar.test.TestCallenge2
for example results.
'''

class Interval:
    def __init__(self, begin = None, end = None):
        self.data = [0,0]
        if begin:
            self.data[0] =begin
        if end:
            self.data[1] = end
        
    def __repr__(self):
        return '[' + str(self.data[0]) + ', ' + str(self.data[1]) + ']'
    
    def begin(self):
        return self.data[0]
    
    def end(self):
        return self.data[1]

    def __lt__(self, other):
        return self.begin() <= other.begin()
    
    def touches(self, other):
        return not (self.begin() > other.end() or self.end() < other.begin())
    
    def touches_any(self, otherList):
        for other in otherList:
            if other.touches(self):
                return True
        return False
    
    def copy(self):
        return Interval(self.begin(), self.end())
    
    def pointsList(self):
        return [self.begin(), self.end()]
    
    def combine(self, other):
        if self.touches(other):
            allPoints = self.pointsList()
            allPoints.extend(other.pointsList())
            return Interval(min(allPoints), max(allPoints))
        return None
    
    def length(self):
        return self.end() - self.begin()

def answer(intervals):
    nonDupIntervals = []
    [nonDupIntervals.append(interval) for interval in intervals if interval not in nonDupIntervals]
    newIntervals = []
    [newIntervals.append(Interval(interval[0],interval[1])) for interval in nonDupIntervals]
    newIntervals.sort(reverse = True)
    combinedIntervals = []
    interval = newIntervals.pop()
    while interval:
        touchingIntervals = [newInterval for newInterval in newIntervals \
                             if newInterval.touches(interval)]
        newCombinedInterval = interval.copy()
        for touchingInterval in touchingIntervals:
            newCombinedInterval = newCombinedInterval.combine(touchingInterval)
            newIntervals.remove(touchingInterval)
        if newCombinedInterval.touches_any(combinedIntervals):
            touchingIntervals = [combinedInterval for combinedInterval in combinedIntervals \
                                 if combinedInterval.touches(newCombinedInterval)]
            for touchingInterval in touchingIntervals:
                newCombinedInterval = newCombinedInterval.combine(touchingInterval)
                combinedIntervals.remove(touchingInterval)
        combinedIntervals.append(newCombinedInterval)
        if newIntervals:
            interval = newIntervals.pop()
        else:
            interval = None
    return sum([interval.length() for interval in combinedIntervals])

if __name__ == '__main__':
    intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
    print intervals
    print answer(intervals)