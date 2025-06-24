import axios from "axios";

const BASE_URL = "https://numerology-calculator.fi/api";

const api = axios.create({
  baseURL: BASE_URL,
});

// 👉 Добавляем access token в каждый запрос
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("accessToken");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// 👉 Обновляем access token при 401 Unauthorized
api.interceptors.response.use(
    response => response,
    async (error) => {
      const originalRequest = error.config;

      // Если access token истёк, и это первый повтор
      if (error.response?.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;

        const refreshToken = localStorage.getItem("refreshToken");
        if (!refreshToken) {
          return Promise.reject(error);
        }

        try {
          const res = await axios.post(`${BASE_URL}/matrix_auth/token/refresh/`, {
            refresh: refreshToken,
          });

          const newAccessToken = res.data.access;
          localStorage.setItem("accessToken", newAccessToken);

          // Применить новый токен и повторить запрос
          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
          return api(originalRequest); // повторяем исходный запрос
        } catch (refreshError) {
          console.error("Ошибка при обновлении токена:", refreshError);
          localStorage.removeItem("accessToken");
          localStorage.removeItem("refreshToken");
          return Promise.reject(refreshError);
        }
      }

      return Promise.reject(error);
    }
);

export default api;
