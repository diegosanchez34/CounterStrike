from django import forms
from django.forms.widgets import TextInput, NumberInput

class PredictionForm(forms.Form):
    InternalTeamId = forms.ChoiceField(label='Internal Team ID', choices=[(1, 'Terrorist'), (2, 'CounterTerrorist')], widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    MatchId = forms.IntegerField(label='Match ID', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    RoundId = forms.IntegerField(label='Round ID', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    PrimaryAssaultRifle = forms.IntegerField(label='Primary Assault Rifle', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    PrimarySniperRifle = forms.IntegerField(label='Primary Sniper Rifle', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    PrimaryPistol = forms.IntegerField(label='Primary Pistol', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    RoundKills = forms.IntegerField(label='Round Kills', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    RoundHeadshots = forms.IntegerField(label='Round Headshots', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    RoundFlankKills = forms.IntegerField(label='Round Flank Kills', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    RoundStartingEquipmentValue = forms.IntegerField(label='Round Starting Equipment Value', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    TeamStartingEquipmentValue = forms.IntegerField(label='Team Starting Equipment Value', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    MatchKills = forms.IntegerField(label='Match Kills', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    MatchAssists = forms.IntegerField(label='Match Assists', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))

class PredictionRFForm(forms.Form):
    Team = forms.ChoiceField(label='Team', choices=[(1, 'Terrorist'), (2, 'CounterTerrorist')], widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    Map = forms.IntegerField(label='Map', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    RoundId = forms.IntegerField(label='Round ID', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    MatchId = forms.IntegerField(label='Match ID', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    Survived = forms.IntegerField(label='Survived', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    RoundKills = forms.IntegerField(label='Round Kills', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    RoundStartingEquipmentValue = forms.IntegerField(label='Round Starting Equipment Value', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    TeamStartingEquipmentValue = forms.IntegerField(label='Team Starting Equipment Value', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    MatchKills = forms.IntegerField(label='Match Kills', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    MatchAssists = forms.IntegerField(label='Match Assists', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))
    MatchHeadshots = forms.IntegerField(label='Match Headshots', widget=NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #3d4536; color: white;'}))