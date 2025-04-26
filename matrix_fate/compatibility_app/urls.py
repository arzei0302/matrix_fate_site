from django.urls import path

from matrix_fate.compatibility_app.service.calculator_compatibility_view import calculate_compatibility_view
from matrix_fate.compatibility_app.service.calculator_matrix_compatibility_view import calculate_matrix_compatibility_view
from matrix_fate.compatibility_app.views.couple_money_views import (
    CompatibilityCategoryWithCoupleMoneyAPIView,
)
from matrix_fate.compatibility_app.views.couple_relations_views import (
    CompatibilityCategoryWithRelationsAPIView,
)
from matrix_fate.compatibility_app.views.couple_resources_views import (
    CompatibilityCategoryWithResourcesAPIView,
)
from matrix_fate.compatibility_app.views.couples_task_for_society_views import (
    CompatibilityCategoryWithCouplesTaskAPIView,
)
from matrix_fate.compatibility_app.views.tasks_for_couple_views import (
    CompatibilityCategoryWithTasksAPIView,
)
from matrix_fate.compatibility_app.views.what_fills_the_vapor_views import (
    CompatibilityCategoryWithWhatFillsAPIView,
)
from matrix_fate.compatibility_app.views.why_did_you_meet_views import (
    CompatibilityCategoryWithWhyDidYouMeetAPIView,
)

urlpatterns = [
    path(
        "why_did_you_meet/<str:category_id_or_title>/why_did_you_meet/",
        CompatibilityCategoryWithWhyDidYouMeetAPIView.as_view(),
        name="why_did_you_meet",
    ),
    path(
        "tasks_for_couple/<str:category_id_or_title>/tasks_for_couple/",
        CompatibilityCategoryWithTasksAPIView.as_view(),
        name="tasks_for_couple",
    ),
    path(
        "couple_resources/<str:category_id_or_title>/couple_resources/",
        CompatibilityCategoryWithResourcesAPIView.as_view(),
        name="couple_resources",
    ),
    path(
        "what_fills_the_vapor/<str:category_id_or_title>/what_fills_the_vapor/",
        CompatibilityCategoryWithWhatFillsAPIView.as_view(),
        name="what_fills_the_vapor",
    ),
    path(
        "couples_task_for_society/<str:category_id_or_title>/couples_task_for_society/",
        CompatibilityCategoryWithCouplesTaskAPIView.as_view(),
        name="couples_task_for_society",
    ),
    path(
        "couple_money/<str:category_id_or_title>/couple_money/",
        CompatibilityCategoryWithCoupleMoneyAPIView.as_view(),
        name="couple_money",
    ),
    path(
        "couple_relations/<str:category_id_or_title>/couple_relations/",
        CompatibilityCategoryWithRelationsAPIView.as_view(),
        name="couple_relations",
    ),

    path("calculate-matrix/", calculate_matrix_compatibility_view, name="calculate-matrix"),
    path("calculate-compatibility/", calculate_compatibility_view, name="calculate-compatibility"),

]
