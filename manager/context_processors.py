from contact_us.models import ContactUs
from .models import BackgroundImagesForPages
from contact_us.models import ContactInfoLeft, Sources, MediaLinks


def background_images_for_pages(request):

    data = {
        'bg_photo': BackgroundImagesForPages.objects.all(),
        'session': request.path,
        'applications': ContactUs.objects.filter(is_processed=False),
        'infos': ContactInfoLeft.objects.all(),
        'sources': Sources.objects.all(),
        'media_links_blocks': MediaLinks.objects.all()
    }

    return data
