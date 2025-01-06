from PIL import Image
import os
from django.conf import settings
from django.core.exceptions import ValidationError


class FileValidationService:

    @classmethod
    def validate_pdf(cls, file):
        if not file.name.endswith('.pdf'):
            raise ValidationError('Загрузите файл в формате PDF.')



class ImageService:

    @classmethod
    def convert_to_webp(cls, instance, field_name, remove_original=True):
        image_field = getattr(instance, field_name)

        if not image_field or not image_field.name:
            return

        img_path = image_field.path
        if not os.path.exists(img_path):
            return

        if img_path.lower().endswith('.webp'):
            return

        webp_path = os.path.splitext(img_path)[0] + '.webp'

        with Image.open(img_path) as img:
            img.save(webp_path, 'WEBP')

        if remove_original:
            os.remove(img_path)

        relative_webp_path = os.path.relpath(webp_path, settings.MEDIA_ROOT)
        setattr(instance, field_name, relative_webp_path)
        instance.save(update_fields=[field_name])


class TranslatorMediaMixin:
    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


def validate_image_min_dimensions(image):
    min_width = 1200  # Минимальная ширина в пикселях
    min_height = 800  # Минимальная высота в пикселях

    with Image.open(image) as img:
        if img.width < min_width or img.height < min_height:
            raise ValidationError(
                f"Размер изображения должен быть не менее {min_width}x{min_height} пикселей."
            )