from django import forms

class PredictionForm(forms.Form):
    InternalTeamId = forms.IntegerField(label='Internal Team ID')
    MatchId = forms.IntegerField(label='Match ID')
    RoundId = forms.IntegerField(label='Round ID')
    PrimaryAssaultRifle = forms.IntegerField(label='Primary Assault Rifle')
    PrimarySniperRifle = forms.IntegerField(label='Primary Sniper Rifle')
    PrimaryPistol = forms.IntegerField(label='Primary Pistol')
    RoundKills = forms.IntegerField(label='Round Kills')
    RoundHeadshots = forms.IntegerField(label='Round Headshots')
    RoundFlankKills = forms.IntegerField(label='Round Flank Kills')
    RoundStartingEquipmentValue = forms.IntegerField(label='Round Starting Equipment Value')
    TeamStartingEquipmentValue = forms.IntegerField(label='Team Starting Equipment Value')
    MatchKills = forms.IntegerField(label='Match Kills')
    MatchAssists = forms.IntegerField(label='Match Assists')
