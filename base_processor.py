from django.conf import settings

# JS Addin for base-template
# If not-blank, enables various Javascript addons

def js_addins(context):
    base_settings = settings.DJANGO_BASE_TEMPLATE
    
    return {
        'GOOGLE_ANALYTICS': base_settings.get('GOOGLE_ANALYTICS', None),
        'TYPEKIT': base_settings.get('TYPEKIT', None)
    }