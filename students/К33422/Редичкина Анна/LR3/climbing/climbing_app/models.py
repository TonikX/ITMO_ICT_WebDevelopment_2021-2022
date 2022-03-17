from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=56)
    contact_person = models.CharField(max_length=60)
    e_mail = models.EmailField(max_length=60)
    phone_number = models.DecimalField(max_digits=15, decimal_places=0)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Peak(models.Model):
    name = models.CharField(max_length=80, unique=True)
    country = models.CharField(max_length=56)
    height = models.DecimalField(max_digits=5, decimal_places=0)
    climbing_duration = models.DecimalField(max_digits=5, decimal_places=0)
    route_description = models.TextField()

    def __str__(self):
        return self.name


class Climbing(models.Model):
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField(null=True)
    peak = models.ForeignKey(Peak, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Person, through='Participation')
    information = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.peak.name)


class Participation(models.Model):
    participant = models.ForeignKey(Person, on_delete=models.CASCADE)
    climbing = models.ForeignKey(Climbing, on_delete=models.CASCADE)


class EmergencySituation(models.Model):
    climbing = models.ForeignKey(
        Climbing, on_delete=models.CASCADE)
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE)
    description = models.TextField()


class ResultsForClubs(models.Model):
    climbing = models.ForeignKey(Climbing, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    description = models.TextField()


class ResultsForPerson(models.Model):
    climbing = models.ForeignKey(Climbing, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.TextField()
