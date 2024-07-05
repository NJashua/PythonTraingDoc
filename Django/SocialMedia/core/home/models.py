from django.db import models
from django.contrib.auth.models import User
import uuid
 
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
     
    class Meta:
        abstract = True
         
class MovieCategory(BaseModel):
    category_name = models.CharField(max_length=100)
     
class Movie(BaseModel):
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE, related_name="pizzas")
    movie_name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    images = models.CharField(max_length=500)
     
class Cart(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="carts")
    is_paid = models.BooleanField(default=False)
     
class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=50)  # Add payment mode field
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username} on {self.timestamp} via {self.payment_mode}"