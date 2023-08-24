from django.db import models
from django.utils import timezone

from projects.company.models import Company


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    battery_percentage = models.IntegerField(null=True, blank=False)
    user = models.CharField(max_length=50)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user} {self.vehicle_type}"


    def next_charge(self):
        return Charge.objects.get(status="Created", vehicle=self)

    def plug_in(self):
        Charge.objects.create(
            status="Created",
            start_time=timezone.now(),
            expected_end_time=timezone.now(),
            vehicle=self,
        )

    def plug_remove(self):
        charge = self.charge
        charge.end_time = timezone.now()
        charge.status = "Cancelled"
        charge.save()

    @property
    def charge(self):
        return Charge.objects.get(status__in=["created", "charging"], vehicle=self)


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
    # we could do this with Kwh but I assume the user will want it in a percentage
    estimated_battery_increase_percentage = models.IntegerField(null=True, blank=False)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50, choices=CHARGE_STATUS)

    # Other possible fields

    # foreign key to schedule so you know if it has been created automatically
    # extra statuses e.g. saying what user cancelled a charge/overwrote a charge
    # when the charge was created

    def __str__(self):
        if self.vehicle:
            return f"{self.vehicle.user} {self.vehicle.vehicle_type} - {self.status}"

# class Schedule(models.Model):
    # company or vehicle
    # status
    # start time
    # duration