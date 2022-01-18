from django import VERSION
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    """Кастомная модель юзера, если возникнет необходимость
    добавлять дополнительные поля"""
    pass


class ListingCategory(models.Model):
    """Модель категории аукционов"""
    name = models.CharField(
        max_length=128,
        verbose_name="название"
    )

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "категория аукциона"
        verbose_name_plural = "категории аукционов"


class Listing(models.Model):
    """Модель вещи, выставленной на аукцион"""

    title = models.CharField(
        max_length=128,
        verbose_name="название"
    )

    description = models.TextField(
        verbose_name="описание"
    )

    starting_bid = models.DecimalField(
        decimal_places=2, 
        max_digits=15,
        verbose_name="начальная стоимость"
    )

    image_url = models.URLField(
        blank=True,
        verbose_name="ссылка на изображение"
    )

    category = models.ForeignKey(
        ListingCategory,
        on_delete=models.PROTECT,                
        related_name='listings',
        null=True,
        blank=True,
        verbose_name="категория"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="время создания"
    )

    created_by = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,                 
        related_name='listings',
        verbose_name="создатель"
    )

    active = models.BooleanField(
        default=True,
        verbose_name="активен?"
    )

    winner = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,                
        related_name='winner',
        null=True,
        blank=True,
        verbose_name="победитель аукциона"
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('listing_detail', kwargs={'pk': self.pk})

    def highest_bidder(self):
        highest_bid = Bid.objects.filter(listing=self).order_by('-value')
        if highest_bid:
            return highest_bid[0].bidder
        else:
            return None

    def current_price(self):
        highest_bid = Bid.objects.filter(listing=self).order_by('-value')
        if highest_bid:
            return highest_bid[0].value
        else:
            return None

    class Meta:
        verbose_name = "вещь, выставленная на аукцион"
        verbose_name_plural = "вещи, выставленные на аукцион"


class ListingComment(models.Model):
    """Модель комментария к аукциону"""

    original_listing = models.ForeignKey(
        Listing, 
        on_delete=models.PROTECT,
        related_name='comments',
        verbose_name="вещь на аукционе"
    )

    text = models.TextField(
        verbose_name="текст"
    )

    author = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,
        related_name='comments',
        verbose_name="автор"
    )
    
    rating = models.IntegerField(default=1)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        s = f'On {self.original_listing} by {self.author} with {self.rating}'
        return s

    class Meta:
        verbose_name = "комментарий к аукциону"
        verbose_name_plural = "комментарии к аукциону"


class Bid(models.Model):
    """Модель предложения цены на аукционе"""

    bidder = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,
        related_name='bids',
        verbose_name="участник аукциона"
    )

    listing = models.ForeignKey(
        Listing, 
        on_delete=models.PROTECT,
        related_name='bids',
        verbose_name="вещь на аукционе"
    )

    value = models.DecimalField(
        decimal_places=2,
        max_digits=15,
        verbose_name="предлагаемая цена"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="время создания"
    )

    def __str__(self) -> str:
        return f'{self.bidder} {self.value}'
    
    class Meta:
        verbose_name = "предложение цены"
        verbose_name_plural = "предложения цены"


class WatchList(models.Model):
    """Модель списка аукционов, за которыми следит пользователь"""

    owner = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        verbose_name="пользователь"
    )

    items = models.ManyToManyField(
        Listing,
        verbose_name="вещи на аукционе"
    )

    def __str__(self) -> str:
        return f"{self.owner}'s watchlists"
    
    class Meta:
        verbose_name = "watch list пользователя"
        verbose_name_plural = "watch list'ы пользователей"
