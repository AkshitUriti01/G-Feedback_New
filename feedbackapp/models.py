from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


def validate_mobile(value):
    if not value.startswith("6") and not value.startswith(
            "7") and not value.startswith("8") and not value.startswith("9"):
        raise ValidationError(
            _("Mobile number must start with 6,7,8 or 9"),
            params={"value": value},
        )

    if len(value) != 10:
        raise ValidationError(
            _("Mobile number must be 10 digits long"),
            params={"value": value},
        )


def validate_reg_num(value):
    if not value.startswith("VU") and not value.startswith("vu"):
        raise ValidationError(
            _("Registration number must start with VU or vu"),
            params={"value": value},
        )


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    regNum = models.CharField(max_length=20)
    mobile = models.PositiveIntegerField()
    reason_for_visiting = models.TextField()
    whom_did_you_meet = models.TextField()
    description = models.TextField()
    isProblemSolved = models.BooleanField()
    rating = models.PositiveIntegerField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name
