from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data #dictionary
    #     print(cleaned_data)
    #     title = cleaned_data.get('title')

    #     if( title.lower().strip() == 'the sun' ):
    #         raise forms.ValidationError('Title entered is already used. Please select another one')
        
    #     print(title)

    #     return title
    
    def clean(self):

        cleaned_data = self.cleaned_data
        print("all data", cleaned_data)

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if( title.lower().strip() == 'the sun' ):
            self.add_error('title','Title entered is already used. Please select another one')
            #raise forms.ValidationError('Title entered is already used. Please select another one')

        if( "sun" in content or "sun" in title.lower() ):
            self.add_error('content', 'sun is not allowed in content')
            raise forms.ValidationError("sun is not allowed")
        
        return cleaned_data