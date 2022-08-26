# Mini challenge 1

### Set the newspaper project up

#### During this first phase, we'll focus our attention on setup and configuration.

1. Create a new django project in this directory (news) that uses this directory as it's containing folder.
2. Create the following apps:
2.1. accounts
2.2. articles
2.3. pages
3. Modify config.settings to include the following:
3.1. Configure the allowed hosts list (bear in mind, we'll be deploying to heroku later)
3.2. Configure the SECRET_KEY and DEBUG settings to read from environment variables.
3.3. Configure the templates directories.
3.4. Configure static and staticfiles directories (consider using whitenoise).
4. *IMPORTANT: Don't run the migrations.*
5. Create the following models in the accounts/models.py file:

```
from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)

```