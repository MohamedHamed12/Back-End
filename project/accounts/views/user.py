# -*- coding: utf-8 -*-
import base64
from datetime import datetime

from accounts.filters import *
from accounts.models import *
from accounts.models import CustomUser
from accounts.permissions import *
from accounts.serializers import *
from accounts.serializers import CustomUserSerializer
from accounts.utils import *
from django.core.exceptions import ObjectDoesNotExist
from orders.pagination import CustomPagination
# views.py
from rest_framework import status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .views import *

# -*- coding: utf-8 -*-



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class=CustomPagination
    permission_classes=[IsAuthenticated,IsAdminOrIsSelf]


class OtpByEmailView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = OtpByEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = OtpByEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]

            try:
                user = User.objects.filter(email=email).order_by('-created_at').first()
            except User.DoesNotExist:
                return Response(
                    {"detail": "Invalid Email"}, status=status.HTTP_400_BAD_REQUEST
                )
            if not user:
                return Response(
                    {"detail": "Invalid Email"}, status=status.HTTP_400_BAD_REQUEST
                )


            SendEmail.send_otp(user)
            return Response(
                {"detail": "OTP sent to your email"}, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailOtpView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyEmailOtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = VerifyEmailOtpSerializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data["otp"]

            user = Otp.verify_otp(otp)
            if not user:
                return Response(
                    {"detail": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST
                )

            refresh = RefreshToken.for_user(user)

            data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": CustomUserSerializer(user).data,
                # "user_type":user.user_type,
                "profile_id":POSITIONS[user.user_type].objects.get(user=user).id

                # "profile": PatientSerializer(user.profile).data,
            }

            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class VerifyMobileOTP(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VerifyMobileOtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = VerifyMobileOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone"]
        otp = serializer.validated_data["otp"]
        try:
            Mobile = PhoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.TOTP(key, interval=EXPIRY_TIME)  # TOTP Model
        if OTP.verify(otp):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.user = request.user
            Mobile.save()
            return Response("OTP Verified", status=200)

        return Response("OTP is wrong/expired", status=400)


# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return (
            str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"
        )


# Time after which OTP will expire
EXPIRY_TIME = 120  # seconds



class PhoneRegister(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PhoneRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = PhoneRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone"]
        try:
            Mobile = PhoneModel.objects.get(
                Mobile=phone
            )  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            PhoneModel.objects.create(
                Mobile=phone,
            )
            Mobile = PhoneModel.objects.get(Mobile=phone)  # user Newly created Model
        Mobile.user = request.user
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.TOTP(key, interval=EXPIRY_TIME)  # TOTP Model for OTP is created
        # send_otp_via_email(request, OTP.now())
        response_data = {
            "message": "OTP  sent to the mobile number ",
            "OTP": OTP.now(),
        }

        return Response(response_data, status=status.HTTP_200_OK)
