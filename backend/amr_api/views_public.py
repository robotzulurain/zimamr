from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LabResult
import csv
from io import StringIO

class UploadCSVView(APIView):
    """
    API endpoint to upload CSV data for LabResult.
    """
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        
        decoded_file = file.read().decode('utf-8')
        io_string = StringIO(decoded_file)
        reader = csv.DictReader(io_string)
        
        for row in reader:
            LabResult.objects.create(
                patient_id=row.get('patient_id'),
                sample_date=row.get('sample_date'),
                organism=row.get('organism'),
                antibiotic=row.get('antibiotic'),
                result=row.get('result')
            )
        return Response({'message': 'CSV uploaded successfully'}, status=status.HTTP_201_CREATED)
