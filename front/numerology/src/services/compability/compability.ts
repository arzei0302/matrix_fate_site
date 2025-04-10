export interface Chakra {
    name: string;
    color: string;
  }
  
  export interface AccordionItem {
    title: string;
    key: string;
    locked?: boolean;
  }
  
  export interface PersonalInfo {
    title: string;
    description: string;
    skyLabel: string;
    skyKey: string;
    earthLabel: string;
    earthKey: string;
    resultKey: string;
    spiritLabel: string;
    spiritKey: string;
    question: string;
  }
  
  export interface Month {
    name: string;
    value: number;
    days: number;
  }
  
  export const newChakraData: Chakra[] = [
    { name: "7. Сахасрара", color: "#8B5CF6" },
    { name: "6. Аджна", color: "#6366F1" },
    { name: "5. Вишудха", color: "#06B6D4" },
    { name: "4. Анахата", color: "#22C55E" },
    { name: "3. Манипура", color: "#EAB308" },
    { name: "2. Свадхистана", color: "#F97316" },
    { name: "1. Муладхара", color: "#EF4444" }
  ];
  
  export const accordionConfig: AccordionItem[] = [
    { title: "Личные качества", key: "qualities" },
    { title: "Кем работать для Души", key: "soulWork" },
    { title: "Карма и задача 40 лет", key: "karma" },
    { title: "Точка душевного комфорта", key: "comfortPoint", locked: true },
    { title: "Самореализация", key: "selfRealization", locked: true },
    { title: "Задачи, которые тянутся из прошлых жизней", key: "pastLifeTasks", locked: true },
    { title: "Точка личной силы", key: "personalPower", locked: true },
    { title: "Сила рода", key: "ancestralStrength", locked: true }
  ];
  
  export const newPersonalInfo: PersonalInfo[] = [
    {
      title: "Поиск себя:",
      description: "Соединение мужского и женского. Выстраивание взаимоотношений. Способности, навыки, умения.",
      skyLabel: "Небо",
      skyKey: "r",
      earthLabel: "Земля",
      earthKey: "s",
      resultKey: "y",
      spiritLabel: "Духовная гармония",
      spiritKey: "w",
      question: "Духовный зачет. Кто я для бога? Где божественное во мне?"
    },
    {
      title: "Социализация:",
      description: "Социальная и родовая системы. Результаты и признание в социуме.",
      skyLabel: "M",
      skyKey: "t",
      earthLabel: "Ж",
      earthKey: "u",
      resultKey: "v",
      spiritLabel: "Планетарное",
      spiritKey: "x",
      question: "Планетарное предназначение человека"
    }
  ];
  
  export const months: Month[] = [
    { name: "Январь", value: 1, days: 31 },
    { name: "Февраль", value: 2, days: 28 },
    { name: "Март", value: 3, days: 31 },
    { name: "Апрель", value: 4, days: 30 },
    { name: "Май", value: 5, days: 31 },
    { name: "Июнь", value: 6, days: 30 },
    { name: "Июль", value: 7, days: 31 },
    { name: "Август", value: 8, days: 31 },
    { name: "Сентябрь", value: 9, days: 30 },
    { name: "Октябрь", value: 10, days: 31 },
    { name: "Ноябрь", value: 11, days: 30 },
    { name: "Декабрь", value: 12, days: 31 }
  ];
  