from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Count

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken

from .models import Paragraph, WordIndex
from .serializers import ParagraphSerializer,UserSerializer,WordIndexSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime

from .models import User

# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        
        user=User.objects.filter(email=email).first()
        print(user)
        if user is None:
            raise AuthenticationFailed('user not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        
        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'iat':datetime.datetime.utcnow()
            }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)
        
        response.data = {
            'jwt':token
        }
        return response
    
    

@authentication_classes([IsAuthenticated])
@permission_classes([IsAuthenticated])
class ParagraphCreateView(APIView):
    # permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = ParagraphSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([IsAuthenticated])
@permission_classes([IsAuthenticated])
class WordSearchView(APIView):
    def get(self, request, word):
        # Tokenize and convert the search word to lowercase
        search_word = word.lower()
        print("Search Word:", search_word)


        # Search for paragraphs containing the specified word
        paragraphs = (
            Paragraph.objects
            .annotate(word_count=Count('wordindex__word'))
            .filter(wordindex__word__iexact=search_word, word_count__lte=10)
            .distinct()[:10]
        )
        
        print("Search Word:", search_word)
        print("Paragraphs:", paragraphs)

        # Serialize the paragraphs
        serializer = ParagraphSerializer(paragraphs, many=True)

        # Return the serialized paragraphs
        return Response(serializer.data)










