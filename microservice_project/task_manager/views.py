from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from task_manager.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_user(request):
    # Реализация регистрации пользователей

    # Получаем данные из запроса
    serializer = UserSerializer(data=request.data)

    # Проверяем, что данные валидны
    if serializer.is_valid():
        # Создаем нового пользователя
        user = serializer.save()

        # Создаем или обновляем токен для пользователя
        token, created = Token.objects.get_or_create(user=user)

        # Возвращаем успешный ответ с данными пользователя и токеном
        return Response({
            'message': 'User registered successfully!',
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

    # Если данные не валидны, возвращаем ошибку с сообщениями об ошибках
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def authenticate_user(request):
    # Реализация аутентификации пользователей

    # Получаем данные из запроса
    username = request.data.get('username')
    password = request.data.get('password')

    # Проверяем, что переданы оба значения
    if not username or not password:
        return Response({'message': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Пытаемся аутентифицировать пользователя
    user = User.objects.filter(username=username).first()

    if user is None or not user.check_password(password):
        return Response({'message': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)

    # Создаем или обновляем токен для пользователя
    token, created = Token.objects.get_or_create(user=user)

    # Возвращаем успешный ответ с данными пользователя и токеном
    return Response({
        'message': 'User authenticated successfully!',
        'user': UserSerializer(user).data,
        'token': token.key
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_list(request):
    # Преобразование users в JSON и возврат в Response
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


