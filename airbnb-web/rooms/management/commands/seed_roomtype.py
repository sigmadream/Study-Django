from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):
    help = "This command creates room type"

    def handle(self, *args, **options):
        room_type = ["Entire place", "Private room", "Shared room"]
        for type in room_type:
            RoomType.objects.create(name=type)
        self.stdout.write(self.style.SUCCESS("Room type created!"))
