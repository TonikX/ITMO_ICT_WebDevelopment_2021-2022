from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from multiselectfield import MultiSelectField


class CustomAccountManager(BaseUserManager):
    def create_user(self, phone_number, email, first_name, password, **others_fields):
        if not phone_number:
            raise ValueError('You must provide an phone_number')
        if not first_name:
            raise ValueError('You must provide an first_name')
        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, first_name=first_name, password=password,
                          **others_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, email, first_name, password, **others_fields):
        others_fields.setdefault('is_superuser', True)
        others_fields.setdefault('is_staff', True)
        others_fields.setdefault('is_active', True)

        if others_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        if others_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')

        if others_fields.get('is_active') is not True:
            raise ValueError('Superuser must be assigned to is_active=True')

        return self.create_user(phone_number, email, first_name, password, **others_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    join_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_host = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'email']

    def __str__(self):
        return self.phone_number


def upload_path(instance, filename):
    return '/'.join(['places', str(instance.title), filename])


class Place(models.Model):
    PLACE_TYPES = [
        ('1', 'Apartment'),
        ('2', 'House'),
        ('3', 'Secondary unit'),
        ('4', 'Unique space'),
        ('5', 'Boutique hotel'),
        ('6', 'Bed and breakfast'),
    ]
    PLACE_OFFERS = [('1', 'Kitchen'),
                    ('2', 'Wifi'),
                    ('3', 'Free parking on premises'),
                    ('4', 'Pets allowed'),
                    ('5', 'Hair dryer'),
                    ('6', 'Shampoo'),
                    ('7', 'Body soap'),
                    ('8', 'Hot water'),
                    ('9', 'Body Washer'),
                    ('10', 'Bed linens'),
                    ('11', 'Smoke alarm'),
                    ('12', 'Cooking basics'),
                    ('13', 'TV'), ('14', 'Air conditioning'),
                    ('15', 'Heating'),
                    ('16', 'Private entrance')]
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    place_type = models.CharField(choices=PLACE_TYPES, default=1, max_length=1)
    place_offers = MultiSelectField(choices=PLACE_OFFERS)
    desc = models.CharField(max_length=1000)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    guests = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to=upload_path)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Reserve(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests_count = models.IntegerField()

    def __str__(self):
        return 'place: {}, {}, {}, guests:{}'.format(self.place.title, self.check_in_date, self.check_out_date,
                                                     self.guests_count)


class Review(models.Model):
    RATING_VALUE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000)
    review_date = models.DateField(auto_now_add=True)
    value = models.IntegerField(choices=RATING_VALUE, default='5')

    def __str__(self):
        return 'author: {},'.format(self.author.first_name)
