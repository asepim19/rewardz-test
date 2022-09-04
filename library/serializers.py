from rest_framework import serializers
from library.models import StudentModels, LibrarianModels, BooksModels, BooksCopyModels, HistoryModels

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModels
        fields = '__all__'

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrarianModels
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModels
        fields = ['_id', 'code', 'name']

class BooksCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksCopyModels
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryModels
        fields = '__all__'

class HistoryBorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryModels
        fields = ['book_id', 'copy_id','user_id']

class HistoryRenewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryModels
        fields = ['book_id', 'copy_id','user_id', 'renew_date']

class HistoryReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryModels
        fields = ['book_id', 'copy_id','user_id', 'return_date']