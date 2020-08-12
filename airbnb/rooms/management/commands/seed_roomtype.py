from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates room type"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many room do you want to create")

    def handle(self, *args, **options):
        room_types = [
            "Big",
            "Midium",
            "Small"
        ]

        for amenity in room_types:
            RoomType.objects.create(name=amenity)
        self.stdout.write(self.style.SUCCESS("Room type created!"))
