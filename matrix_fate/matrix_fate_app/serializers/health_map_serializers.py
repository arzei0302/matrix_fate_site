from rest_framework import serializers
from ..models import (
    Category,
    SahasraraO7,
    SahasraraP7,
    SahasraraQ7,
    AdjnaO6,
    AdjnaP6,
    AdjnaQ6,
    VishudkhaO5,
    VishudkhaP5,
    VishudkhaQ5,
    AnakhataO4,
    AnakhataP4,
    AnakhataQ4,
    ManipuraO3,
    ManipuraP3,
    ManipuraQ3,
    SvadkhistanaO2,
    SvadkhistanaP2,
    SvadkhistanaQ2,
    MuladkharaO1,
    MuladkharaP1,
    MuladkharaQ1,
    TotalO,
    TotalP,
    TotalQ,
)


class SahasraraO7Serializer(serializers.ModelSerializer):
    class Meta:
        model = SahasraraO7
        fields = ["order_id", "title", "description"]


class SahasraraP7Serializer(serializers.ModelSerializer):
    class Meta:
        model = SahasraraP7
        fields = ["order_id", "title", "description"]


class SahasraraQ7Serializer(serializers.ModelSerializer):
    class Meta:
        model = SahasraraQ7
        fields = ["order_id", "title", "description"]


class AdjnaO6Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdjnaO6
        fields = ["order_id", "title", "description"]


class AdjnaP6Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdjnaP6
        fields = ["order_id", "title", "description"]


class AdjnaQ6Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdjnaQ6
        fields = ["order_id", "title", "description"]


class VishudkhaO5Serializer(serializers.ModelSerializer):
    class Meta:
        model = VishudkhaO5
        fields = ["order_id", "title", "description"]


class VishudkhaP5Serializer(serializers.ModelSerializer):
    class Meta:
        model = VishudkhaP5
        fields = ["order_id", "title", "description"]


class VishudkhaQ5Serializer(serializers.ModelSerializer):
    class Meta:
        model = VishudkhaQ5
        fields = ["order_id", "title", "description"]


class AnakhataO4Serializer(serializers.ModelSerializer):
    class Meta:
        model = AnakhataO4
        fields = ["order_id", "title", "description"]


class AnakhataP4Serializer(serializers.ModelSerializer):
    class Meta:
        model = AnakhataP4
        fields = ["order_id", "title", "description"]


class AnakhataQ4Serializer(serializers.ModelSerializer):
    class Meta:
        model = AnakhataQ4
        fields = ["order_id", "title", "description"]


class ManipuraO3Serializer(serializers.ModelSerializer):
    class Meta:
        model = ManipuraO3
        fields = ["order_id", "title", "description"]


class ManipuraP3Serializer(serializers.ModelSerializer):
    class Meta:
        model = ManipuraP3
        fields = ["order_id", "title", "description"]


class ManipuraQ3Serializer(serializers.ModelSerializer):
    class Meta:
        model = ManipuraQ3
        fields = ["order_id", "title", "description"]


class SvadkhistanaO2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SvadkhistanaO2
        fields = ["order_id", "title", "description"]


class SvadkhistanaP2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SvadkhistanaP2
        fields = ["order_id", "title", "description"]


class SvadkhistanaQ2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SvadkhistanaQ2
        fields = ["order_id", "title", "description"]


class MuladkharaO1Serializer(serializers.ModelSerializer):
    class Meta:
        model = MuladkharaO1
        fields = ["order_id", "title", "description"]


class MuladkharaP1Serializer(serializers.ModelSerializer):
    class Meta:
        model = MuladkharaP1
        fields = ["order_id", "title", "description"]


class MuladkharaQ1Serializer(serializers.ModelSerializer):
    class Meta:
        model = MuladkharaQ1
        fields = ["order_id", "title", "description"]


class TotalOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalO
        fields = ["order_id", "title", "description"]


class TotalPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalP
        fields = ["order_id", "title", "description"]


class TotalQSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalQ
        fields = ["order_id", "title", "description"]


class CategoryWithHealthMapSerializer(serializers.ModelSerializer):
    sahasrara_o7 = SahasraraO7Serializer(many=True)
    sahasrara_p7 = SahasraraP7Serializer(many=True)
    sahasrara_q7 = SahasraraQ7Serializer(many=True)

    adjna_o6 = AdjnaO6Serializer(many=True)
    adjna_p6 = AdjnaP6Serializer(many=True)
    adjna_q6 = AdjnaQ6Serializer(many=True)

    vishudkha_o5 = VishudkhaO5Serializer(many=True)
    vishudkha_p5 = VishudkhaP5Serializer(many=True)
    vishudkha_q5 = VishudkhaQ5Serializer(many=True)

    anakhata_o4 = AnakhataO4Serializer(many=True)
    anakhata_p4 = AnakhataP4Serializer(many=True)
    anakhata_q4 = AnakhataQ4Serializer(many=True)

    manipura_o3 = ManipuraO3Serializer(many=True)
    manipura_p3 = ManipuraP3Serializer(many=True)
    manipura_q3 = ManipuraQ3Serializer(many=True)

    svadkhistana_o2 = SvadkhistanaO2Serializer(many=True)
    svadkhistana_p2 = SvadkhistanaP2Serializer(many=True)
    svadkhistana_q2 = SvadkhistanaQ2Serializer(many=True)

    muladkhara_o1 = MuladkharaO1Serializer(many=True)
    muladkhara_p1 = MuladkharaP1Serializer(many=True)
    muladkhara_q1 = MuladkharaQ1Serializer(many=True)

    total_o = TotalOSerializer(many=True)
    total_p = TotalPSerializer(many=True)
    total_q = TotalQSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "sahasrara_o7",
            "sahasrara_p7",
            "sahasrara_q7",
            "adjna_o6",
            "adjna_p6",
            "adjna_q6",
            "vishudkha_o5",
            "vishudkha_p5",
            "vishudkha_q5",
            "anakhata_o4",
            "anakhata_p4",
            "anakhata_q4",
            "manipura_o3",
            "manipura_p3",
            "manipura_q3",
            "svadkhistana_o2",
            "svadkhistana_p2",
            "svadkhistana_q2",
            "muladkhara_o1",
            "muladkhara_p1",
            "muladkhara_q1",
            "total_o",
            "total_p",
            "total_q",
        ]
