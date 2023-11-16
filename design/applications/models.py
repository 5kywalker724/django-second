from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from .validators import CustomValidator
from django.core.validators import MinLengthValidator


class AdvUser(AbstractUser):
    username = models.CharField(
        verbose_name="Логин",
        max_length=150,
        unique=True,
        blank=False,
        help_text=(
            "Разрешается использовать только латиницу и дефис."
        ),
        validators=[UnicodeUsernameValidator],
        error_messages={
            "unique": "Пользователь с таким именем уже существует.",
        },
    )
    first_name = models.CharField(verbose_name="Имя", max_length=150, blank=False)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150, blank=False)
    email = models.EmailField(verbose_name="Почта", blank=False)
    patronymic = models.CharField(blank=False, verbose_name="Отчество", max_length=150)
