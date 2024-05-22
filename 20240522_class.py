class Job:
    def __init__(self, work, deadline, profit):
        self.work = work
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f"Job(work={self.work}, deadline={self.deadline}, profit={self.profit})"

class JobScheduler:
    def __init__(self, jobs):
        self.jobs = jobs

    def schedule(self):
        # Sort jobs by profit in descending order
        self.jobs.sort(key=lambda x: x.profit, reverse=True)

        n = len(self.jobs)
        result = [None] * n
        slot = [False] * n

        for job in self.jobs:
            for j in range(min(n, job.deadline) - 1, -1, -1):
                if not slot[j]:
                    slot[j] = True
                    result[j] = job
                    break

        scheduled_jobs = [job for job in result if job is not None]
        # Sort the scheduled jobs by their deadlines to get the correct order
        scheduled_jobs.sort(key=lambda x: x.deadline)

        return [job.work for job in scheduled_jobs]

# Example usage
jobs = [
    Job(1, 3, 40),
    Job(2, 1, 35),
    Job(3, 1, 30),
    Job(4, 3, 25),
    Job(5, 1, 20),
    Job(6, 3, 15),
    Job(7, 2, 10)
]

scheduler = JobScheduler(jobs)
optimal_schedule = scheduler.schedule()

print(optimal_schedule)
