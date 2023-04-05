from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOISCES = (
        ('sulpak.kg', 'sulpak.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == ['sulpak.kg']:
            laptop_parser = parser.parser()
            for i in laptop_parser:
                models.SulpakKg.objects.create(**i)