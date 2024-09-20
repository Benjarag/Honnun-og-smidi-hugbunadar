class AuthenticationService:
    def authenticate(self, username: str, password: str) -> bool:
        return username != password