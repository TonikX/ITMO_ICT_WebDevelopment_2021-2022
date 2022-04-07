# Регистрация и Авторизация



###Регистрация POST
*protocol:Host:port/api/auth/users/* <br>
**Header** <br>
* Content-Type:multipart/form-data <br>
* Accept: application/json<br>

**Body**

* username: username <br>
* password: password <br>


###Авторизация POST
*protocol:Host:port/api/auth/token/login/* <br>
**Header** <br>
* Content-Type:multipart/form-data <br>
* Accept: application/json<br>
* Authorization: Token token<br>

**Body**

* username: username <br>
* password: password <br>


###Изменение, получение, удаление данных GET / PATCH / PUT / DELETE
*protocol:Host:port/api/auth/users/me/* <br>
**Header** <br>
* Content-Type:multipart/form-data <br>
* Accept: application/json<br>
* Authorization: Token token<br>

**Body**

optional