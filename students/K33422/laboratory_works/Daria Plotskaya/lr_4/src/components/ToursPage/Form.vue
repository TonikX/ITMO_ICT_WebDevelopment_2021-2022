<template>
    <b-col cols="4">
        <h5>Заказать билеты</h5>
        <form @submit.prevent="onSubmit(form)" class="form-container">
            <div class="mb-3">
                <label for="input-default">На какое имя бронировать:</label>
                <b-form-input v-model="form.name" id="input-default" placeholder="Введите имя"></b-form-input>
            </div>
            <div class="mb-3">
                <label for="input-default">Количество людей:</label>
                <b-form-input v-model="form.count" id="input-default" placeholder="Введите число"></b-form-input>
            </div>
            <b-button type="submit" variant="outline-primary">Заказать билеты</b-button>
            <p v-if="totalPrice" class="mt-3">
                {{ totalPrice }} - итоговая цена, ждите с вами свяжуться
            </p>
        </form>
    </b-col>
</template>

<script>
    import {mapGetters} from "vuex";

    export default {
        name: "Form",
        data() {
            return {
                form: {
                    name: "",
                    tour: this.$route.params.id,
                    count: "",
                }
            };
        },
        destroyed: function () {
            this.$store.commit('setTotalPrice', null)
        },
        methods: {
            onSubmit(form) {
                this.$store.dispatch('reservations', form)
            }
        },
        computed: {
        ...mapGetters({
                totalPrice: 'totalPrice',
            })
        },
    }
</script>

<style scoped>
.form-container {
    width: 100%;
    height: 400px;
    padding: 20px;
    text-align: start;
    border: 1px solid rgba(0, 0, 0, 0.22);
    border-radius: 4px;
    background: rgba(186, 186, 186, 0.19);
}
</style>