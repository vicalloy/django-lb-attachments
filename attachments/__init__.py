__version__ = '0.8.1'

try:
    from django.conf import settings
    ATTACHMENT_STORAGE_DIR = getattr(settings, 'ATTACHMENT_STORAGE_DIR', 'attachments')
except:
    pass
