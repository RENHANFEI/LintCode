from collections import defaultdict, Counter
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        can_take = {i for i in range(numCourses)}
        indegrees = Counter()

        pre_to_post = defaultdict(lambda: [])
        for post, pre in prerequisites:
            pre_to_post[pre].append(post)
            indegrees[post] += 1
            if post in can_take:
                can_take.remove(post)

        order = []
        while can_take:
            take = can_take.pop()
            order.append(take)
            for post in pre_to_post[take]:
                indegrees[post] -= 1
                if indegrees[post] == 0:
                    can_take.add(post)

        if len(order) < numCourses:
            return []

        return order

