from models.intervals import IntervalSet, Interval
from typing import List

class MergeHandler():
    def __init__(self):
        pass

    def merge_intervals(self, includes: List[Interval], excludes: List[Interval]) -> List[Interval]:
        # merged_intervals = []
        merged_intervals = includes

        # for include_interval in includes:
        #     for exclude_interval in excludes:
        #         if exclude_interval.start <= include_interval.start <= exclude_interval.end:
        #             include_interval.start = exclude_interval.end + 1

        # for include_interval in includes:
        #     if not merged_intervals or merged_intervals[-1].end < include_interval.start:
        #         merged_intervals.append(include_interval)
        #     else:
        #         merged_intervals[-1].end = max(merged_intervals[-1].end, include_interval.end)

        return merged_intervals