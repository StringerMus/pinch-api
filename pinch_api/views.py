from rest_framework.decorators import api_view
from rest_framework.response import Response


from .settings import REST_AUTH
JWT_AUTH_COOKIE = REST_AUTH['JWT_AUTH_COOKIE']
JWT_AUTH_REFRESH_COOKIE = REST_AUTH['JWT_AUTH_REFRESH_COOKIE']
JWT_AUTH_SAMESITE = REST_AUTH['JWT_AUTH_SAMESITE']
JWT_AUTH_SECURE = REST_AUTH['JWT_AUTH_SECURE']
USER_DETAILS_SERIALIZER = ['pinch_api.serializers.CurrentUserSerializer']


#Email
from rest_framework import status
from django.core.mail import send_mail
from .serializers import EmailSerializer
from django.conf import settings


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to the Pinch API"
    })


@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response


#Email
class SendEmailView(api_view):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                send_mail(
                    subject=data['subject'],
                    message=f"""
                    You have received a new query on Pinch.

                    Sender: {data['name']} ({data['email']})
                    Listing ID: {data['listing_id']}
                    
                    Message:
                    {data['message']}
                    """,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[data['to_email']],
                    fail_silently=False,
                )
                return Response({"success": "Email sent successfully!"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)