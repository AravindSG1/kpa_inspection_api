from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

class WheelSpecificationView(APIView):
    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": serializer.data["formNumber"],
                    "submittedBy": serializer.data["submittedBy"],
                    "submittedDate": serializer.data["submittedDate"],
                    "status": "Saved"
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        form_number = request.query_params.get('formNumber')
        submitted_by = request.query_params.get('submittedBy')
        submitted_date = request.query_params.get('submittedDate')

        filters = {}
        if form_number:
            filters['formNumber'] = form_number
        if submitted_by:
            filters['submittedBy'] = submitted_by
        if submitted_date:
            filters['submittedDate'] = submitted_date

        queryset = WheelSpecification.objects.filter(**filters)

        if not queryset.exists():
            return Response({
                "success": True,
                "message": "No matching wheel specification forms found for the given filters.",
                "data": []
            }, status=status.HTTP_200_OK)

        serializer = WheelSpecificationSerializer(queryset, many=True)

        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
