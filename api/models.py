from django.db import models

# Create your models here.
class Invoice(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    invoice_number=models.IntegerField(unique=True)
    CustomerName=models.CharField(max_length=25)
    BillingAddress=models.TextField()
    ShippingAddress=models.TextField()
    GSTIN=models.CharField(max_length=20)
    TotalAmount=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self) -> str:
        return f"Invoice{self.invoice_number}"

class InvoiceItem(models.Model):
    invoice=models.ForeignKey(Invoice,related_name="invoice_item",on_delete=models.CASCADE)
    itemName=models.CharField(max_length=250)
    Quantity=models.DecimalField(max_digits=10,decimal_places=2)
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    Amount=models.DecimalField(max_digits=10,decimal_places=2)


class BillSundry(models.Model):
    invoice=models.ForeignKey(Invoice,related_name="bill_sundry",on_delete=models.CASCADE)
    bill_sundry_name=models.CharField(max_length=250)
    amount=models.DecimalField(max_digits=10,decimal_places=2)

