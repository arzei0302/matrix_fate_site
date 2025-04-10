import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import LanguageDetector from "i18next-browser-languagedetector";

const resources = {
  ru: {
    translation: {
      infoTable: {
        title: "Персональный расчет",
        subtitle: "Карта здоровья",
        chakraName: "НАЗВАНИЕ ЧАКРЫ",
        body: "ФИЗИКА",
        energy: "ЭНЕРГИЯ",
        emotion: "ЭМОЦИИ",
        total: "ИТОГО"
      },
      financePage: {
        enterBirthDate: "Enter birth date",
        day: "Day",
        month: "Month",
        year: "Year",
        calculate: "Calculate",
        commatrix: "Compatibility matrix",
        btn: "Calculate compatibility"
      },
      sky: "Небо",        // ru
earth: "Земля",
spiritualHarmony: "Духовная гармония",
planetary: "Планетарное",
financeAccordion: {
  qualities: {
    title: "Личные качества",
    description: "Описание личных качеств"
  },
  soulWork: {
    title: "Кем работать для души",
    description: "Описание работы для души"
  },
  karma: {
    title: "Карма и задача 40 лет",
    description: "Описание кармы и задачи"
  },
  pastLife: {
    title: "Задачи из прошлых жизней",
    description: "Описание задач из прошлых жизней"
  },
  comfortPoint: {
    title: "Точка комфорта",
    description: "Описание точки комфорта"
  },
  selfRealization: {
    title: "Самореализация",
    description: "Описание самореализации"
  },
  pointPersonalPower: {
    title: "Точка личной силы",
    description: "Описание точки личной силы"
  },
  genericPower: {
    title: "Сила рода",
    description: "Описание силы рода"
  },
  parentChildKarma: {
    title: "Детско-родительская карма",
    description: "Описание детско-родительской кармы"
  },
  spiritualKarma: {
    title: "Духовная карма",
    description: "Описание духовной кармы"
  },
  matrixRelationship: {
    title: "Отношения в матрице",
    description: "Описание отношений в матрице"
  },
  matrixMoney: {
    title: "Деньги в матрице",
    description: "Описание денег в матрице"
  },
  soulMission: {
    title: "Миссия души",
    description: "Описание миссии души"
  },
  diseasePredisposition: {
    title: "Предрасположенность к заболеваниям",
    description: "Описание предрасположенности к заболеваниям"
  },
  healthMap: {
    title: "Карта здоровья",
    description: "Описание карты здоровья"
  },
  total:"Общий прогноз",
  january:"Январь",
  feb:"Феварль",
  march:"Март",
  april:"Апрель",
  may:"Май",
  june:"Июнь",
  july:"Июль",
  august:"Август",
  sep:"Сентябрь",
  okt:"Октябрь",
  nov:"Ноябрь",
  dec:"Декабрь"

}
,
      // Header + UI
      matrix: "Матрица судьбы",
      finance: "Финансы",
      compatibility: "Совместимость",
      child: "Детская",
      prognosis: "Прогноз 2025",
      login: "Войти",
      cabinet: "Личный кабинет",
      unlock: "Разблокировать",
      noDescription: "Нет описания",

      // Chakra names
      chakra_7: "7. Сахасрара",
      chakra_6: "6. Аджна",
      chakra_5: "5. Вишудха",
      chakra_4: "4. Анахата",
      chakra_3: "3. Манипура",
      chakra_2: "2. Свадхистана",
      chakra_1: "1. Муладхара",

      // Accordion titles
      qualities: "Личные качества",
      soulWork: "Кем работать для Души",
      karma: "Карма и задача 40 лет",
      comfortPoint: "Точка душевного комфорта",
      selfRealization: "Самореализация",
      pastLifeTasks: "Задачи, которые тянутся из прошлых жизней",
      personalPower: "Точка личной силы",
      ancestralStrength: "Сила рода",

      parentChildKarma: "Детско-родительская карма",
      spiritualKarma: "Духовная карма",
      matrixRelationship: "Отношения в матрице",
      matrixMoney: "Деньги в матрице",
      soulMission: "Миссия души",
      diseasePredisposition: "Предрасположенность к заболеваниям",
      healthMap: "Карта здоровья",

      // PersonalInfo
      searchSelf: "Поиск себя:",
      searchSelfDesc: "Соединение мужского и женского. Выстраивание взаимоотношений. Способности, навыки, умения.",
      socialization: "Социализация:",
      socializationDesc: "Социальная и родовая системы. Результаты и признание в социуме.",
      spiritualQuestion1: "Духовный зачет. Кто я для бога? Где божественное во мне?",
      spiritualQuestion2: "Планетарное предназначение человека",

      // Months
      months: {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь"
      }
    }
  },

  en: {
    translation: {
      financeAccordion: {
        qualities: {
          title: "Personal qualities",
          description: "Description of personal qualities"
        },
        soulWork: {
          title: "Work for the soul",
          description: "Description of work for the soul"
        },
        karma: {
          title: "Karma and the task at 40",
          description: "Description of karma and the life task"
        },
        pastLife: {
          title: "Tasks from past lives",
          description: "Description of tasks from past lives"
        },
        comfortPoint: {
          title: "Comfort point",
          description: "Description of the comfort point"
        },
        selfRealization: {
          title: "Self-realization",
          description: "Description of self-realization"
        },
        pointPersonalPower: {
          title: "Personal power point",
          description: "Description of the personal power point"
        },
        genericPower: {
          title: "Ancestral strength",
          description: "Description of ancestral strength"
        },
        parentChildKarma: {
          title: "Parent-child karma",
          description: "Description of parent-child karma"
        },
        spiritualKarma: {
          title: "Spiritual karma",
          description: "Description of spiritual karma"
        },
        matrixRelationship: {
          title: "Relationships in the matrix",
          description: "Description of relationships in the matrix"
        },
        matrixMoney: {
          title: "Money in the matrix",
          description: "Description of money in the matrix"
        },
        soulMission: {
          title: "Soul mission",
          description: "Description of the soul mission"
        },
        diseasePredisposition: {
          title: "Disease predisposition",
          description: "Description of disease predisposition"
        },
        healthMap: {
          title: "Health map",
          description: "Description of the health map"
        },
        total: "General forecast",
        january: "January",
        feb: "February",
        march: "March",
        april: "April",
        may: "May",
        june: "June",
        july: "July",
        august: "August",
        sep: "September",
        okt: "October",
        nov: "November",
        dec: "December"
      },
      cabinetF: {
        myMatrices: "My Matrices",
        tariffs: "Tariffs",
        history: "View History",
        logout: "Logout",
        logoutConfirm: "Are you sure you want to log out?"
      },
      mymatrices: {
        available: "Available",
        dates: "dates",
        active: "Active",
        subscriptions: "subscriptions"
      },
      tariffs: {
        buy: "BUY",
        loading: "Loading tariffs..."
      },
      yes: "Yes",
      no: "No",
      sky: "Sky",
      earth: "Earth",
      spiritualHarmony: "Spiritual Harmony",
      planetary: "Planetary",
      infoTable: {
        title: "Personal Calculation",
        subtitle: "Health Map",
        chakraName: "CHAKRA NAME",
        body: "PHYSICAL",
        energy: "ENERGY",
        emotion: "EMOTIONS",
        total: "TOTAL"
      },
      matrix: "Destiny Matrix",
      finance: "Finance",
      compatibility: "Compatibility",
      child: "Child",
      prognosis: "Forecast 2025",
      login: "Login",
      cabinet: "My Cabinet",
      unlock: "Unlock",
      noDescription: "No description",

      chakra_7: "7. Sahasrara",
      chakra_6: "6. Ajna",
      chakra_5: "5. Vishuddha",
      chakra_4: "4. Anahata",
      chakra_3: "3. Manipura",
      chakra_2: "2. Svadhisthana",
      chakra_1: "1. Muladhara",

      qualities: "Personal qualities",
      soulWork: "Soul-purpose work",
      karma: "Karma and purpose at 40",
      comfortPoint: "Soul comfort point",
      selfRealization: "Self-realization",
      pastLifeTasks: "Tasks from past lives",
      personalPower: "Personal power point",
      ancestralStrength: "Ancestral strength",

      parentChildKarma: "Parent-child karma",
      spiritualKarma: "Spiritual karma",
      matrixRelationship: "Relationships in the matrix",
      matrixMoney: "Money in the matrix",
      soulMission: "Soul mission",
      diseasePredisposition: "Disease predisposition",
      healthMap: "Health map",

      searchSelf: "Search for self:",
      searchSelfDesc: "Unifying masculine and feminine. Building relationships. Abilities, skills, talents.",
      socialization: "Socialization:",
      socializationDesc: "Social and ancestral systems. Achievements and recognition in society.",
      spiritualQuestion1: "Spiritual exam. Who am I to God? Where is the divine within me?",
      spiritualQuestion2: "Planetary purpose of a person",
      history: {
        category: "Category",
        date: "Date",
        action: "Action",
        open: "OPEN",
        loading: "Loading data..."
      },
      footer: {
        privacyPolicy: "Privacy Policy",
        publicOffer: "Public Offer Agreement"
      },
      compability:{
        parentChildKarma: "Parent-child karma",
        spiritualKarma: "Spiritual karma",
        matrixRelationship: "Relationships in the matrix",
        matrixMoney: "Money in the matrix",
        soulMission: "Soul mission",
        diseasePredisposition: "Disease predisposition",
        healthMap: "Health map",

        searchSelf: "Search for self:",
        searchSelfDesc: "Unifying masculine and feminine. Building relationships. Abilities, skills, talents.",
        socialization: "Socialization:",
        socializationDesc: "Social and ancestral systems. Achievements and recognition in society.",
        spiritualQuestion1: "Spiritual exam. Who am I to God? Where is the divine within me?",
        spiritualQuestion2: "Planetary purpose of a person",
      },
      months: {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
      }
    }
  },

  fi: {
    footer: {
      privacyPolicy: "Tietosuojakäytäntö",
      publicOffer: "Julkinen sopimus"
    },
    translation: {
      tariffs: {
        buy: "OSTA",
        loading: "Ladataan tilauspaketteja..."
      },
      history: {
        category: "Kategoria",
        date: "Päivämäärä",
        action: "Toiminto",
        open: "AVAA",
        loading: "Ladataan tietoja..."
      },

      infoTable: {
        title: "Henkilökohtainen laskenta",
        subtitle: "Terveyskartta",
        chakraName: "CHAKRAN NIMI",
        body: "FYYSINEN",
        energy: "ENERGIA",
        emotion: "TUNTEET",
        total: "YHTEENSÄ"
      },
      financePage: {
        enterBirthDate: "Syötä syntymäaika",
        day: "Päivä",
        month: "Kuukausi",
        year: "Vuosi",
        calculate: "Laske",
        commatrix: "Yhteensopivuusmatriisi",
        btn: "Laske yhteensopivuus"

      },
      mymatrices: {
        available: "Saatavilla olevat",
        dates: "päivät",
        active: "Voimassa olevat",
        subscriptions: "tilaukset"
      },
      cabinetF: {
        myMatrices: "Omat matriisit",
        tariffs: "Tilauspaketit",
        history: "Katseluhistoria",
        logout: "Kirjaudu ulos",
        logoutConfirm: "Haluatko varmasti kirjautua ulos?"
      },
      yes: "Kyllä",
      no: "Ei",

      sky: "Taivas",
      earth: "Maa",
      spiritualHarmony: "Henkinen harmonia",
      planetary: "Planetaarinen",
      matrix: "Kohtalon matriisi",
      finance: "Talous",
      compatibility: "Yhteensopivuus",
      child: "Lapsi",
      prognosis: "Vuoden 2025 ennuste",
      login: "Kirjaudu",
      cabinet: "Oma tili",
      unlock: "Avaa",
      noDescription: "Ei kuvausta",
      financeAccordion: {
        qualities: {
          title: "Henkilökohtaiset ominaisuudet",
          description: "Henkilökohtaisten ominaisuuksien kuvaus"
        },
        soulWork: {
          title: "Sielun työ",
          description: "Kuvaus työstä sielulle"
        },
        karma: {
          title: "Karma ja tehtävä 40-vuotiaana",
          description: "Karman ja tehtävän kuvaus"
        },
        pastLife: {
          title: "Tehtävät menneistä elämistä",
          description: "Menneiden elämien tehtävien kuvaus"
        },
        comfortPoint: {
          title: "Mukavuuspiste",
          description: "Mukavuuspisteen kuvaus"
        },
        selfRealization: {
          title: "Itsensä toteuttaminen",
          description: "Itsensä toteuttamisen kuvaus"
        },
        pointPersonalPower: {
          title: "Henkilökohtainen voimapiste",
          description: "Henkilökohtaisen voimapisteen kuvaus"
        },
        genericPower: {
          title: "Suvun voima",
          description: "Suvun voiman kuvaus"
        },
        parentChildKarma: {
          title: "Lapsi–vanhempi-karma",
          description: "Lapsi–vanhempi-karman kuvaus"
        },
        spiritualKarma: {
          title: "Henkinen karma",
          description: "Henkisen karman kuvaus"
        },
        matrixRelationship: {
          title: "Suhteet matriisissa",
          description: "Suhteiden kuvaus matriisissa"
        },
        matrixMoney: {
          title: "Raha matriisissa",
          description: "Rahan kuvaus matriisissa"
        },
        soulMission: {
          title: "Sielun tehtävä",
          description: "Sielun tehtävän kuvaus"
        },
        diseasePredisposition: {
          title: "Alttius sairauksille",
          description: "Alttiuden kuvaus sairauksille"
        },
        healthMap: {
          title: "Terveyskartta",
          description: "Terveyskartan kuvaus"
        }
      },
      chakra_7: "7. Sahasrara",
      chakra_6: "6. Ajna",
      chakra_5: "5. Vishuddha",
      chakra_4: "4. Anahata",
      chakra_3: "3. Manipura",
      chakra_2: "2. Svadhisthana",
      chakra_1: "1. Muladhara",

      qualities: "Henkilökohtaiset ominaisuudet",
      soulWork: "Sielun työ",
      karma: "Karma ja tehtävä 40-vuotiaana",
      comfortPoint: "Sielun mukavuuspiste",
      selfRealization: "Itsensä toteuttaminen",
      pastLifeTasks: "Tehtävät menneistä elämistä",
      personalPower: "Henkilökohtainen voimapiste",
      ancestralStrength: "Sukujen voima",

      parentChildKarma: "Lapsi–vanhempi-karma",
      spiritualKarma: "Henkinen karma",
      matrixRelationship: "Suhteet matriisissa",
      matrixMoney: "Raha matriisissa",
      soulMission: "Sielun tehtävä",
      diseasePredisposition: "Sairauksien alttius",
      healthMap: "Terveyskartta",

      searchSelf: "Itseä etsimässä:",
      searchSelfDesc: "Maskuliinisen ja feminiinisen yhdistäminen. Suhteiden rakentaminen. Taidot ja kyvyt.",
      socialization: "Sosiaalistuminen:",
      socializationDesc: "Sosiaaliset ja sukujärjestelmät. Tunnustus ja saavutukset.",
      spiritualQuestion1: "Henkinen testi. Kuka olen Jumalalle? Missä on jumaluus minussa?",
      spiritualQuestion2: "Ihmisen planetaarinen tarkoitus",

      months: {
        1: "Tammikuu",
        2: "Helmikuu",
        3: "Maaliskuu",
        4: "Huhtikuu",
        5: "Toukokuu",
        6: "Kesäkuu",
        7: "Heinäkuu",
        8: "Elokuu",
        9: "Syyskuu",
        10: "Lokakuu",
        11: "Marraskuu",
        12: "Joulukuu"
      }
    }
  }
};

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources,
    fallbackLng: "ru",
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
