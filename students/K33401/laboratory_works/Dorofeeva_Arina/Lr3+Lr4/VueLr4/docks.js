import axios from "axios";

/**
 * Делает POST запрос на сервер, запрашивая токен авторизации.
 * Поле authData имеет следующий вид
 * {
 * username: string,
 * password: string
 * }
 * В ответе ожидает токен, который сохраняется в
 * localstorig
 * А также записывает токен в поле token состояения приложения
 * После чего редиректит в личный кабинет.
 *
 * В случае неудачной попытки запроса, ожидает responseError,
 * который сохраняется в loginError для дальнейшего вывода в виде сообщения
 * пользователю
 *
 * @param {object} state - локальное состояние приложения
 * @param {object} authData - данные пользователя
 * @login
 */

function login(state, authData) {

    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }
    const {username, password} = authData;
    const body = JSON.stringify({username, password});


    axios.post(URL + '/auth/token/login/', body, config).then(res => {
        localStorage.setItem("token", res.data.auth_token);
        state.token = res.data.auth_token
        router.push({
            path: '/cabinet',
        });
    }).catch(err => {
        state.loginError = err.response.data
    })
}


/**
 * Делает Post запрос на сервер для регистрации пользователя
 * Поле authData имеет следующий вид
 * {
 * username: string,
 * password: string
 * }
 * В случае неудачной попытки запроса, ожидает responseError,
 * которой сохраняется в registrationError, для дальнейшего вывода в виде особщения
 * пользователю
 *
 * @param {object} state - локальное состояние приложения
 * @param {object} authData - данные пользователя
 * @registerUser
 */
function registerUser(state, authData) {

    const config = {
        headers: {
            "Content-Type": 'application/json'
        }
    }
    axios.post(URL + `/auth/users/`, authData, config).then(res => {
        router.push({
            path: "/sign-in"
        })
    }).catch(err => {
        state.registrationError = err.response.data
    })
}


/**
 * Делает DELETE запрос видео пользователя на сервер.
 * Поле data имеет следующий вид
 * {
 * id: string,
 * }
 * В случае успешноого ответа удаляет по id видео из локального состояния
 *
 *
 * @param {object} state - локальное состояние приложения
 * @param {object} data - данные видео
 *
 * @removeVideo
 */
function removeVideo(state, data) {
    const token = state.token || localStorage.getItem('token');
    const config = tokenConfig(token)
    axios.delete(URL + `/api/videos-of-user/${data.id}`, config).then(res => {
        state.videosOfUser = state.videosOfUser.filter(video => video.id !== data.id)
    }).catch(err => {
        console.log(err)
    })
}


/**
 * Делает GET запрос видео пользователя на сервер.
 *
 * в ответе ожидается
 * {
 * id: string | number,
 * tags: string,
 * link: string
 * }
 *
 * В случае успешноого ответа сохраняет видео в локальное состояние - videosOfUser
 *
 * @param {object} state - локальное состояние приложения
 *
 * @getVideosOFUser
 */
function getVideosOFUser(state) {
    const token = localStorage.getItem('token');
    const config = tokenConfig(token)
    axios.get(URL + `/api/videos-of-user/?owner=${state.userData.id}`, config).then(res => {
        state.videosOfUser = res.data;
    }).catch(err => {
        console.log(err)
    })
}