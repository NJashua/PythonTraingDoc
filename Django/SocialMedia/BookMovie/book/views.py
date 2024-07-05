from django.shortcuts import render, redirect
from.models import Movie, Booking, Theater, Show
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Show, Booking, Theater
from .forms import BookingForm, PaymentForm
from django.contrib import messages

@login_required
def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

@login_required
def api_movies(request):
    movies = Movie.objects.all()
    price = request.GET.get('price')
    if price:
        movies = movies.filter(price__lte=price)
    payload = [{'id': movie.id, 'movie_name': movie.movie_name, 'movie_description': movie.movie_description, 'movie_image': movie.movie_image, 'price': movie.price} for movie in movies]
    return JsonResponse(payload, safe=False)

@login_required
def book_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    shows = Show.objects.filter(movie=movie)
    return render(request, 'book_movie.html', {'shows': shows})

@login_required
def book_show(request, show_id):
    show = Show.objects.get(id=show_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.movie = show.movie
            booking.show = show
            booking.save()
            return redirect('payment', booking.id)
    else:
        form = BookingForm()
    return render(request, 'book_show.html', {'form': form, 'show': show})

@login_required
def payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            if payment_method == 'card':
                # process card payment
                pass
            elif payment_method == 'paypal':
                # process paypal payment
                pass
            else:
                messages.error(request, 'Invalid payment method')
                return redirect('payment', booking_id)
            messages.success(request, 'Payment successful!')
            booking.payment_status = True
            booking.save()
            return redirect('home')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form, 'booking': booking})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid username or password')
        return redirect('login')
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')

def custom_logout(request):
    logout(request)
    return redirect('login')