from django import forms
from core.models import Packagereview

class PackageReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : 'Write your review here .....'}))

    class Meta:
        model = Packagereview
        fields = ['review', 'rating']
