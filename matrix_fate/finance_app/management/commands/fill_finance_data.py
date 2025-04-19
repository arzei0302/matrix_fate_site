from django.core.management.base import BaseCommand
from django.utils.html import escape
from finance_app.models import (
    FinanceCategory, 
    YourGreatestTalentBirth, QualitiesRevealedAge20, QualitiesDevelopAge40,
    YourOpportunity, 
    TaskPersonalArcana1, TaskPersonalArcana2, TaskPersonalArcana3,
    TheMainTask40Years, WhatBeforeYouTurn40Years, WhatAfterYouTurn40Years,
    WhatGivesYouMoney, WhatOpensYourMoneyChannel, AreasOfRealization,
    TasksOpenMoneyChannel1, TasksOpenMoneyChannel2, WhatBlocksMoneyEnergy
)

CATEGORY_MAPPING = {
    "Kyvyt": 1,
    "Itsensä toteuttaminen": 2,
    "Tehtävä yhteiskunnassa": 3,
    "Mikä tuo rahaa": 4,
    "Mikä estää rahavirran": 5,
    "Karma ja 40 vuoden tehtävä": 6,
}

DESCRIPTION = "Tässä pitäisi olla kuvaus"


def create_entries(model, category_id, title_prefix, description_prefix):
    category = FinanceCategory.objects.get(id=category_id)
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
        create_entries(YourGreatestTalentBirth, CATEGORY_MAPPING["Kyvyt"], "Suurin lahjakkuutesi syntymästä lähtien", DESCRIPTION)
        create_entries(QualitiesRevealedAge20, CATEGORY_MAPPING["Kyvyt"], "20 ikävuoteen mennessä ilmenevät ominaisuudet", DESCRIPTION)
        create_entries(QualitiesDevelopAge40, CATEGORY_MAPPING["Kyvyt"], "Ominaisuudet, joita meidän on kehitettävä ennen 40 vuoden ikää", DESCRIPTION)
        create_entries(YourOpportunity, CATEGORY_MAPPING["Itsensä toteuttaminen"], "Sinun tilaisuutesi", DESCRIPTION)
        create_entries(TaskPersonalArcana1, CATEGORY_MAPPING["Tehtävä yhteiskunnassa"], "Henkilökohtaisen arkanan tehtävä1", DESCRIPTION)
        create_entries(TaskPersonalArcana2, CATEGORY_MAPPING["Tehtävä yhteiskunnassa"], "Henkilökohtaisen arkanan tehtävä2", DESCRIPTION)
        create_entries(TaskPersonalArcana3, CATEGORY_MAPPING["Tehtävä yhteiskunnassa"], "Henkilökohtaisen arkanan tehtävä3", DESCRIPTION)
        create_entries(WhatGivesYouMoney, CATEGORY_MAPPING["Mikä tuo rahaa"], "Mikä antaa sinulle rahaa", DESCRIPTION)
        create_entries(WhatOpensYourMoneyChannel, CATEGORY_MAPPING["Mikä tuo rahaa"], "Mikä avaa rahakanavasi", DESCRIPTION)
        create_entries(AreasOfRealization, CATEGORY_MAPPING["Mikä tuo rahaa"], "Toteuttamisalueet", DESCRIPTION)
        create_entries(TasksOpenMoneyChannel1, CATEGORY_MAPPING["Mikä estää rahavirran"], "Mitkä tehtävät sinun on suoritettava, jotta voit avata rahakanavan1", DESCRIPTION)
        create_entries(TasksOpenMoneyChannel2, CATEGORY_MAPPING["Mikä estää rahavirran"], "Mitkä tehtävät sinun on suoritettava, jotta voit avata rahakanavan2", DESCRIPTION)
        create_entries(WhatBlocksMoneyEnergy, CATEGORY_MAPPING["Mikä estää rahavirran"], "Mikä estää rahan energian", DESCRIPTION)
        create_entries(TheMainTask40Years, CATEGORY_MAPPING["Karma ja 40 vuoden tehtävä"], "Tärkein haaste 40 vuoden ajan", DESCRIPTION)
        create_entries(WhatBeforeYouTurn40Years, CATEGORY_MAPPING["Karma ja 40 vuoden tehtävä"], "Mitä sinun on tehtävä ennen kuin täytät 40", DESCRIPTION)
        create_entries(WhatAfterYouTurn40Years, CATEGORY_MAPPING["Karma ja 40 vuoden tehtävä"], "Mitä sinun on tehtävä 40 ikävuoden jälkeen", DESCRIPTION)

        
        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена 22 записями в каждую таблицу!"))

# python manage.py fill_finance_data