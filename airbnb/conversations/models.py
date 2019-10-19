from django.db import models
from core import models as core_models


class Converstation(core_models.TimeStampModel):
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    converstation = models.ForeignKey("Converstation", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} say: {self.text}'
