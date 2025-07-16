# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import AllowAny
# from rest_framework import status
# from .serializers import regserialiser,logserialiser,CustomUserSerializer
# from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated
# from .models import CustomUser

# class register(APIView):
#     def post(self,request):
#         k=request.data
#         ser=regserialiser(data=k)
#         if ser.is_valid():
#             ser.save()
#             return Response({"message":"User created"},status=status.HTTP_201_CREATED)
#         return Response(ser.errors)


# class logg(APIView):
#     permission_classes=[AllowAny]
#     def post(self,request):
#         print("im login view=============")
#         k=request.data
#         ser=logserialiser(data=k)
#         if not ser.is_valid():
#             return Response(ser.errors)
#         user=authenticate(
#             email=ser.validated_data['email'],
#             password=ser.validated_data['password']
#         )
        
#         if user is None:
#             return Response("user not exist")
#         if user.is_blocked:                                              
#             return Response("Your account has been blocked by the admin.")       
#         refresh = RefreshToken.for_user(user)
#         USER=CustomUser.objects.get(email=user)
#         print("user==",USER.is_admin)
#         return Response({
#             'access_token': str(refresh.access_token),
#             'refresh_token': str(refresh),
#             'admin':user.is_admin,
#         }, status=200)        
    

# class SelfUserView(APIView):
#     permission_classes=[IsAuthenticated]
#     def get (self,request):
#         user=CustomUser.objects.get(email=request.user) 
#         ser=CustomUserSerializer(user)
#         return Response(ser.data) 










from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .serializers import regserialiser, logserialiser, CustomUserSerializer
from .models import CustomUser


class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        ser = regserialiser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        ser = logserialiser(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            email=ser.validated_data['email'],
            password=ser.validated_data['password']
        )

        if user is None:
            return Response({"message": "Invalid email or password"}, status=status.HTTP_404_NOT_FOUND)

        if user.is_blocked:
            return Response({"message": "Your account has been blocked by the admin."}, status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(user)

        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'admin': user.is_admin,
        }, status=status.HTTP_200_OK)


class SelfUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = CustomUser.objects.get(email=request.user.email)
        except CustomUser.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        ser = CustomUserSerializer(user)
        return Response(ser.data, status=status.HTTP_200_OK)
