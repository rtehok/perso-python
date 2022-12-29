import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted([(enqueued, process, i) for i, (enqueued, process) in enumerate(tasks)])

        res = []

        next_task = []

        curr_time = 0
        task_index = 0

        while task_index < len(tasks) or next_task:
            if not next_task and curr_time < sorted_tasks[task_index][0]:
                # move current time to next index
                curr_time = sorted_tasks[task_index][0]

            while task_index < len(sorted_tasks) and curr_time >= sorted_tasks[task_index][0]:
                # the next eligible tasks are the one that happened during the processing of last task
                # add to next_task ordered by process_time to take the shortest one
                _, process_time, original_idx = sorted_tasks[task_index]
                heapq.heappush(next_task, (process_time, original_idx))
                task_index += 1

            process_time, index = heapq.heappop(next_task)

            curr_time += process_time

            res.append(index)

        return res


if __name__ == "__main__":
    assert Solution().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1]
    assert Solution().getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [4, 3, 2, 0, 1]
