from .models import Cook,Customer
from rest_framework import serializers

class CookSerializer(serializers.ModelSerializer):
  class Meta:
      model = Cook
      fields =  (
            "id",
            "cookName",
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
            "date_added",
            "cook",
            "id"
        )

  