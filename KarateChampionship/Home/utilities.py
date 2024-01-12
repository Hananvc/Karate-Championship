import pyotp
from django.core.mail import send_mail


def genarate_otp(email):
    totp = pyotp.TOTP(pyotp.random_base32())
    otp = totp.at(0)

    # Send OTP via email
    send_mail(
        'OTP Verification',
        f'Your OTP is: {otp}',
        'sender@example.com',
        [email],  # Use user.email instead of undefined email variable
        fail_silently=False,
        )
    return otp