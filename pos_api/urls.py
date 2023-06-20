from .views import PostList,  PostListDetailfilter, CreatePost
from django.urls import path

app_name = 'pos_api'

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
]

# http://127.0.0.1:8000/api #for all user data
# http://127.0.0.1:8000/api/post/your <slug:some word>/ #fro get one user data
# http://127.0.0.1:8000/api/admin/create/ #for post
# http://127.0.0.1:8000/api/toke/ # for login
# http://127.0.0.1:8000/api/user/create # for signup
# http://127.0.0.1:8000/api/logout/blacklist/ # for logout
# word_count = models.PositiveIntegerField(default=0, blank=True) # add this to base/model.py file
# class PostSerializer(serializers.ModelSerializer):
#     full_name = serializers.CharField(source='author.full_name', read_only=True)
#     email = serializers.EmailField(source='author.email', read_only=True)
#     word_count = serializers.IntegerField(read_only=True)

#     class Meta:
#         model = Post
#         fields = ('id', 'audio', 'excerpt', 'content', 'author','','slug' ,'full_name', 'email', 'word_count') # add slug field to pos_api/serializeers.py