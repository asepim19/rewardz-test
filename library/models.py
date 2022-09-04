from django.db import models
from datetime import datetime, timedelta
import uuid

class StudentModels(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(blank=True, null=True)

    class Meta:
        db_table = 'tb_student'

class LibrarianModels(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(blank=True, null=True)

    class Meta:
        db_table = 'tb_librarian'

class BooksModels(models.Model):
    _id = models.UUIDField(primary_key = True, default=uuid.uuid4)
    code = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(blank=True, null=True)

    class Meta:
        db_table = 'tb_books'

class BooksCopyModels(models.Model):
    _id = models.UUIDField(primary_key = True, default=uuid.uuid4)
    book_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(blank=True, null=True)

    class Meta:
        db_table = 'tb_books_copy'

class HistoryModels(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book_id = models.UUIDField()
    user_id = models.UUIDField()
    copy_id = models.UUIDField()
    borrow_date = models.DateTimeField(auto_now_add=True)
    renew_date = models.DateTimeField(null=True)
    return_date = models.DateTimeField(null=False, default=datetime.now()+timedelta(days=30))
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(blank=True, null=True)

    class Meta:
        db_table = 'tb_history'