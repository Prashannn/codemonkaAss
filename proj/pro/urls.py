# urls.py
from django.urls import path
from .views import LoginView,WordSearchView,RegisterView,ParagraphCreateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('paragraph/', ParagraphCreateView.as_view(), name='create_paragraph'),

    # path('paragraphs/', ParagraphListView.as_view(), name='paragraph-list'),
    path('wordindex/<str:word>/', WordSearchView.as_view(), name='wordindex-list'),
]























































# from django.urls import path
# from .views import RegisterView,LoginView, CreateParagraphView, SearchParagraphsView

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='login'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('create-paragraph/', CreateParagraphView.as_view(), name='create-paragraph'),
#     path('search/<str:word>/', SearchParagraphsView.as_view(), name='search-paragraphs'),
# ]