from django.db import models

from projects.company.models import Company


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)

    def next_charge(self):
        return Charge.objects.get(status="Created", vehicle=self)

    def plug_in(self):
        Charge(
            status="Created",
            start_time=timezone.now(),
            expected_end_time=timezone.now(),
            vehicle=self,
        )

    def plug_remove(self):
        charge = Charge.objects.get(status__in=["Created", "Charging"], vehicle=self)
        charge.end_time = timezone.now()
        charge.status = "Cancelled"
        charge.save()

    def __str__(self):
        return f"{self.vehicle.user} {self.vehicle.vehicle_type}"


class Charge(models.Model):
    CHARGE_STATUS = (
        ("created", "Created"),
        ("cancelled", "Cancelled"),
        ("charging", "Charging"),
        ("complete", "Complete"),
    )

    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    expected_end_time = models.DateTimeField(null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50, choices=CHARGE_STATUS)

    # Other possible fields

    # extra statuses e.g. saying what user cancelled a charge/overwrote a charge
    # when the charge was created

    def __str__(self):
        if self.vehicle:
            return f"{self.vehicle.user} {self.vehicle.vehicle_type} - {self.status}"