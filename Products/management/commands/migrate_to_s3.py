# your_app/management/commands/migrate_to_s3.py

import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files.storage import default_storage
from Products.models import Menu  # import your models

class Command(BaseCommand):
    help = 'Migrate media files from local storage to S3'

    def handle(self, *args, **kwargs):
        media_root = settings.MEDIA_ROOT

        for image in Menu.objects.all():
            local_file_path = os.path.join(media_root, image.image.name)
            if os.path.exists(local_file_path):
                with open(local_file_path, 'rb') as file_data:
                    image.image.save(image.image.name, file_data)
                    image.save()
                    self.stdout.write(f'Successfully uploaded {image.image.name} to S3')
            else:
                self.stdout.write(f'File {local_file_path} does not exist')
