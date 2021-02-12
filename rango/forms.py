from django import forms
<<<<<<< HEAD
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile
=======
from rango.models import Page, Category

>>>>>>> dfff8dc76e2ea3abd62f521a43a1667a8eb58bcd
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
<<<<<<< HEAD
    class Meta:
        model = Category
        fields = ('name',)
=======

    class Meta:
        model = Category
        fields = ('name',)

>>>>>>> dfff8dc76e2ea3abd62f521a43a1667a8eb58bcd
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=Page.URL_MAX_LENGTH, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
<<<<<<< HEAD
    class Meta:
        model = Page
        exclude = ('category',)
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
=======

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

>>>>>>> dfff8dc76e2ea3abd62f521a43a1667a8eb58bcd
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data
<<<<<<< HEAD
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username","email", "password")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
=======
>>>>>>> dfff8dc76e2ea3abd62f521a43a1667a8eb58bcd
