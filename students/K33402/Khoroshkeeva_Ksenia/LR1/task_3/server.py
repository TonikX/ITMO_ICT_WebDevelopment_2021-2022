import socket

# Создание сервера
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 5000))
conn.listen(10)

# Список предметов и оценок
subjects_and_marks = []

# Бесконечно принимаем соединения и отправляем ответы
while True:
    try:
        # Прием сообщения
        sock, address = conn.accept()
        data = sock.recv(16384).decode("utf-8")
        data = data.replace("\r", "")
        if not data:
            continue
        print(data)

        # Читаем файл index.html
        with open("index.html", "r", encoding="utf-8") as f:
            index_html = f.read()

        # Обработка запроса
        method, url, http_version = data.split("\n")[0].split(maxsplit=3)
        if method == "GET" and url == "/":
            # Для правильного GET-запроса никаких дополнительных действий
            pass
        elif method == "POST" and url == "/":
            # Для правильного POST-запроса получаем данные из формы
            form_data = data.split("\n\n", maxsplit=2)[1]
            parsed_data = [None, None]
            for pair in form_data.split("&"):
                key, value = pair.split("=", maxsplit=2)
                if key == "subject":
                    parsed_data[0] = value
                elif key == "mark":
                    parsed_data[1] = value
            if parsed_data[0] is not None and parsed_data[1] is not None:
                subjects_and_marks.append(parsed_data)
        else:
            # Если неправильный метод или неправильный URL, возвращаем 404
            response = f"HTTP/1.1 404 Not Found\n\nНет такой страницы"
            sock.send(response.encode("utf-8"))
            continue

        # Генерируем данные с оценками и добавляем их на место {} в HTML странице
        subjects_and_marks_html = "".join(f"<p>{s} - {m}</p>" for s, m in subjects_and_marks)
        index_html = index_html.format(subjects_and_marks_html)

        # Генерируем и отправляем ответ
        response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{index_html}"
        sock.send(response.encode("utf-8"))
    except KeyboardInterrupt:
        # При нажатии на ctrl+c сначала закрываем соединение
        conn.close()
        break
