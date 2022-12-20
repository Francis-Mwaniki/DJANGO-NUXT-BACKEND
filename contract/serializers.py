from .models import Cook,Customer
from rest_framework import serializers

class CookSerializer(serializers.ModelSerializer):
  class Meta:
      model = Cook
      fields =  (
            "id",
            "cookName",
            "host",
            "quote",
            "description",
            "recipeName",
            "get_image",
            "get_thumbnail",
            "date_added"
        )

  
class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
      model = Customer
      fields =  (
            "customername",
            "comments",
            "rating",
            "user",
            "date_added",
            "cook",
            "id"
        )

  