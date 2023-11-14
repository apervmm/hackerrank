from typing import List

def mcis(data: List[int], k: int) -> List[int]:
    common_elements_set = set()
    for i in range(len(data) - k + 1):
        curr_subarray = []

        for j in range(i, i + k):
            curr_subarray.append(data[j])
        print(curr_subarray)

        if len(common_elements_set) == 0:
            common_elements_set = set(curr_subarray)
        else:
            new_subarray_set = set(curr_subarray)
            common_elements_set = common_elements_set & new_subarray_set

            if len(common_elements_set) == 0:
                return -1
    return min(common_elements_set)


def mci(data: List[int]) -> List[int]:
    res = []
    for i in range(1, len(data)+1):
        res.append(mcis(data, i))
    return res


data = [4, 3, 3, 4, 2]
print(mci(data))