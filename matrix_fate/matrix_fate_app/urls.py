from django.urls import path

from matrix_fate.matrix_fate_app.report.matrix_fate_report import FullMatrixPDFView
from matrix_fate.matrix_fate_app.service.matrix_fate_calc import calculate_matrix_view
from .views.personal_qualities_views import CategoryWithTalentsAPIView
from .views.soul_work_views import CategoryWithTalentsSoulAPIView
from .views.main_task_40_views import CategoryWithMainTask40APIView
from .views.soul_comfort_point_views import CategoryWithSoulComfortAPIView
from .views.self_realization_views import CategoryWithSelfRealizationAPIView
from .views.past_life_task_views import CategoryWithPastLifeTaskAPIView
from .views.personal_power_point_views import CategoryWithPersonalPowerAPIView
from .views.ancestral_power_views import CategoryWithAncestralPowerAPIView
from .views.parent_child_karma_views import CategoryWithParentChildKarmaAPIView
from .views.spiritual_karma_views import CategoryWithSpiritualKarmaAPIView
from .views.matrix_relationships_views import CategoryWithMatrixRelationshipsAPIView
from .views.matrix_money_views import CategoryWithMatrixMoneyAPIView
from .views.soul_mission_views import CategoryWithSoulMissionAPIView
from .views.disease_predisposition_views import CategoryWithDiseasePredispositionAPIView
from .views.ancestral_task7_views import CategoryWithAncestralTask7APIView

from .views.health_map_views import CategoryWithHealthMapAPIView


urlpatterns = [
    path(
        "personal_qualities/<str:category_id_or_title>/talents/",
        CategoryWithTalentsAPIView.as_view(),
        name="personal_qualities",
    ),
    path(
        "soul_work/<str:category_id_or_title>/talents/",
        CategoryWithTalentsSoulAPIView.as_view(),
        name="soul-work-talents",
    ),
    path(
        "main_task_40/<str:category_id_or_title>/talents/",
        CategoryWithMainTask40APIView.as_view(),
        name="main-task-40-talents",
    ),
    path(
        "soul_comfort_point/<str:category_id_or_title>/talents/",
        CategoryWithSoulComfortAPIView.as_view(),
        name="soul-comfort-point-talents",
    ),
    path(
        "self_realization/<str:category_id_or_title>/talents/",
        CategoryWithSelfRealizationAPIView.as_view(),
        name="self-realization-talents",
    ),
    path(
        "past_life_task/<str:category_id_or_title>/talents/",
        CategoryWithPastLifeTaskAPIView.as_view(),
        name="past-life-task-talents",
    ),
    path(
        "personal_power_point/<str:category_id_or_title>/personal_power_point/",
        CategoryWithPersonalPowerAPIView.as_view(),
        name="personal_power_point",
    ),
    path(
        "ancestral_power/<str:category_id_or_title>/ancestral_power/",
        CategoryWithAncestralPowerAPIView.as_view(),
        name="ancestral_power",
    ),
    path(
        "parent_child_karma/<str:category_id_or_title>/parent_child_karma/",
        CategoryWithParentChildKarmaAPIView.as_view(),
        name="parent_child_karma",
    ),
    path(
        "spiritual_karma/<str:category_id_or_title>/spiritual_karma/",
        CategoryWithSpiritualKarmaAPIView.as_view(),
        name="spiritual_karma",
    ),
    path(
        "matrix_relationships/<str:category_id_or_title>/matrix_relationships/",
        CategoryWithMatrixRelationshipsAPIView.as_view(),
        name="matrix_relationships",
    ),
    path(
        "matrix_money/<str:category_id_or_title>/matrix_money/",
        CategoryWithMatrixMoneyAPIView.as_view(),
        name="matrix_money",
    ),
    path(
        "soul_mission/<str:category_id_or_title>/soul_mission/",
        CategoryWithSoulMissionAPIView.as_view(),
        name="soul_mission",
    ),
    path(
        "disease_predisposition/<str:category_id_or_title>/disease_predisposition/",
        CategoryWithDiseasePredispositionAPIView.as_view(),
        name="disease_predisposition",
    ),
    path(
        "ancestral_task7/<str:category_id_or_title>/ancestral_task7/",
        CategoryWithAncestralTask7APIView.as_view(),
        name="ancestral_task7",
    ),
    path(
        "health_map/<str:category_id_or_title>/health_map/",
        CategoryWithHealthMapAPIView.as_view(),
        name="health_map",
    ),

    path("calculate-matrix/", calculate_matrix_view, name="calculate-matrix"),
    # path("matched_programs/", get_programs_by_matrix_view, name="matched-programs"),

    path("matrix-report/", FullMatrixPDFView.as_view(), name="matrix-report"),

]
