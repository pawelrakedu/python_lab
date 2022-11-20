from locust import HttpUser, task

class getprime(HttpUser):
    @task
    def getprime(self):
        self.client.get("prime/2")
        
    @task
    def getprime(self):
        self.client.get("prime/999999")
     
    @task
    def getprime(self):
        self.client.get("time")
