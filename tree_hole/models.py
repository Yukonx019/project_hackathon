from django.db import models


class Challenge(models.Model):
    """A problem waiting for a cross-disciplinary knowledge block."""

    title = models.CharField(max_length=120)
    description = models.TextField()
    author_name = models.CharField(max_length=80, default="Anonymous student")
    discipline = models.CharField(max_length=50)
    tags = models.CharField(max_length=240, blank=True)
    hearts = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class KnowledgeBlock(models.Model):
    """A contributed perspective which can be remixed into a challenge."""

    challenge = models.ForeignKey(Challenge, related_name="blocks", on_delete=models.CASCADE)
    body = models.TextField()
    author_name = models.CharField(max_length=80, default="Anonymous student")
    discipline = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Block for {self.challenge_id}: {self.body[:40]}"
