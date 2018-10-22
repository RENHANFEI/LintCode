class MyCalendar:

    def __init__(self):
        self.cal = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start >= end:
            return False
            
        for book in self.cal:
            if start < book[1] and end > book[0]:
                return False
        
        self.cal.append([start, end])
        return True
        