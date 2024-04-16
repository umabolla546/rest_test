
from rest_framework import serializers
from .models import InvoiceItem, BillSundry, Invoice

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = "__all__"

    def validate(self, data):
        if data['Quantity'] * data['Price'] != data['Amount']:
            raise serializers.ValidationError("Amount must equal Quantity * Price")
        return data

class BillSundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BillSundry
        fields = "__all__"
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        return value

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_item = InvoiceItemSerializer(many=True)
    bill_sundry = BillSundrySerializer(many=True)

    class Meta:
        model = Invoice
        fields = "__all__"
    
    def validate(self, data):
        calculated_invoice_item_total = sum(item['Amount'] for item in data['invoice_item'])
        calculated_bill_sundry_total = sum(sun['Amount'] for sun in data['bill_sundry'])

        if data['TotalAmount'] != calculated_invoice_item_total + calculated_bill_sundry_total:
            raise serializers.ValidationError("Total amount does not match sum of invoice items and bill sundries")
        
        return data
