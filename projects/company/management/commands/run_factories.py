from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from projects.charge.models import Vehicle, Charge
from projects.company.models import Company


class Command(BaseCommand):
    help = "Runs factories to provide initial data"

    def handle(self, *args, **options):
        User.objects.create_user("super")
        company = Company(
            name="Fake company"
        )
        vehicle = Vehicle(
            vehicle_type="Mercedes Ex",
            battery_percentage=50,
            company=company,
        )
        Vehicle(
            vehicle_type="Toyota Green",
            battery_percentage=20,
            company=company,
        )
        Charge(
            start_time=timezone.now() + timedelta(hours=1),
            expected_end_time=timezone.now() + timedelta(hours=2),
            estimated_battery_increase_percentage=20,
            vehicle=vehicle,
            status="created",
        )
