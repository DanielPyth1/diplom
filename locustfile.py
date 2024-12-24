from locust import HttpUser, task

class EducationalModuleUser(HttpUser):
    @task
    def list_modules(self):
        self.client.get("/api/modules/")
