from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def post_user_create(self):
        payload = {
            "id": 4141,
            "username": "testayse",
            "firstName": "ayse",
            "lastName": "abd",
            "email": "ayse.test@test.com",
            "password": "ayseayse",
            "phone": "41414141414",
            "userStatus": 1
            }
        self.client.post("https://petstore.swagger.io/v2/user", json=payload)

    @task
    def get_user_info(self):
        self.client.get("https://petstore.swagger.io/v2/user/testayse")

    @task
    def get_user_login(self):
        payload = {
            "username": "testayse",
            "password": "ayseayse"
            }
        self.client.get("https://petstore.swagger.io/v2/user/login", params=payload)

    @task
    def get_logout(self):
        self.client.get("https://petstore.swagger.io/v2/user/logout")

    @task
    def put_user_update(self):
        payload = {
                "id": 4141,
                "username": "testayse",
                "firstName": "ayse",
                "lastName": "abc",
                "email": "ayse@test.com",
                "password": "ayseabc",
                "phone": "41414141414",
                "userStatus": 1
             }
        self.client.put("https://petstore.swagger.io/v2/user/testayse", json=payload)

    @task
    def delete_username(self):
        payload = {
            "id": 4141,
            "username": "testayseabd",
            "firstName": "ayse",
            "lastName": "abc",
            "email": "ayse@test.com",
            "password": "ayseabc",
            "phone": "41414141414",
            "userStatus": 1
            }
        self.client.post("https://petstore.swagger.io/v2/user/testayseabd", json=payload)
        self.client.delete("https://petstore.swagger.io/v2/user/testayseabd")

    @task
    def post_create_with_array(self):
        payload = [
            {
                "id": 1,
                "username": "ayseabdc",
                "firstName": "ds",
                "lastName": "sd",
                "email": "strsing@test.com",
                "password": "fsf",
                "phone": "566789886877g",
                "userStatus": 0
            }]
        self.client.post("https://petstore.swagger.io/v2/user/createWithArray", json=payload)

