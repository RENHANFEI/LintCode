class MyCalendarTwo:

    def __init__(self):
        self.cal = []
        self.intersections = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :type book: [start, end]
        :rtype: bool
        """
        
        # if start >= end:
        #     return False
            
        if self.cal == []:
            self.cal.append([start, end])
            return True
        
        intersections = self.intersections[:]
        for book in self.cal:
            if start < book[1] and end > book[0]:
                intersections.append([max(start, book[0]), min(end, book[1])])
        
                
        if len(intersections) == 0:
            self.cal.append([start, end])
            return True
        
        # double or >double intersection
        intersections.sort()
        pre_intersection = intersections[0]
        for intersection in intersections[1:]:
            if intersection[0] < pre_intersection[1]:
                return False
            pre_intersection = intersection
        
        self.intersections = intersections[:]
        self.cal.append([start, end])
        
        return True