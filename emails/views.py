from rest_framework import status
from django.core.mail import send_mail
from .serializers import EmailSerializer
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

@csrf_exempt
@api_view(['POST'])
def send_email_view(request):
    print(f"Email data: {serializer.validated_data}")
    response = JsonResponse({"success": "CORS test passed!"})
    response["Access-Control-Allow-Origin"] = "https://pinch-5e6e24dd12fc.herokuapp.com"
    response["Access-Control-Allow-Credentials"] = "true"
    return response
    # serializer = EmailSerializer(data=request.data)
    # if serializer.is_valid():
    #     data = serializer.validated_data
    #     try:
    #         send_mail(
    #             subject=data['subject'],
    #             message=f"""
    #             You have received a new query on Pinch.

    #             Sender: {data['name']} ({data['email']})
    #             Listing ID: {data['listing_id']}
                
    #             Message:
    #             {data['message']}
    #             """,
    #             from_email=settings.DEFAULT_FROM_EMAIL,
    #             recipient_list=[data['to_email']],
    #             fail_silently=False,
    #         )
    #         return Response({"success": "Email sent successfully!"}, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)