from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        widgets = {
            "title" : forms.TextInput(
                attrs= {
                    "class" : "form-control"
                },
            ),
            # "grade" : forms.NumberInput(
            #     attrs= {
            #         "class" : "form-control"
            #         "min" : "1",
            #         "max" :"5",
            #     },
            # ),
        }
        
        labels = {
            "title" : "제목",
            "content": "내용",
            "movie_name" : "영화 제목",
            "grade" : "점수"
        }