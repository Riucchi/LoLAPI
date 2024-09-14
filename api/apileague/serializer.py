from rest_framework import serializers
from .models import Champion, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['passive_img','q_img','w_img','e_img','r_img','passive_name','q_name','w_name','e_name','r_name']

class ChampionSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Champion
        fields = ['nombre', 'lore', 'champ_img', 'skills']


