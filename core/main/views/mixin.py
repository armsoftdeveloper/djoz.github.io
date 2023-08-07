# Import necessary models and forms
from ..models import *
from ..forms.forms import NewsletterForm

# Predefined menu items for navigation
menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Discography', 'url_name': 'discography'},
    {'title': 'Tours', 'url_name': 'tours'},
    {'title': 'Videos', 'url_name': 'videos'},
    {'title': 'Blog', 'url_name': 'blog'},
    {'title': 'Contact', 'url_name': 'contact'},
]

# DataMixin provides common context data used across views.
class DataMixin:
    def get_user_context(self, **kwargs):
        # Create a dictionary to store the context data
        context = kwargs
        
        # Add the predefined menu to the context
        context['menu'] = menu

        # Fetch and add the static information to the context
        context['static_info'] = StaticInfo.objects.get()

        # Create and add the NewsletterForm instance to the context
        context['formNewsletter'] = NewsletterForm()

        # Return the updated context with common data
        return context
