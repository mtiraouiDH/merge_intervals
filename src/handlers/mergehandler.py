from models.intervals import IntervalSet, Interval
from typing import List
from utils.transformers import transform_to_list_of_dicts, transform_to_list_of_tuples

class MergeHandler():

    def merge_overlapping(self, intervals):
        if intervals == []:
            return []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        merged_intervals = [sorted_intervals[0]]

        for current_start, current_end in sorted_intervals[1:]:
            previous_start, previous_end = merged_intervals[-1]

            # Check for intersection
            if current_start <= previous_end:
                # Merge overlapping intervals
                merged_intervals[-1] = (previous_start, max(current_end, previous_end))
            else:
                # No intersection, add the current interval
                merged_intervals.append((current_start, current_end))

        return merged_intervals
    
    def merge_intervals(self, includes: List[Interval], excludes: List[Interval]) -> List[Interval]:
        
        output_intervals = []

        includes_tuples = transform_to_list_of_tuples(includes)
        excludes_tuples = transform_to_list_of_tuples(excludes)

        sorted_includes_tuples = self.merge_overlapping(includes_tuples)
        sorted_excludes_tuples = self.merge_overlapping(excludes_tuples)

        i, j = 0, 0

        while i < len(sorted_includes_tuples) and j < len(sorted_excludes_tuples):
            
            start1, end1 = sorted_includes_tuples[i]
            start2, end2 = sorted_excludes_tuples[j]

            # Check if sorted_includes_tuples interval is entirely before sorted_excludes_tuples interval
            if end1 < start2:
                output_intervals.append(sorted_includes_tuples[i])
                i += 1

            # Check if sorted_includes_tuples is entirely after sorted_excludes_tuples
            # remove the current ixclude interval as it has no effect
            elif end2 < start1:
                sorted_excludes_tuples = sorted_excludes_tuples[1:]

            # If there a partial overlap, add the not overlapped range
            elif start1 <= start2 and end1 <= end2:
                output_intervals.append((sorted_includes_tuples[i][0], sorted_excludes_tuples[j][0]-1))
                i += 1

            # If there an overlap, move to the next interval in sorted_includes_tuples
            elif end1 >= start2 and end1 <= end2:
                i += 1

            # If sorted_includes_tuples extends beyond sorted_excludes_tuples
            elif end1 > end2 and start2 < start1:
                sorted_includes_tuples[i] = (sorted_excludes_tuples[j][1]+1, sorted_includes_tuples[i][1])
                j += 1
            # If sorted_includes_tuples includes sorted_excludes_tuples
            else:
                output_intervals.append((sorted_includes_tuples[i][0], sorted_excludes_tuples[j][0]-1))
                sorted_includes_tuples[i] = (sorted_excludes_tuples[j][1]+1, sorted_includes_tuples[i][1])

        # Add remaining intervals from sorted_includes_tuples
        while i < len(sorted_includes_tuples):
            print ("i: " + str(i) + ", j: " + str(j))
            output_intervals.append(sorted_includes_tuples[i])
            i += 1
        # return self.transform_to_list_of_dicts(self.deduct_intervals(sorted_includes_tuples, sorted_excludes_tuples))
        return transform_to_list_of_dicts(output_intervals)
        