class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue
        start = t - 3000
        queue.append(t)
        while(queue and queue[0] < start):
            queue.popleft()
        return len(queue)
    