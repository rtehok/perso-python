from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        circle_students_cnt = cnt.get(0, 0)
        square_students_cnt = cnt.get(1, 0)

        for sandwich in sandwiches:
            if sandwich == 0 and circle_students_cnt == 0:
                return square_students_cnt
            if sandwich == 1 and square_students_cnt == 0:
                return circle_students_cnt

            if sandwich == 0:
                circle_students_cnt -= 1
            else:
                square_students_cnt -= 1

        return 0


assert Solution().countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]) == 0
assert Solution().countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]) == 3
