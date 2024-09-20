class AuthorizationService:
    def authenticate(self, username: str, password: str) -> bool:
        return username != password
