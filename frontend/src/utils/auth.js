import { jwtDecode } from "jwt-decode";

export const setToken = (token) => {
  localStorage.setItem("token", token);
};

export const getToken = () => {
  const token = localStorage.getItem("token");

  if (!token) return null;

  try {
    const decoded = jwtDecode(token);
    const now = Date.now() / 1000;

    if (decoded.exp < now) {
      logoutUser();
      return null;
    }

    return token;
  } catch {
    logoutUser();
    return null;
  }
};

export const logoutUser = () => {
  localStorage.removeItem("token");
};