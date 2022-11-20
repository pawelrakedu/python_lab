from locust import HttpUser, task

class getprime(HttpUser):
    @task(3)
    def getprime(self):
        self.client.get("time")
