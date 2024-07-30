from rest_framework import serializers
from .models import Player, PlayerSkill

class PlayerSkillSerializer(serializers.ModelSerializer):
    skill = serializers.ChoiceField(choices=PlayerSkill.skill_choices, source='skill_name')
    value = serializers.IntegerField(source='skill_level')
    playerId = serializers.SerializerMethodField()

    class Meta:
        model = PlayerSkill
        fields = ['id', 'skill', 'value', 'playerId']
        read_only_fields = ['id', 'playerId']

    def get_playerId(self, obj):
        return obj.player.id if obj.player else None

class PlayerSerializer(serializers.ModelSerializer):
    playerSkills = PlayerSkillSerializer(many=True, source='skills')

    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'playerSkills']
        read_only_fields = ['id']

    def validate_position(self, value):
        valid_positions = dict(Player.POSITION_CHOICES).keys()
        if value not in valid_positions:
            raise serializers.ValidationError(f"Invalid value for position: {value}")
        return value

    def validate_playerSkills(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("Player must have at least one skill")
        return value

    def create(self, validated_data):
        skills_data = validated_data.pop('skills')
        player = Player.objects.create(**validated_data)
        for skill_data in skills_data:
            PlayerSkill.objects.create(player=player, **skill_data)
        return player

    def update(self, instance, validated_data):
        skills_data = validated_data.pop('skills', [])
        instance = super().update(instance, validated_data)

        # Update or create skills
        existing_skills = list(instance.skills.all())
        for skill_data in skills_data:
            if existing_skills:
                skill = existing_skills.pop(0)
                for attr, value in skill_data.items():
                    setattr(skill, attr, value)
                skill.save()
            else:
                PlayerSkill.objects.create(player=instance, **skill_data)

        # Delete any remaining existing skills
        for skill in existing_skills:
            skill.delete()

        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['playerSkills'] = PlayerSkillSerializer(instance.skills.all(), many=True).data
        return representation

    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except serializers.ValidationError as e:
            error_dict = {"message": "Validation error"}
            if 'position' in e.detail:
                error_dict["message"] = e.detail['position'][0]
            elif 'playerSkills' in e.detail:
                error_dict["message"] = e.detail['playerSkills'][0]
            raise serializers.ValidationError(error_dict)