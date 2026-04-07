import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #priority queue? min number so min-heap]
        #basically we use a min heap -> we pop the min task and when we use a task, we push it again but with integer n
        frequent = Counter(tasks) #returns [('x', 2)]
        heap = [-cnt for cnt in frequent.values()]
        heapq.heapify(heap)

        time = 0
        cooldown = deque() #pairs of [cnt, time]
        while heap or cooldown:
            time += 1

            if not heap:
                time = cooldown[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    cooldown.append([cnt, time + n])
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])
        return time 




        