from django.urls import path

from finance_app.report.finance_report import FullFinancePDFView
from finance_app.service.matrix_finance_calc import calculate_finance_matrix_view
from finance_app.views.destination_society_views import FinanceCategoryWithTasksAPIView
from finance_app.views.karma_and_task_40_views import (
    FinanceCategoryWithKarmaAndTask40APIView,
)
from finance_app.views.what_gives_you_money_views import (
    FinanceCategoryWhatGivesYouMoneyAPIView,
)
from finance_app.views.self_actualization_views import (
    FinanceCategoryWithOpportunityAPIView,
)
from finance_app.views.talents_views import FinanceCategoryWithTalentsAPIView
from finance_app.views.what_blocks_money_energy_views import (
    FinanceCategoryWithBlocksAPIView,
)

urlpatterns = [
    path(
        "talents/<str:category_id_or_title>/talents/",
        FinanceCategoryWithTalentsAPIView.as_view(),
        name="talents",
    ),
    path(
        "finance_opportunity/<str:category_id_or_title>/talents/",
        FinanceCategoryWithOpportunityAPIView.as_view(),
        name="finance_opportunity",
    ),
    path(
        "destination_society/<str:category_id_or_title>/tasks/",
        FinanceCategoryWithTasksAPIView.as_view(),
        name="destination_society",
    ),
    path(
        "what_gives_you_money/<str:category_id_or_title>/tasks/",
        FinanceCategoryWhatGivesYouMoneyAPIView.as_view(),
        name="what_gives_you_money",
    ),
    path(
        "blocks_money/<str:category_id_or_title>/tasks/",
        FinanceCategoryWithBlocksAPIView.as_view(),
        name="blocks_money",
    ),
    path(
        "karma_and_task_40/<str:category_id_or_title>/",
        FinanceCategoryWithKarmaAndTask40APIView.as_view(),
        name="karma_and_task_40",
    ),
    path(
        "calculate-finance-matrix/",
        calculate_finance_matrix_view,
        name="calculate-finance-matrix",
    ),
    path("finance-report/", FullFinancePDFView.as_view(), name="finance-report"),

]
