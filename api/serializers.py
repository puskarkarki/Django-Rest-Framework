from rest_framework import serializers 
from res_tutorials.models import Books

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = ('title', 'subtitle', 'author', 'isbn')
    
    