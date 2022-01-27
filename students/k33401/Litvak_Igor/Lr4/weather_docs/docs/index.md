# Weather frontend

Please refer to this manual to learn how to use the website

## Pages

* `/` - Index page with weather
* `/login` - Login page
* `/register` - Registration page
* `/profile` - Profile page where you can change your favourite cities or your account information

## Authentication

Authentication is done with JWT tokens. Tokens are refreshed automatically.

## Storage

Storage is done with [Vuex](https://vuex.vuejs.org/) library and persists through user session by [Vuex-persistedstate](https://www.npmjs.com/package/vuex-persistedstate) library
