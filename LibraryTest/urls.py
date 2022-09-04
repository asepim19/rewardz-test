"""LibraryTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from library.views import LibraryViewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/search', LibraryViewset.as_view({'get':'search'}), name='search-book'),
    path('api/student/borrow', LibraryViewset.as_view({'post': 'student_borrow'}), name='student-borrow'),
    path('api/student/renew', LibraryViewset.as_view({'put': 'student_refresh'}), name='student-refresh'),
    path('api/librarian/borrow', LibraryViewset.as_view({'post': 'librarian_borrow'}), name='librarian-borrow'),
    path('api/librarian/returned', LibraryViewset.as_view({'put': 'librarian_returned'}), name='librarian-returned'),
    path('api/librarian/history', LibraryViewset.as_view({'get': 'librarian_history'}), name='librarian-history'),
]
