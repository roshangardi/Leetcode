from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        coursemap = defaultdict(list)
        indegreelist = [0] * numCourses

        for course in prerequisites:
            indegreelist[course[0]] += 1
            coursemap[course[1]].append(course[0])

        count = 0
        # result = []
        queue = []
        for i in range(numCourses):
            if indegreelist[i] == 0:
                queue.append(i)

        while queue:
            popednode = queue.pop(0)
            # result.append(popednode)
            for j in coursemap[popednode]:
                indegreelist[j] -= 1
                if indegreelist[j] == 0:
                    queue.append(j)
            count += 1

        if count == numCourses:
            # print("Course can be taken in following order: {}".format(result))
            return True
        else:
            return False


obj = Solution()
prerequisites = [[1, 0], [1, 2]]
print(obj.canFinish(3, prerequisites))