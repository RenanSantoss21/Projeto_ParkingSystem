from rest_framework import serializers
from customers.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'
        #fields = ['id', 'name', 'email', 'phone'] #outra forma de definir os campos a serem serializados