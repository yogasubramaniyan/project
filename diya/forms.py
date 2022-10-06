from django import forms

class Contactformemail(froms.Form):
	fromemail=forms.EmailFeild(required=True)
	subjectform=CharFeild(required=True)
	message=CharFeild(required=True)