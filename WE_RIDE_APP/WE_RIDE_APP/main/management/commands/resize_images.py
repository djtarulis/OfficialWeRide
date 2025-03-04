from django.core.management.base import BaseCommand
from main.models import Photo  # Import your EventPhoto model
from PIL import Image
import os

class Command(BaseCommand):
    help = 'Resize all uploaded event images to a max size'

    def handle(self, *args, **kwargs):
        max_size = (800, 600)  # Maximum width and height

        photos = Photo.objects.all()
        if not photos:
            self.stdout.write(self.style.WARNING("No images found to resize."))
            return

        for photo in photos:
            image_path = photo.image.path  # Get full file path

            if not os.path.exists(image_path):
                self.stdout.write(self.style.ERROR(f"File not found: {image_path}"))
                continue

            try:
                img = Image.open(image_path)
                img.thumbnail(max_size)  # Resize the image
                img.save(image_path)  # Overwrite the existing image

                self.stdout.write(self.style.SUCCESS(f"Resized: {photo.title} ({image_path})"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to resize {photo.title}: {e}"))
