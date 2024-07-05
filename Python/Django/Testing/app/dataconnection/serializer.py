from django.contrib import admin
from rest_framework import serializers
import models

class Task(serializers.ModelSerializer):
    title = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    image = serializers.CharField()
    discount_price = serializers.IntegerField()
    rating = serializers.FloatField()

    class Meta:
        model = Task
        fields = ['id','title', 'price', 'description', 'image', 'discount_price', 'rating']

        def get_short_description(self, obj):
            return obj.description[:50]ā