from django.core.management.base import BaseCommand
from django.utils.html import escape
from compatibility_app.models import (
    CompatibilityCategory,

    WhyDidYouMeet,
    TasksForCoupleArcana1, TasksForCoupleArcana2, TasksForCoupleArcana3,
    CoupleResourcesArcana1, CoupleResourcesArcana2,
    WhatFillsTheVapor,
    CouplesTaskForSociety,
    WhatGivesTribute, WhatTasksUnlockMoneyChannels, WhatBlocksMonetaryEnergy,
    CoupleRelations1, CoupleRelations2, WhatRelationshipProblemsCanArise,
)

CATEGORY_MAPPING = {
    "Miksi tapasitte": 1,
    "Parin yhteiset tehtävät": 2,
    "Parin resurssit": 3,
    "Mikä ravitsee suhdetta": 4,
    "Parin tehtävä yhteiskunnassa": 5,
    "Raha parisuhteessa": 6,
    "Suhteet parisuhteessa": 7,
}

DESCRIPTION = "Tässä pitäisi olla kuvaus"


def create_entries(model, category_id, title_prefix, description_prefix):
    category = CompatibilityCategory.objects.get(id=category_id)
    entries = [
        model(
            category=category,
            title=f"{title_prefix} {i}",
            description=escape(f"{description_prefix} {i}"),
            order_id=i,
        ) for i in range(1, 23)
    ]
    model.objects.bulk_create(entries)

class Command(BaseCommand):
    help = "Заполняет таблицы данными"

    def handle(self, *args, **kwargs):
        create_entries(WhyDidYouMeet, CATEGORY_MAPPING["Miksi tapasitte"], "Arcan", DESCRIPTION)

        create_entries(TasksForCoupleArcana1, CATEGORY_MAPPING["Parin yhteiset tehtävät"], "Arcan1", DESCRIPTION)
        create_entries(TasksForCoupleArcana2, CATEGORY_MAPPING["Parin yhteiset tehtävät"], "Arcan2", DESCRIPTION)
        create_entries(TasksForCoupleArcana3, CATEGORY_MAPPING["Parin yhteiset tehtävät"], "Arcan3", DESCRIPTION)
        
        create_entries(CoupleResourcesArcana1, CATEGORY_MAPPING["Parin resurssit"], " Arcan1", DESCRIPTION)
        create_entries(CoupleResourcesArcana2, CATEGORY_MAPPING["Parin resurssit"], " Arcan2", DESCRIPTION)

        create_entries(WhatFillsTheVapor, CATEGORY_MAPPING["Mikä ravitsee suhdetta"], "Arcan", DESCRIPTION)

        create_entries(CouplesTaskForSociety, CATEGORY_MAPPING["Parin tehtävä yhteiskunnassa"], "Arcan", DESCRIPTION)

        create_entries(WhatGivesTribute, CATEGORY_MAPPING["Raha parisuhteessa"], "Mikä antaa sinulle rahaa", DESCRIPTION)
        create_entries(WhatTasksUnlockMoneyChannels, CATEGORY_MAPPING["Raha parisuhteessa"], "Mitä tehtäviä sinun on suoritettava avataksesi rahakanavan", DESCRIPTION)
        create_entries(WhatBlocksMonetaryEnergy, CATEGORY_MAPPING["Raha parisuhteessa"], "Mikä estää rahan energian", DESCRIPTION)

        create_entries(CoupleRelations1, CATEGORY_MAPPING["Suhteet parisuhteessa"], "Arcan1", DESCRIPTION)
        create_entries(CoupleRelations2, CATEGORY_MAPPING["Suhteet parisuhteessa"], "Arcan2", DESCRIPTION)
        create_entries(WhatRelationshipProblemsCanArise, CATEGORY_MAPPING["Suhteet parisuhteessa"], "Mitä parisuhdeongelmia voi syntyä", DESCRIPTION)
        
        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена 22 записями в каждую таблицу!"))


# python manage.py fill_compatibility_data
