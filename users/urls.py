from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView,UserDetail

app_name = "users"

urlpatterns = [
    path("create/", CustomUserCreate.as_view(), name="create_user"),
    path('userdetail/<str:pk>/', UserDetail.as_view(), name='userdetail'),
    path("logout/blacklist/", BlacklistTokenUpdateView.as_view(), name="blacklist"),
]
