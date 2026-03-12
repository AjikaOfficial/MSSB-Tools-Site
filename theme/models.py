from django.db import models
import hashlib


class Image(models.Model):
    file = models.ImageField(upload_to="images/")
    sha256 = models.CharField(max_length=64, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.file and not self.sha256:
            sha = get_file_hash(self.file)

            existing = Image.objects.filter(sha256=sha).first()
            if existing:
                self.pk = existing.pk
                self.file = existing.file
                self.sha256 = existing.sha256
                return

            self.sha256 = sha

        super().save(*args, **kwargs)

    def __str__(self):
        path = self.file.name
        return path.split("/")[-1] if "/" in path else path
    def path(self):
        return self.file.name


def get_file_hash(file):
    hash = hashlib.sha256()
    for chunk in file.chunks():
        hash.update(chunk)

    file.seek(0)
    return hash.hexdigest()