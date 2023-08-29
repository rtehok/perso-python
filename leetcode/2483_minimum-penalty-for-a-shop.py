class Solution:
    def bestClosingTimeV1(self, customers: str) -> int:
        n = len(customers)
        nb_Y_after = [0] * (n + 1)
        nb_N_before = [0] * (n + 1)

        for i in range(1, n + 1):
            if i > 0 and customers[i - 1] == "N":
                nb_N_before[i] = nb_N_before[i - 1] + 1
                continue
            nb_N_before[i] = nb_N_before[i - 1]

        for i in range(n - 1, -1, -1):
            if customers[i] == "Y":
                nb_Y_after[i] = nb_Y_after[i + 1] + 1
                continue
            nb_Y_after[i] = nb_Y_after[i + 1]

        min_penalty = float("inf")
        earliest_hour = 0
        for i in range(n + 1):
            if nb_N_before[i] + nb_Y_after[i] < min_penalty:
                min_penalty = nb_N_before[i] + nb_Y_after[i]
                earliest_hour = i

        return earliest_hour

    def bestClosingTimeTwoPasses(self, customers: str) -> int:
        cur_penalty = min_penalty = customers.count("Y")
        earliest_hour = 0

        for i, ch in enumerate(customers):
            if ch == "Y":
                cur_penalty -= 1
            else:
                cur_penalty += 1

            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                earliest_hour = i + 1

        return earliest_hour

    def bestClosingTime(self, customers: str) -> int:
        cur_penalty = min_penalty = 0
        earliest_hour = 0

        for i, ch in enumerate(customers):
            if ch == "Y":
                cur_penalty -= 1
            else:
                cur_penalty += 1

            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                earliest_hour = i + 1

        return earliest_hour


if __name__ == "__main__":
    assert Solution().bestClosingTime("NYNNNYYN") == 0
    assert Solution().bestClosingTime("YYNY") == 2
    assert Solution().bestClosingTime("NNNNN") == 0
    assert Solution().bestClosingTime("YYYY") == 4
