from rest_framework import serializers
from ..models import (
    ChildCategory,
    WhatChildShouldTeachParents,
    WhatMistakesRelationshipParentsChildren,
    WhatShouldComeQualitiesChild,
)

class WhatChildShouldTeachParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatChildShouldTeachParents
        fields = ["order_id", "title", "description"]

class WhatMistakesRelationshipParentsChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatMistakesRelationshipParentsChildren
        fields = ["order_id", "title", "description"]

class WhatShouldComeQualitiesChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatShouldComeQualitiesChild
        fields = ["order_id", "title", "description"]

class ChildCategoryParentKarmaSerializer(serializers.ModelSerializer):
    what_child_should_teach_parents = WhatChildShouldTeachParentsSerializer(many=True)
    what_mistakes_relationship_parents_children = WhatMistakesRelationshipParentsChildrenSerializer(many=True)
    what_should_come_qualities_child = WhatShouldComeQualitiesChildSerializer(many=True)

    class Meta:
        model = ChildCategory
        fields = [
            "id", "title", "description", "is_paid",
            "what_child_should_teach_parents",
            "what_mistakes_relationship_parents_children",
            "what_should_come_qualities_child"
        ]
