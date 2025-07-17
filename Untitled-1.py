# ----------------------------
# Настройки сервера
# ----------------------------
# Укажи здесь путь к папке с сайтом
# Например: "site", "build", "." (текущая папка)
SITE_DIRECTORY = "."

# Укажи порт (по желанию)
PORT = 8000

# ----------------------------
# Не трогай ниже если не хочешь менять логику
# ----------------------------
import http.server
import socketserver
import os
import webbrowser

# Переходим в нужную папку
os.chdir(SITE_DIRECTORY)

# Создаем обработчик
Handler = http.server.SimpleHTTPRequestHandler

# Запускаем сервер
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен!")
    print(f"Папка: {os.path.abspath(SITE_DIRECTORY)}")
    print(f"Адрес: http://localhost:{PORT}")

    # Открыть в браузере автоматически
    webbrowser.open(f"http://localhost:{PORT}")

    httpd.serve_forever()