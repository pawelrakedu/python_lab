
from locust import HttpUser, task

class getprime(HttpUser):
    @task(2)
    def getprime(self):
        self.client.get("prime/999999")
