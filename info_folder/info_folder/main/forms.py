from django import forms
from .models import ModulesInfo

class OpleidingSelect(forms.Form):
    opleiding_selected = forms.CharField(max_length=50)

# class ModuleForm(forms.ModelForm):
#     save_module = forms.IntegerField(initial=0)
#     class Meta:
#         model = Modules
#         fields = ('cijfer',)

# class SelecteerStudentForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile_General
#         fields = ('firstname', 'lastname',)

# class SelecteerOpleidingForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile_General
#         fields = ('opleiding_selected', )

# class BuyModuleForm(forms.ModelForm):
#     class Meta:
#         model = Modules
#         fields = ('buy_module','date', )

# class UserOpleidingKiezenForm(forms.Form):
#     wiskunde = forms.BooleanField()
#     natuurkunde = forms.BooleanField()
#     sterrenkunde = forms.BooleanField()
#     scheikunde = forms.BooleanField()
#     biologie = forms.BooleanField()
#     lst = forms.BooleanField()
#     farmacie = forms.BooleanField()
#     informatica = forms.BooleanField()
#     ki = forms.BooleanField()
#     tbk = forms.BooleanField()

#     helper = FormHelper()
#     helper.label_class = 'col-lg-2'
#     helper.field_class = 'col-lg-8'
#     # helper.form_class = 'form-horizontal'
#     helper.layout = Layout(
#         Field('wiskunde', style="background: #FAFAFA; padding: 10px; left:-10px; bottom:0.5%"),
#         Field('natuurkunde', style="background: #FAFAFA; padding: 10px; left:-10px"),
#         Field('sterrenkunde', style="background: #FAFAFA; padding: 10px; left:-10px"),
#         Field('scheikunde', style="background: #FAFAFA; padding: 10px; left:-10px"),
#         Field('biologie', style="background: #FAFAFA; padding: 10px; left:-10px"),
#         Field('lst', style="background: #FAFAFA; padding: 10px; left:-10px"),
#         Field('farmacie', style="background: #FAFAFA; padding: 10px; left:-10px"),
#         Field('informatica', style="background: #FAFAFA; padding: 10px; left:-10px"),
#         FormActions(
#             Submit('save_changes', 'Save', css_class="btn-primary"),
#         )
#     )

# class UserProfileGeneralForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile_General
#         fields = ('firstname', 'lastname') #'questions'

# class UserProfileOpleidingForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile_Opleiding
#         fields = ('weging_stud', 'weging_toek', 'weging_soc')

# class ExportPDFForm(forms.Form):
# 	export_pdf = forms.IntegerField(initial=0)

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Questions
#         fields = ('question','answers', 'gebied','q_number',)

# class ModulesDatesForm(forms.Form):
#     dates = forms.ChoiceField(widget=forms.RadioSelect())

#     helper = FormHelper()
#     helper.label_class = 'col-lg-2'
#     helper.field_class = 'col-lg-8'
#     # helper.form_class = 'form-horizontal'
#     helper.layout = Layout(
#         Field('dates'),
#     )