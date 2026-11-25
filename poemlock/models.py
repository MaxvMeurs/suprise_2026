from django.db import models


class Poem(models.Model):
    title = models.CharField(max_length=200, default="Gedicht")
    body = models.TextField(help_text="Vul hier het gedicht in dat je wilt tonen.")
    active = models.BooleanField(default=True, help_text="Alleen het meest recente actieve gedicht wordt getoond.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} ({'actief' if self.active else 'inactief'})"


class Task(models.Model):
    order = models.PositiveSmallIntegerField(unique=True, help_text="Volgorde (1, 2, 3).")
    question = models.TextField(help_text="De vraag/opdracht zoals getoond aan de gebruiker.")
    correct_answer = models.CharField(max_length=200, help_text="Het juiste antwoord (vergelijking gebeurt hoofdletter-ongevoelig).")
    digit = models.CharField(max_length=1, help_text="Het cijfer (0-9) dat deze opdracht oplevert voor het combinatieslot.")

    class Meta:
        ordering = ["order"]

    def __str__(self) -> str:
        return f"Opdracht {self.order}: {self.question[:40]}..."
