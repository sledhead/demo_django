from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data #dictionary
        print(cleaned_data)
        title = cleaned_data.get('title')

        if( title.lower().strip() == 'the sun' ):
            raise forms.ValidationError('Title entered is already used. Please select another one')
        
        print(title)

        return title