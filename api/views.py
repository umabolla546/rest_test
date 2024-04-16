
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from .models import Invoice
from .serializer import InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as error:
            return Response({"error": str(error.detail)}, status=status.HTTP_400_BAD_REQUEST)

