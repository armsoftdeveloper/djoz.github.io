'''

    In This Python File You Find All Important Models

'''

# For models work
from django.db import models
# This Module Is Install Use pip install django-phonenumber-field and pip install django-phonenumbers
from phonenumber_field.modelfields import PhoneNumberField
# For Get Absolute Url
from django.urls import reverse

# Model to store static information for the website
class StaticInfo(models.Model):
    logo = models.ImageField(("Upload Background Image"), upload_to="media/%Y-%m-%d")
    phone = PhoneNumberField(("Set Phone Number"))
    email = models.EmailField(("Set Email"), max_length=254)
    address = models.CharField(("Set Address"), max_length=50)
    facebook_url = models.URLField(("Set Facebook Url"), max_length=200, blank=True)
    twitter_url = models.CharField(("Set Twitter Url"), max_length=50, blank=True)
    instagram_url = models.CharField(("Set Instagram Url"), help_text="If You Have Any More Social Accounts And Want To Add Your Webpage, Please Contact With Page Creator Company.", max_length=50, blank=True)

    def __str__(self):
        return "Page Control"
    
    class Meta:
        verbose_name = "Page Information"
        verbose_name_plural = "Page Information"

# Model to store main content for the website's homepage
class Main(models.Model):
    title = models.CharField(("Set Title"), max_length=50)
    sub_title = models.CharField(("Set Sub Title"), max_length=50)
    description = models.TextField(("Set Description"))
    img = models.ImageField(("Upload Background Image"), upload_to="media/%Y-%m-%d")
    url = models.URLField(("Set Video Url"), max_length=200)
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return "Main Control"
    
    class Meta:
        verbose_name = "Main"
        verbose_name_plural = "Main"

# Model to store upcoming events for the website's slider
class UpcomingEvents(models.Model):
    img = models.ImageField(("Upload Slider Image"), upload_to="media/%Y-%m-%d")
    date = models.DateField(("Set Date"))
    title = models.CharField(("Set Title"), max_length=50)
    location = models.CharField(("Set Location"), max_length=50)
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']
        verbose_name = "Upcoming Events Slider"
        verbose_name_plural = "Upcoming Events Slider"

# Model to store information about the website's "About" section
class AboutSpad(models.Model):
    img = models.ImageField(("Upload Image"), upload_to="media/%Y-%m-%d")
    title = models.CharField(("Set Title"), max_length=50)
    description = models.TextField(("Set Description"))
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return "About Spad Control"
    
    class Meta:
        verbose_name = "About Spad"
        verbose_name_plural = "About Spad"

# Model to store services information for the website
class Services(models.Model):
    img = models.ImageField(("Upload Image"), upload_to="media/%Y-%m-%d")
    title = models.CharField(("Set Title"), max_length=50)
    description = models.TextField(("Set Description"))
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']
        verbose_name = "Service"
        verbose_name_plural = "Services"

# Model to store audio tracks for the website
class Tracks(models.Model):
    title = models.CharField(("Set Track Title"), max_length=50)
    track = models.FileField(("Upload Audio"), upload_to="files/%Y-%m-%d")
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return f"{self.title} , {self.track}"

    class Meta:
        ordering = ['id']
        verbose_name = "Track"
        verbose_name_plural = "Tracks"

# Model to store YouTube feed information for the website
class YoutubeFeed(models.Model):
    title = models.CharField(("Set Title"), max_length=50)
    url = models.URLField(("Set Url"), max_length=200)
    img = models.ImageField(("Upload Image"), upload_to="media/%Y-%m-%d")
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']
        verbose_name = "Youtube Feed"
        verbose_name_plural = "Youtube Feed"

# Model to store ticket section information for the website
class TicketSection(models.Model):
    title = models.CharField(("Set Title"), max_length=50)
    subtitle = models.CharField(("Set Subtitle"), max_length=50)
    img = models.ImageField(("Upload Background Image"), upload_to="media/%Y-%m-%d")
    days_left = models.IntegerField(("Set Days"), blank=True)
    hours_left = models.IntegerField(("Set Hours"), blank=True)
    minutes_left = models.IntegerField(("Set Minutes"), blank=True)
    seconds_left = models.IntegerField(("Set Seconds"), blank=True)
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return "Ticket Section Control"
    
    class Meta:
        verbose_name = "Ticket Section"
        verbose_name_plural = "Ticket Section"

# Model to store skills information for the website
class Skills(models.Model):
    title = models.CharField(("Set Title"), max_length=50)
    sub_title = models.CharField(("Set Subtitle"), max_length=50)
    img = models.ImageField(("Upload Image"), upload_to="media/%Y-%m-%d")
    description = models.TextField(("Set Description"))
    url = models.URLField(("Set Video Url"), max_length=200)
    option_first_title = models.CharField(("Option First Title"), max_length=50)
    option_first_range = models.CharField(("Option First Range"), max_length=50)
    option_second_title = models.CharField(("Option Second Title"), max_length=50)
    option_second_range = models.CharField(("Option Second Range"), max_length=50)
    option_third_title = models.CharField(("Option Third Title"), max_length=50)
    option_third_range = models.CharField(("Option Third Range"), max_length=50)
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return "Skills Control"
    
    verbose_name = "Skills"
    verbose_name_plural = "Skills"

# Model to store image group information for the website
class ImageGroup(models.Model):
    img_first = models.ImageField(upload_to=f"media/%Y-%m-%d", blank=True)
    img_second = models.ImageField(upload_to=f"media/%Y-%m-%d", blank=True)
    img_third = models.ImageField(upload_to=f"media/%Y-%m-%d", blank=True)
    img_fourth = models.ImageField(upload_to=f"media/%Y-%m-%d", blank=True)
    img_fiveth = models.ImageField(upload_to=f"media/%Y-%m-%d", blank=True)
    img_sixth = models.ImageField(upload_to=f"media/%Y-%m-%d", blank=True)
    img_seventh = models.ImageField(upload_to=f"media/%Y-%m-%d", blank=True)
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return "Image Control"
    
    class Meta:
        verbose_name = "Image Group"
        verbose_name_plural = "Image Group"

# Model to store information for the website's "About" feed
class AboutFeed(models.Model):
    title = models.CharField(("Set Title"), max_length=50)
    description = models.TextField(("Set Description"))
    img = models.ImageField(("Upload Image"), upload_to="media/%Y-%m-%d")
    icon_image = models.ImageField(("Upload Icon Image"), upload_to="media/%Y-%m-%d")
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']
        verbose_name = "About Feed"
        verbose_name_plural = "About Feed"

# Model to store discography information for the website
class Discography(models.Model):
    price = models.IntegerField(("Set Price"))
    img = models.ImageField(("Upload Image"), upload_to="media/%Y-%m-%d")
    title = models.CharField(("Set Title"), max_length=50)
    app_store = models.URLField(("Set App Store URL"), max_length=200)
    google_play = models.URLField(("Set Google Play URL"), max_length=200)
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']
        verbose_name = "Discography"
        verbose_name_plural = "Discography"

# Model to store tour information for the website
class Tours(models.Model):
    title = models.CharField(("Set Title"), max_length=50)
    set_time = models.TimeField(("Set Time"), auto_now=False, auto_now_add=False)
    set_date = models.DateField(("Set Date"), auto_now=False, auto_now_add=False)
    location = models.CharField(("Set Location"), max_length=50)
    price = models.IntegerField(("Set Price"))
    img = models.ImageField(("Upload Image"), upload_to="media/%Y-%m-%d")
    description = models.TextField(("Set Description"))
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tours"
        verbose_name_plural = "Tours"

# Model to store video information for the website
class Videos(models.Model):
    title = models.CharField(("Set Title"), max_length=50)
    set_date = models.DateField(("Set Date"), auto_now=False, auto_now_add=False)
    img = models.ImageField(("Upload Image"), upload_to="media/%Y-%m-%d")
    url = models.URLField(("Set Video Url"), max_length=200)
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']
        verbose_name = "Videos"
        verbose_name_plural = "Videos"

class Blog(models.Model):
    MUSIC_CHOICES = (
        ('music', 'Music'),
        ('festival', 'Festival'),
        ('tinternational', 'Tinternational'),
        ('event', 'Event'),
    )
    type = models.CharField(max_length=255, choices=MUSIC_CHOICES, blank=True)
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.type
    
    def get_absolute_url(self):
        # Assuming you have a URL pattern named 'blog-detail' that points to the detail view
        return reverse('blog-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['id']
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

# Model to store detailed information for each blog entry
class BlogDetail(models.Model):
    connect = models.ForeignKey(Blog, verbose_name=("Select Type"), related_name='blog_details', on_delete=models.CASCADE)
    title = models.CharField(("Set Title"), max_length=50)
    img = models.ImageField(("Upload Image"), upload_to="media/%Y-%m-%d", null=True)
    sub_title = models.CharField(("Set Sub Title"), max_length=50)
    description = models.TextField(("Set Description"))
    set_date = models.DateField(("Set Date"), auto_now=False, auto_now_add=False)
    quote = models.TextField(("Set Quote"), null=True, blank=True, help_text="It's Not Important To Write Quote")
    quote_author = models.CharField(("Quote Author"), max_length=50, null=True, blank=True)
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # Assuming you have a URL pattern named 'blog-detail-detail' that points to the detail view
        return reverse('blog-detail-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['id']
        verbose_name = "Blog Detail View"
        verbose_name_plural = "Blog Detail Views"


# Model to store Privacy Policy information from the website's ckeditor form
class PrivacyPolicy(models.Model):
    title = models.CharField(("Установить заголовок"), max_length=50)
    description = models.TextField(("Установить текст"))
    is_published = models.BooleanField(("Is Published?"), default=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return "Privacy Policy Contro"
    
    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policy"

# Model to store contact information from the website's contact form
class Contact(models.Model):
    name = models.CharField(("Name"), max_length=50)
    email = models.EmailField(("Email"), max_length=254)
    phone = models.CharField(("Phone"), max_length=50)
    message = models.TextField(("Comment"))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")

    def __str__(self):
        return self.name , self.email
    
    class Meta:
        ordering = ['-id']
        verbose_name = "Message"
        verbose_name_plural = "Messages"

# Model to store email addresses for the website's newsletter subscribers
class Newsletter(models.Model):
    email = models.EmailField(("Subscriber Email"), max_length=254)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletter"
