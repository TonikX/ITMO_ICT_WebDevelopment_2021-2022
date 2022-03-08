# Простой компонент для формы 

Поддерживает отображение серверных ошибок в стандартном формате Django, сброс ошибок при вводе, все возможные типы полей и прочее

```js
/**
 * Import Vue.js
 */
import Vue from "vue";

/**
 * Import vue-goodshare single element
 */
import VueGoodshareFacebook from "vue-goodshare/src/providers/Facebook.vue";

const app = new Vue({
  el: "#app",
  components: {
    VueGoodshareFacebook
  }
});
```

Add component to HTML template (with attributes):

```html
<div id="app">
  <app-input
    v-model="form.username"
    label="Имя пользователя"
    placeholder="Ваше имя пользователя"
    :errors.sync="errors"
    :errors-key="'username'"
    required
  />
</div>
```
