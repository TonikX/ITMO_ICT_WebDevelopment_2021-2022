# Вход
Вход пользователя в систему осуществляется по URL: /login

Для входа необходимо указать в форме адрес электронной почты и пароль.

При отправке формы отправляется POST-запрос на бэкенд по URL: /api/auth/jwt/login

В случае успешного входа, пользователь будет перенаправлен на предыдущую страницу сайта, которую он посещал.