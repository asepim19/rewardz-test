from rest_framework import viewsets, status
from .serializers import BooksSerializer, HistoryBorrowSerializer, HistoryRenewSerializer, HistoryReturnSerializer, HistorySerializer
from .models import BooksModels, BooksCopyModels, HistoryModels
from rest_framework.response import Response

class LibraryViewset(viewsets.ModelViewSet):

    # PUBLIC SEARCH
    def search(self, request):
        response = {
            'success':False,
            'message': "Something Wrong !",
            'data':{}
        }
        keyword = self.request.query_params.get("keyword", "")
        book = BooksModels.objects.get(name=keyword)
        ignored = HistoryModels.objects.filter(book_id=book._id).values_list('copy_id', flat=True).order_by('-return_date')
        countCopy = BooksCopyModels.objects.all().exclude(_id__in=ignored).filter(book_id=book._id).count()
        if countCopy :
            response["success"] = True
            response["message"] = "Success Get Book Data"
            response["data"] = BooksSerializer(book).data
            response["data"]["count_copy"] = countCopy
        else :
            available = HistoryModels.objects.filter(book_id=book._id).order_by('-return_date')
            response["success"] = True
            response["message"] = "Success Get Book Data, But Not Enought copy for you."
            response["data"]['available_date'] = available[0].return_date

        return Response(response)

    # STUDENT
    def student_login(self, request):
        queryset = BooksModels.objects.all().filter(status='ACTIVE').order_by('order')
        serializer = BooksSerializer(queryset, many=True)
        return Response(serializer.data)

    def student_borrow(self, request):
        response = {
            'success':False,
            'message': "Something Wrong !",
            'data':{}
        }
        serializer = HistoryBorrowSerializer(data=request.data)
        validation = serializer.is_valid()

        if not validation:
            response['message'] = "Data Validation Failed"
            response['data'] = serializer.errors
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        check = HistoryModels.objects.all().filter(
            book_id=request.data['book_id'],
            copy_id=request.data['copy_id'],
            user_id=request.data['user_id'],
        ).count()
        if check :
            response['message'] = "User Already Borrowed This Book"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response['success'] = True
        response['message'] = "Success Borrow Book"
        response['data'] = serializer.data
        return Response(response)

    def student_refresh(self, request):
        response = {
            'success':False,
            'message': "Something Wrong !",
            'data':{}
        }

        serializer = HistoryRenewSerializer(data=request.data)
        validation = serializer.is_valid()

        if not validation:
            response['message'] = "Data Validation Failed"
            response['data'] = serializer.errors
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        check = HistoryModels.objects.all().filter(
            book_id=request.data['book_id'],
            copy_id=request.data['copy_id'],
            user_id=request.data['user_id'],
        ).count()
        if not check :
            response['message'] = "User Data Not Found For This Book"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response['success'] = True
        response['message'] = "Success Refresh Book"
        response['data'] = serializer.data
        return Response(response)

    # LIBRARIAN
    def librarian_login(self, request):
        queryset = BooksModels.objects.all().filter(status='ACTIVE').order_by('order')
        serializer = BooksSerializer(queryset, many=True)
        return Response(serializer.data)

    def librarian_borrow(self, request):
        response = {
            'success':False,
            'message': "Something Wrong !",
            'data':{}
        }
        serializer = HistoryBorrowSerializer(data=request.data)
        validation = serializer.is_valid()

        if not validation:
            response['message'] = "Data Validation Failed"
            response['data'] = serializer.errors
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        check = HistoryModels.objects.all().filter(
            book_id=request.data['book_id'],
            copy_id=request.data['copy_id'],
            user_id=request.data['user_id'],
        ).count()
        if check :
            response['message'] = "User Already Borrowed This Book"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response['success'] = True
        response['message'] = "Success Borrow Book"
        response['data'] = serializer.data
        return Response(response)

    def librarian_returned(self, request):
        response = {
            'success':False,
            'message': "Something Wrong !",
            'data':{}
        }
        serializer = HistoryReturnSerializer(data=request.data)
        validation = serializer.is_valid()

        if not validation:
            response['message'] = "Data Validation Failed"
            response['data'] = serializer.errors
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        check = HistoryModels.objects.all().filter(
            book_id=request.data['book_id'],
            copy_id=request.data['copy_id'],
            user_id=request.data['user_id'],
        ).count()
        if not check :
            response['message'] = "No User Data Borrowed This Book"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response['success'] = True
        response['message'] = "Success Return Book"
        response['data'] = serializer.data
        return Response(response)

    def librarian_history(self, request):
        response = {
            'success':False,
            'message': "Something Wrong !",
            'data':{}
        }

        queryset = HistoryModels.objects.all().order_by('created_at')
        serializer = HistorySerializer(queryset, many=True)
        print(serializer.data)
        response['success'] = True
        response['message'] = "Success Get History Data"
        response['data'] = serializer.data
        return Response(response)
