from django import forms
from .models import Review, Course

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        university = kwargs.pop('university', None)
        super(ReviewForm, self).__init__(*args, **kwargs)
        
        # Dynamically set the queryset for the course field
        if university:
            self.fields['course'].queryset = Course.objects.filter(university=university)
        else:
            self.fields['course'].queryset = Course.objects.none()  # Or any default behavior if university is not provided
    
    course = forms.ModelChoiceField(queryset=Course.objects.none(), required=True)
    rating = forms.FloatField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'step': '0.5'}),
        required=True
    )
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Review
        fields = ['course', 'rating', 'comment']
