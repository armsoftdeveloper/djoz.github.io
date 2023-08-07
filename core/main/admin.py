'''

    In This Python File You Find All Classes for Admin Page View

'''

# Import for registering models
from django.contrib import admin
# Import all models in current app
from .models import *
# Import ckeditor widget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Import forms for contact with ckeditor
from django import forms
# For Image Visibilirt in Admin
from django.utils.html import mark_safe


admin.site.site_header = 'Djoz'
#--------------------------------------------- CKEDITOR ---------------------------------------------#

class PrivacyPolicyForm(forms.ModelForm):
    description = forms.CharField(label = "Description" , widget = CKEditorUploadingWidget())

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'

# Admin & Model Admin for StaticInfo model
@admin.register(StaticInfo)
class StaticInfoAdmin(admin.ModelAdmin):
    list_display = ('get_image' ,'phone', 'email', 'address', 'facebook_url', 'twitter_url', 'instagram_url')
    list_display_links = ('get_image' ,'phone', 'email', 'address')
    search_fields = ('phone', 'email', 'address', 'facebook_url', 'twitter_url', 'instagram_url')
    
    def get_image(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

    
# Admin & Model Admin for Main model
@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'get_image' , 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title', )
    list_editable = ('is_published' ,)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'sub_title', 'description')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for UpcomingEvents model
@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' , 'date', 'location' , 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published' ,)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'location')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for AboutSpad model
@admin.register(AboutSpad)
class AboutSpadAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' , 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published' ,)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'description')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for Services model
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' , 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published' ,)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'description')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for Tracks model
@admin.register(Tracks)
class TracksAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published' ,)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title',)
    

# Admin & Model Admin for Youtube model
@admin.register(YoutubeFeed)
class YoutubeFeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' , 'url' , 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title',)
    
    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'


# Admin & Model Admin for TicketSection model
@admin.register(TicketSection)
class TicketSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' ,'subtitle', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'subtitle')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for Skills model
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' ,'sub_title', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'sub_title', 'description')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'
    
# Admin & Model Admin for ImageGroup model
@admin.register(ImageGroup)
class ImageGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('id',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')

# Admin & Model Admin for About Feed model
@admin.register(AboutFeed)
class AboutFeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' , 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'description')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for Discography model
@admin.register(Discography)
class DiscographyAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' , 'price', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title',)

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for Tours model
@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' , 'set_date', 'location', 'price', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'location', 'description')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for Videos model
@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' , 'set_date', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title',)

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for Blog model
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('type', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('type',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')

# Admin & Model Admin for Blog Detail model
@admin.register(BlogDetail)
class BlogDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image' , 'connect', 'set_date', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'connect__type', 'description')

    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" height="100px" width="100px" />')
        return '-'
    get_image.short_description = 'Image'

# Admin & Model Admin for Blog Detail model
@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_create', 'time_update' , 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update')
    search_fields = ('title', 'descripion', 'description')
    form = PrivacyPolicyForm

# Admin & Model Admin for Contact model
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'time_create')
    list_display_links = ('name',)
    list_filter = ('time_create',)
    search_fields = ('name', 'email', 'phone', 'message')

# Admin & Model Admin for Newsletter model
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'time_create')
    list_display_links = ('email',)
    list_filter = ('time_create',)
    search_fields = ('email',)
