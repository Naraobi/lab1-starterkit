from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import translation

@receiver(user_logged_in)
def set_language_on_login(sender, request, user, **kwargs):
    try:
        # Get the user's first profile
        profile = user.profiles.first()
        if profile:
            lang = profile.default_language
        else:
            lang = 'en'
    except Exception:
        lang = 'en'

    # ✅ Use the correct session key for language
    request.session['django_language'] = lang

    # ✅ Activate the language for the current request
    translation.activate(lang)
    request.LANGUAGE_CODE = lang
