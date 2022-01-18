from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Listing, ListingComment, ListingCategory, Bid, WatchList, User
from .forms import ListingCommentForm


class ListingList(ListView):
    """Список всех вещей, выставленных на аукцион"""
    model = Listing
    template_name = "auctions/index.html"

    def get_queryset(self):
        listings = Listing.objects.filter(active=True)
        return listings


class CategoryList(ListView):
    """Список всех категорий аукционов"""
    model = ListingCategory
    template_name = "auctions/categories.html"


class WatchListList(LoginRequiredMixin, ListView):
    """Список всех аукционов, добавленных в watch-list текущего пользователя"""
    model = Listing
    template_name = 'auctions/watchlist.html'

    def get_queryset(self):
        w = self.request.user.watchlist
        return w.items.all()


class CreateListing(LoginRequiredMixin, CreateView):
    """View для выставления вещи на аукцион"""
    model = Listing
    fields = ['title', 'description', 'starting_bid', 'image_url',
              'category']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ListingDetail(DetailView):
    """View для просмотра информации по конкретному аукциону"""
    model = Listing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        listing = Listing.objects.get(pk=self.kwargs['pk'])

        if self.request.user == listing.created_by:
            is_author = True
        else:
            is_author = False

        if self.request.user == listing.winner:
            is_winner = True
        else:
            is_winner = False
        
        comments = ListingComment.objects.filter(original_listing=listing).all()

        context['is_winner'] = is_winner
        context['is_author'] = is_author
        context['form'] = ListingCommentForm()
        context['comments'] = comments
        return context


def register(request):
    """View для регистрации нового пользователя"""
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            watchlist = WatchList(owner=user)
            watchlist.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def add_to_watchlist(request, pk):
    """View для добавления аукциона в Watch list пользователя"""
    watchlist = request.user.watchlist
    watchlist.items.add(Listing.objects.get(pk=pk))
    return HttpResponseRedirect(reverse('listing_detail', kwargs={'pk': pk}))


@login_required
def remove_from_watchlist(request, pk):
    """View для удаления аукциона из Watch list пользователя"""
    watchlist = request.user.watchlist
    watchlist.items.remove(Listing.objects.get(pk=pk))
    return HttpResponseRedirect(reverse('listing_detail', kwargs={'pk': pk}))


@login_required
def new_bid(request, pk):
    """View для создания нового предложения цены на аукционе"""
    if request.method == 'POST':
        listing = Listing.objects.get(pk=pk)
        error = ''
        try:
            value = float(request.POST['bid_value'])

            if value <= listing.starting_bid:
                error = 'Your bid should be higher than the starting value!'

            if listing.current_price():
                if value <= listing.current_price():
                    error = 'Your bid should be higher than other bids for this listing!'
        except ValueError:
            error = 'You have to type in a valid number'

        if error:
            request.session['new_bid_error'] = error
        else:
            bid = Bid.objects.create(bidder=request.user,
                                     listing=listing,
                                     value=value)
            bid.save()
        return HttpResponseRedirect(reverse('listing_detail', kwargs={'pk': pk}))
    else:
        return HttpResponseRedirect(reverse('listing_detail', kwargs={'pk': pk}))


@login_required
def close_listing(request, pk):
    """View для закрытия аукциона по вещи"""
    listing = Listing.objects.get(pk=pk)
    listing.active = False
    listing.winner = listing.highest_bidder()
    listing.save()
    return HttpResponseRedirect(reverse('listing_detail', kwargs={'pk': pk}))


@login_required
def make_comment(request, pk):
    """View для создания комментария к аукциону"""
    listing = Listing.objects.get(pk=pk)
    form = ListingCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.original_listing = listing
        comment.author = request.user
        comment.save()
        return HttpResponseRedirect(reverse('listing_detail', kwargs={'pk': pk}))


class ViewCategory(ListView):
    """View для получения списка аукционов по конкретной категории"""
    model = Listing
    template_name = "auctions/view_category.html"

    def get_queryset(self):
        pk = self.kwargs['pk']
        category = ListingCategory.objects.get(pk=pk)
        listings = Listing.objects.filter(active=True).filter(category=category)
        return listings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        category = ListingCategory.objects.get(pk=pk)
        context['category'] = category.name
        return context
