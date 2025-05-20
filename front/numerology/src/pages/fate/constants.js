import sahasrara from "../../assets/1.jpeg";
import ajna from "../../assets/2.jpeg";
import vishuddha from "../../assets/3.jpeg";
import anahata from "../../assets/4.jpeg";
import manipura from "../../assets/5.jpeg";
import svadhisthana from "../../assets/6.jpeg";
import muladhara from "../../assets/7.jpeg";
export const newChakraData = [
  { name: "7. Сахасрара", color: "#ffe6e6", icon: sahasrara },
  { name: "6. Аджна", color: "#ffeedd", icon: ajna },
  { name: "5. Вишудха", color: "#fff8e6", icon: vishuddha },
  { name: "4. Анахата", color: "#e6ffe6", icon: anahata },
  { name: "3. Манипура", color: "#e6f7ff", icon: manipura },
  { name: "2. Свадхистана", color: "#e6f0ff", icon: svadhisthana },
  { name: "1. Муладхара", color: "#f3e6ff", icon: muladhara }
];

export const newPersonalInfo = [
  {
    title: "searchSelf",
    description: "searchSelfDesc",
    skyLabel: "sky",
    skyKey: "r",
    earthLabel: "earth",
    earthKey: "s",
    resultKey: "y",
    spiritLabel: "spiritualHarmony",
    spiritKey: "w",
    question: "spiritualQuestion1"
  },
  {
    title: "socialization",
    description: "socializationDesc",
    skyLabel: "sky",
    skyKey: "t",
    earthLabel: "earth",
    earthKey: "u",
    resultKey: "v",
    spiritLabel: "planetary",
    spiritKey: "x",
    question: "spiritualQuestion2"
  }
];


export const months = [
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

export const years = Array.from({ length: 100 }, (_, i) => 2025 - i);

