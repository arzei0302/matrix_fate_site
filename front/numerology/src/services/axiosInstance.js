import axios from "axios";

const BASE_URL = "https://matrixaaa.duckdns.org";

// Создаём инстанс axios
const api = axios.create({
  baseURL: BASE_URL,
});

// Добавляем интерцептор для токена
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("accessToken");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
