from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, login, customertype, password=None):
        if not login:
            raise ValueError('Users must have an login.')

        user = self.model(
            login=login,
            customertype=customertype,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None):
        user = self.create_user(
            login=login,
            password=password,
            customertype=self.model.CUSTOMER_FLIGHT_WORKER
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
