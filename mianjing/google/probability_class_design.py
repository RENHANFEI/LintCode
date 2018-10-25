'''
Design a class to return a query based on its probability.
Input: dictionary with key = query_name, value = probability
Eg. {a: 0.5, b: 0.2, c: 0.2, d: 0.1}
Output: a or b or c or d with probability stated in the input
'''
import random

class RandomWithProbability(object):

    def __init__(self, arg):
        # initialize with the elements and their probabilities
        self.probabilities = dict(arg) # convert to dict
        self.elements = []
        self.cumulatives = []
        self.__getProbabilityDict()


    def getRandomElement(self):
        randf = random.random()
        idx = self.__mapToIdx(randf)
        return self.elements[idx]

    def __mapToIdx(self, randf):
        # use binary search
        start, end = 0, len(self.cumulatives)
        while start + 1 < end:
            mid = (start + end) // 2
            cumulative = self.cumulatives[mid]
            if randf > cumulative:
                l = mid
            elif randf < cumulative:
                r = mid
            else:
                return mid - 1 if mid > 0 else 0

            if randf > self.cumulatives[start]:
                return end
            else:
                return start


    def __getProbabilityDict(self):
        pos = 0
        for element, probability in self.probabilities.items():
            pos += probability
            self.elements.append(element)
            self.cumulatives.append(pos)

        if round(pos, 8) != 1:
            raise Exception("Probabilities do not sum up to 1!")


test = {'a': .5, 'b': .2, 'c': .2, 'd': .1}
randomWithProbability = RandomWithProbability(test)
print(randomWithProbability.getRandomElement())

# class RandomWithProbability(object):

#     def __init__(self, arg):
#         # initialize with the elements and their probabilities
#         self.probabilities = dict(arg) # convert to dict
#         self.elements_list = []
#         self.__getElementList()

#     def getRandomElement(self):
#         idx = random.randint(0, len(self.elements_list) - 1)
#         return self.elements_list[idx]

#     def __getElementList(self):
#         min_probability = min(self.probabilities.values())
#         multiplier = 1
#         while int(min_probability * multiplier) != min_probability * multiplier:
#             multiplier *= 10

#         for element, probability in self.probabilities.items():
#             time = int(probability * multiplier)
#             self.elements_list += [element] * time