import math
class TurretDefense:
    def firstMiss(self, xs, ys, times):
        x1 = 0
        y1 = 0
        time = 0
        for i in range(len(xs)):
            x2 = xs[i]
            y2 = ys[i]
            dist = abs(x2 - x1) + abs(y2 - y1)
            if(times[i] < time + dist):
                return i
            x1 = x2
            y1 = y2
            time = times[i]
        return -1
