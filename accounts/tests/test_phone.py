import email
from os import access
from urllib import response
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import PhoneModel  # Update with the correct import
from django.core import mail
from django.contrib.auth import get_user_model
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC, EmailAddress

from accounts.tests.test_user import AccessTokenTest, UserTest 
User=get_user_model()


class GetPhoneNumberRegisteredTimeBasedTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.phone_number = "1234567890"  # Replace with a phone number you want to use
        user = User.objects.create_user(username='testuser',email='test@example.com', password='testpassword')

        self.client.force_authenticate(user=user)

    def test_get_request_creates_PhoneModel_if_not_exists(self):
      
        response = self.client.get(reverse('OTP_Gen', args=[self.phone_number]))
       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(PhoneModel.objects.filter(Mobile=self.phone_number).exists())

    def test_get_request_returns_otp(self):
        response = self.client.get(reverse('OTP_Gen', args=[self.phone_number]))
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("OTP" , response.data)

    def test_post_request_with_valid_otp(self):
        response = self.client.get(reverse('OTP_Gen', args=[self.phone_number]))
        otp=response.data["OTP"]
        response = self.client.post(reverse('OTP_Gen', args=[self.phone_number]), {"otp": otp})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mobile = PhoneModel.objects.get(Mobile=self.phone_number)
        self.assertTrue(mobile.isVerified)
    # def test_post_request_with_valid_otp(self):
    #     self.client.get(reverse('OTP_Gen', args=[self.phone_number]))
    #     idx=mail.outbox[0].body.find('Your OTP is:')
    #     otp=mail.outbox[0].body[idx:]
    #     response = self.client.post(reverse('OTP_Gen', args=[self.phone_number]), {"otp": otp})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_request_with_invalid_otp(self):
        PhoneModel.objects.create(Mobile=self.phone_number)
        otp = "000000"  # Replace with an invalid OTP
        response = self.client.post(reverse('OTP_Gen', args=[self.phone_number]), {"otp": otp})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_nonexistent_phone_number(self):
        response = self.client.post(reverse('OTP_Gen', args=["nonexistent_number"]), {"otp": "123456"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_request_with_verified_user(self):
        PhoneModel.objects.create(Mobile=self.phone_number, isVerified=True)
        otp = "123456"  # Replace with a valid OTP
        response = self.client.post(reverse('OTP_Gen', args=[self.phone_number]), {"otp": otp})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# # Ensure to update the URL name ('OTP_Gen') in the reverse calls.
