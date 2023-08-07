# Importing necessary modules and packages
from typing import Any, Dict

from django.db.models.query import QuerySet
from .utils import *

'''

    In This Python File You Find All Functions For Main App

    * Views
    * Views - Models
    * Views - Templates
    * Call Function Types e.g. ListView , DetailView , CreateView
    * Forms Handling
    * Forms Handling For AJAX
    * Work With Gmail
    * 404 Page
    * You Can Find The Views Templates at templates - Folder

'''

# This class represents the index page view, displaying various sections of content.
class IndexListView(ListView, DataMixin):
    template_name = 'index.html'
    model = StaticInfo
    context_object_name = 'static_info'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # Get the default context from the parent class.
        context = super().get_context_data(**kwargs)

        # Fetch additional data to be displayed on the index page.
        context['main'] = Main.objects.get()
        context['events'] = UpcomingEvents.objects.all()
        context['about_spad'] = AboutSpad.objects.get()
        context['services'] = Services.objects.all()
        context['tracks'] = Tracks.objects.all()
        context['youtube_feed'] = YoutubeFeed.objects.all()
        context['ticket_section'] = TicketSection.objects.get()

        # Merge the user-specific context data with the default context.
        c_def = self.get_user_context(title='Home')
        return dict(list(context.items()) + list(c_def.items()))


# This class represents the about page view, displaying information about the organization.
class AboutListView(ListView, DataMixin):
    template_name = 'pages/about.html'
    model = ImageGroup
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # Get the default context from the parent class.
        context = super().get_context_data(**kwargs)

        # Fetch additional data to be displayed on the about page.
        context['about_spad'] = AboutSpad.objects.get()
        context['skills'] = Skills.objects.get()
        context['image_group'] = ImageGroup.objects.get()
        context['about_feed'] = AboutFeed.objects.all()

        # Merge the user-specific context data with the default context.
        c_def = self.get_user_context(title='About')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return ImageGroup.objects.filter(is_published = True)
    
# This class represents the discography page view, displaying a list of albums.
class DiscographyListView(ListView, DataMixin):
    model = Discography
    template_name = 'pages/discography.html'
    context_object_name = 'page_obj'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # Get the default context from the parent class.
        context = super().get_context_data(**kwargs)

        # Fetch the discography data and paginate the results.
        context['discography'] = Discography.objects.all()
        page_num = self.request.GET.get('page', 1)
        paginator = Paginator(context['discography'], 3)
        try:
            context['page_obj'] = paginator.page(page_num)
        except PageNotAnInteger:
            context['page_obj'] = paginator.page(1)
        except EmptyPage:
            context['page_obj'] = paginator.page(paginator.num_pages)

        # Merge the user-specific context data with the default context.
        c_def = self.get_user_context(title='Discography')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Discography.objects.filter(is_published = True)

# This class represents the tours page view, displaying a list of upcoming tours.
class ToursListView(ListView, DataMixin):
    model = Tours
    template_name = 'pages/tours.html'
    context_object_name = 'page_obj'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # Get the default context from the parent class.
        context = super().get_context_data(**kwargs)

        # Fetch the tours data and paginate the results.
        context['tours'] = Tours.objects.all()
        context['ticket_section'] = TicketSection.objects.get()
        page_num = self.request.GET.get('page', 1)
        paginator = Paginator(context['tours'], 3)
        try:
            context['page_obj'] = paginator.page(page_num)
        except PageNotAnInteger:
            context['page_obj'] = paginator.page(1)
        except EmptyPage:
            context['page_obj'] = paginator.page(paginator.num_pages)

        # Merge the user-specific context data with the default context.
        c_def = self.get_user_context(title='Tours')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Tours.objects.filter(is_published = True)

# This class represents the videos page view, displaying a list of video content.
class VideosListView(ListView, DataMixin):
    model = Videos
    template_name = 'pages/videos.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # Get the default context from the parent class.
        context = super().get_context_data(**kwargs)

        # Fetch the video data and separate the first video from the rest.
        context['videos'] = Videos.objects.all()
        context['first_video'] = context['videos'].first()
        context['remaining_videos'] = context['videos'][1:]

        # Merge the user-specific context data with the default context.
        c_def = self.get_user_context(title='Videos')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Videos.objects.filter(is_published = True)

# This class represents the blog page view, displaying a list of blog posts.
class BlogListView(ListView, DataMixin):
    model = Blog
    template_name = 'pages/blog.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # Get the default context from the parent class.
        context = super().get_context_data(**kwargs)

        # Fetch the blog data and paginate the results.
        context['blog'] = Blog.objects.all()
        context['blogDetail'] = BlogDetail.objects.all()
        page_num = self.request.GET.get('page', 1)
        paginator = Paginator(context['blogDetail'], 6)
        try:
            context['page_obj'] = paginator.page(page_num)
        except PageNotAnInteger:
            context['page_obj'] = paginator.page(1)
        except EmptyPage:
            context['page_obj'] = paginator.page(paginator.num_pages)

        # Merge the user-specific context data with the default context.
        c_def = self.get_user_context(title='Blog')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(is_published = True).select_related('blog_details')

# This class represents the blog details page view, displaying a single blog post.
class BlogDetailsView(DetailView, DataMixin):
    model = BlogDetail
    template_name = 'pages/blog-details.html'
    context_object_name = 'single_item'

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        # Get the default context from the parent class.
        context = super().get_context_data(**kwargs)
        
        # Fetch the primary key (id) from the URL parameters and get the number of visitors.
        id = self.kwargs.get('pk')
        context['visitors_count'] = self.request.session.get(f'page_{id}_visitors', 0)

        # Increment the number of visitors and store it in the session.
        if context['visitors_count'] == 0:
            self.request.session[f'page_{id}_visitors'] = 1
        else:
            self.request.session[f'page_{id}_visitors'] += 1

        # Merge the user-specific context data with the default context.
        c_def = self.get_user_context(title=context['single_item'].title)
        return dict(list(context.items()) + list(c_def.items()))
    
class PrivacyPolicyListView(ListView, DataMixin):
    model = PrivacyPolicy
    template_name = 'pages/privacy-policy.html'
    # context_object_name = 'privacy'

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['privacy_policy'] = PrivacyPolicy.objects.get()

        c_def = self.get_user_context(title='Privacy Policy')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return PrivacyPolicy.objects.filter(is_published = True)
    
# This class represents the contact page view, allowing users to send messages.
class ContactListView(ListView, DataMixin):
    template_name = 'pages/contact.html'
    model = Contact
    context_object_name = 'form'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # Get the default context from the parent class.
        context = super().get_context_data(**kwargs)

        # Initialize the contact form.
        context['form'] = MessageForm()

        # Merge the user-specific context data with the default context.
        c_def = self.get_user_context(title='Contact')
        return dict(list(context.items()) + list(c_def.items()))
    

# This class represents the contact message submission view, handling form submission.
class ContactMessageCreateView(CreateView):
    model = Contact
    form_class = MessageForm
    template_name = 'pages/contact.html'
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        # Send an email notification with the message details.
        subject = 'New Message from {}'.format(form.cleaned_data['name'])
        body = '\nName: {}\nEmail: {}\nPhone: {}\nMessage: {}'.format(
            form.cleaned_data['name'],
            form.cleaned_data['email'],
            form.cleaned_data['phone'],
            form.cleaned_data['message']
        )

        try:
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=form.cleaned_data['email'],
                to=["armsoftdeveloper@gmail.com"],
            )
            email.send()
        except Exception as e:
            print(e)

        # Save the form data to the model.
        instance = form.save()

        # Return JSON response for AJAX handling.
        ser_instance = serializers.serialize('json', [instance])
        return JsonResponse({"instance": ser_instance}, status=200)

    def form_invalid(self, form):
        return JsonResponse({"error": form.errors}, status=400)


# This class represents the newsletter subscription view, handling form submission.
class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'pages/about.html'

    def get_success_url(self):
        # Return the URL of the current page (the page from where the form was submitted)
        return self.request.get_full_path()
    
    def get_template_names(self):
        # Return a list of template names in the order of priority
        return [
            'pages/home.html',
            'pages/about.html',
            'pages/discography.html',
            'pages/tours.html',
            'pages/videos.html',
            'pages/blog.html',
            'pages/blog-details.html',
            'pages/contact.html',
        ]
    
    def form_valid(self, form):
        # Send a subscription confirmation email to the user.
        subject = 'New Follower'
        body = '\nEmail: {}'.format(form.cleaned_data['email'])
        try:
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=form.cleaned_data['email'],
                to=["armsoftdeveloper@gmail.com"],
            )
            email.send()
        except Exception as e:
            print("Email sending error:", e)

        # Save the form data to the model.
        response = super().form_valid(form)
        ser_instance = serializers.serialize('json', [self.object,])
        return JsonResponse({"instance": ser_instance}, status=200)

# This function represents the 404 Page Not Found Template
def pageNotFound(request, exception):
    return render(request , 'pages/404.html' , status=404)