from django.db import models


class Room(models.Model):
    SUBJECTS = (
        ('math', 'Математика'),
        ('inf', 'Информатика'),
        ('othr', 'Другое')
    )
    SUBJECTS_COLOR = (
        ('math', '#28a745'),
        ('inf', '#007bff'),
        ('othr', '#6c757d')
    )

    name = models.CharField(max_length=32)
    subject = models.CharField(max_length=4, choices=SUBJECTS)
    description = models.TextField()

    creator = models.CharField(max_length=162)
    max_people = models.IntegerField(default=5)
    audio_works = models.BooleanField(default=False)

    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def subject_name(self):
        return dict(self.SUBJECTS)[self.subject]

    def subject_color(self):
        return dict(self.SUBJECTS_COLOR)[self.subject]
