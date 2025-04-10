import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header/Header"; // Ваш компонент Header
import Footer from "./components/Footer/Footer"; // Ваш компонент Footer
import MyMatrices from "./components/MyMatrices/MyMatrices";  // Компонент для "Мои Матрицы"
import Tariffs from "./components/Tariffs/Tariffs";        // Компонент для "Тарифы"
import ViewHistory from "./components/ViewHistory/ViewHistory"; // Компонент для "История просмотров"
import Fate from "./pages/fate/fate"; // Пример других страниц
import Finance from "./pages/finance/finance";
import Compatibility from "./pages/compatibility/compatibility";
import Child from "./pages/child/child";
import Prognoses from "./pages/progonoses/prognoses";
import Cabinet from "./pages/cabinet/cabinet"; // Компонент Cabinet
import Additional from "./pages/additional/additional";
import Question from "./pages/additional/question/qustion";
import { Provider } from "react-redux";
import store from "./store/store";
import "./App.css";
import './i18n'
function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <Router>
          <Header />
          <Routes>
            {/* Основные маршруты */}
            <Route path="/" element={<Fate />} />
            <Route path="/finance" element={<Finance />} />
            <Route path="/compatibility" element={<Compatibility />} />
            <Route path="/child" element={<Child />} />
            <Route path="/prognoses" element={<Prognoses />} />
            <Route path="/additional" element={<Additional />} />
            <Route path="/additional/question" element={<Question />} />

            {/* Маршрут для кабинета с вложенными маршрутами */}
            <Route path="/cabinet" element={<Cabinet />}>
              <Route path="mymatrices" element={<MyMatrices />} />
              <Route path="tariffs" element={<Tariffs />} />
              <Route path="viewhistory" element={<ViewHistory />} />
            </Route>

          </Routes>
          <Footer />
        </Router>
      </Provider>
    </div>
  );
}

export default App;
