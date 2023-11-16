from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class CustomValidator(validators.RegexValidator):
    regex = r"\w[а-яА-ЯёЁ]"
    message = _(
        "Введите допустимое слово. Должно содержать кириллицу и символы пробела и дефис."
    )
    flags = 0
