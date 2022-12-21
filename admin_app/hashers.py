from django.contrib.auth.hashers import BasePasswordHasher


class EmptyPasswordHasher(BasePasswordHasher):
    algorithm = 'empty'


    def verify(self, password, encoded):
        """Check if the given password is correct."""
        print(password, encoded)
        return password == encoded

    def encode(self, password, salt):
        print(password)
        return password

    def safe_summary(self, encoded):
        return {
            'algorithm': self.algorithm,
        }

