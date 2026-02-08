const API_URL = "http://localhost:8000/api";

export const fetchSensors = async () =>
  fetch(`${API_URL}/sensors`).then(res => res.json());

export const fetchAlerts = async () =>
  fetch(`${API_URL}/alerts`).then(res => res.json());
