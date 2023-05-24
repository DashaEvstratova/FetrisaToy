	export const API_URL = 'http://localhost:8000/api';
export const WEBSOCKET_URL = (
    API_URL.replace("http", "ws").replace("/api", '/ws')
);