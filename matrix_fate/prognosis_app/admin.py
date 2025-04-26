from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (
    GeneralPrognosis, January, February, March, April, May, June, 
    July, August, September, October, November, December, BreakdownByYear
)
# from other_app.models import (
#     AccessMatrixModel, FinancialAndAntiCodeCalculation, ArcanaClues, 
#     PastCard, PresentCard, FutureCard, MessageSupport, 
#     PublicOfferAgreement, PrivacyPolicy, LandingPage
# )
from matrix_fate.other_app.models import (
    AccessMatrixModel, MessageSupport, 
    PublicOfferAgreement, PrivacyPolicy, SocialLinks
)


class MatrixAdmin(AdminSite):
    site_header = "Управление данными для матрицы Прогнозов"
    site_title = "Админ панель Матрицы Прогнозов"
    index_title = "Добро пожаловать в админ панель Матрицы Прогнозов"

    def get_app_list(self, request):
        """Группировка моделей без стандартных категорий"""

        grouped_apps = [
            ("ОБЩИЙ ПРОГНОЗ", ["GeneralPrognosis"]),
            ("ПРОГНОЗЫ ПО МЕСЯЦАМ", [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ]),
            # ("ДОП РАСЧЕТЫ", [
            #     "FinancialAndAntiCodeCalculation", "ArcanaClues", "PastCard", "PresentCard", "FutureCard"
            # ]),
            ("ОСТАЛЬНЫЕ", [
                "AccessMatrixModel", "MessageSupport", "PublicOfferAgreement", "PrivacyPolicy", "SocialLinks",
                # "LandingPage"
            ]),
            ("РАЗБОР ПО ГОДАМ", ["BreakdownByYear"]),
        ]

        grouped_models = {group[0]: {"name": group[0], "models": []} for group in grouped_apps}

        registered_models = {model.__name__: model for model in self._registry}

        for group_name, model_names in grouped_apps:
            for model_name in model_names:
                if model_name in registered_models:
                    model = registered_models[model_name]
                    grouped_models[group_name]["models"].append({
                        "name": model._meta.verbose_name_plural,
                        "object_name": model.__name__,
                        "admin_url": f"/prognosis_admin/{model._meta.app_label.lower()}/{model.__name__.lower()}/"
                    })

        return [grouped_models[group] for group in grouped_models if grouped_models[group]["models"]]


prognosis_admin = MatrixAdmin(name="prognosis_admin")


class BaseAdmin(admin.ModelAdmin):
    list_display = ("id", "order_id", "title", "description")
    search_fields = ("order_id", "title")
    list_filter = ("id",)
    list_per_page = 22
    list_display_links = ("order_id", "title", "description")



class AccessMatrixModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "is_active", "order")
    search_fields = ("name",)
    list_filter = ("is_active",)
    list_editable = ("is_active", "order")


# class FinancialAndAntiCodeCalculationAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "order_id", "image")
#     search_fields = ("title",)
#     list_filter = ("order_id",)


# class ArcanaCluesAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "image")
#     search_fields = ("title",)


# class PastCardAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "image")
#     search_fields = ("title",)


# class PresentCardAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "image")
#     search_fields = ("title",)


# class FutureCardAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "image")
#     search_fields = ("title",)


class MessageSupportAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "reference")
    search_fields = ("title",)


class PublicOfferAgreementAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


# class LandingPageAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "sub_title", "order_id")
#     search_fields = ("title",)
#     list_filter = ("order_id",)


class BreakdownByYearAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("title",)


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "link")
    search_fields = ("title",)


prognosis_admin.register(GeneralPrognosis, BaseAdmin)
for model in [January, February, March, April, May, June, July, August, September, October, November, December]:
    prognosis_admin.register(model, BaseAdmin)

prognosis_admin.register(AccessMatrixModel, AccessMatrixModelAdmin)
# prognosis_admin.register(FinancialAndAntiCodeCalculation, FinancialAndAntiCodeCalculationAdmin)
# prognosis_admin.register(ArcanaClues, ArcanaCluesAdmin)
# prognosis_admin.register(PastCard, PastCardAdmin)
# prognosis_admin.register(PresentCard, PresentCardAdmin)
# prognosis_admin.register(FutureCard, FutureCardAdmin)
prognosis_admin.register(MessageSupport, MessageSupportAdmin)
prognosis_admin.register(PublicOfferAgreement, PublicOfferAgreementAdmin)
prognosis_admin.register(PrivacyPolicy, PrivacyPolicyAdmin)
# prognosis_admin.register(LandingPage, LandingPageAdmin)
prognosis_admin.register(BreakdownByYear, BreakdownByYearAdmin)
prognosis_admin.register(SocialLinks, SocialLinksAdmin)
