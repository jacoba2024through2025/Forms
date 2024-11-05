from django import forms


class HowOld(forms.Form):
    end_year = forms.IntegerField()
    birth_year = forms.IntegerField()

class Order(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()

class HeyYou(forms.Form):
    name_data = forms.CharField()










#class AddForm(forms.Form):
    #x = forms.IntegerField()
    #y = forms.IntegerField()
    #z = forms.IntegerField()

#class SignUpForm(forms.Form):
    #email = forms.EmailField()
    #password = forms.CharField(widget=forms.PasswordInput)
    #repeated_password = forms.CharField(widget=forms.PasswordInput)

    #def clean(self):
        #cleaned_data = super().clean()

        #if cleaned_data["password"] != cleaned_data["repeated_password"]:
            #self.add_error("repeated_password", "Passwords must match")
        
        #return cleaned_data