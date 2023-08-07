'''

    In This Python File You Find All Important URLS

'''

# Import path for url
from django.urls import path
# Import necessary views
from .views.views import *
# For Cache
from django.views.decorators.cache import cache_page

# Define URL patterns for different views
urlpatterns = [
    path('', cache_page(60)(IndexListView.as_view()), name='home'),  # Home page view
    path('about', cache_page(60)(AboutListView.as_view()), name='about'),  # About page view
    path('discography', cache_page(60)(DiscographyListView.as_view()), name='discography'),  # Discography page view
    path('tours', cache_page(60)(ToursListView.as_view()), name='tours'),  # Tours page view
    path('videos', cache_page(60)(VideosListView.as_view()), name='videos'),  # Videos page view
    path('blog', cache_page(60)(BlogListView.as_view()), name='blog'),  # Blog page view
    path('blog/detail/<int:pk>/', cache_page(60)(BlogDetailsView.as_view()), name='blog-detail-detail'),  # Blog detail page view
    path('terms', cache_page(60)(PrivacyPolicyListView.as_view()), name='privacy_policy'),  # Privacy Policy page view
    path('contact', cache_page(60)(ContactListView.as_view()), name='contact'),  # Contact page view
    path('post/ajax/message', ContactMessageCreateView.as_view(), name="post_message"),  # AJAX view for sending messages
    path('post/ajax/newsletter', NewsletterCreateView.as_view(), name='post_newsletter'),  # AJAX view for subscribing to newsletters
]
