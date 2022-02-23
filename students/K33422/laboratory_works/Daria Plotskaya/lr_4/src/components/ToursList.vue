<template>
    <b-container>
        <ul class="list-unstyled">
            <b-media class='mb-3 media' tag="li" v-for="(el, index) in toursList" :key="index">
                <template #aside>
                    <router-link class="link-tour" v-if="el" :to="'/tours/' + el.id">
                        <b-icon icon="arrow-up-right" style="width: 90px; height: 90px;" aria-hidden="true"></b-icon>
                    </router-link>
                </template>
                <h4 class="mt-0 mb-2">{{el.destination}}</h4>
                <p class="mb-3">
                    Вы отправитсь в удивительное путешествие с {{ el.date_from }} числа. И до {{ el.date_to }} вас ждет незабываемый отдых. В одном из знаменитых отелей города:
                    {{ el.hotel }}. Стоимость путевки всего: {{ el.price }}. Количество мест ограничего: {{ el.empty_count }}
                </p>
            </b-media>
        </ul>
    </b-container>
</template>

<script>
    import {mapGetters} from "vuex";

    export default {
        name: "ToursList",
        mounted() {
            this.$store.dispatch('mountedProfile')
        },
        computed: {
            ...mapGetters({
                username: 'username',
                toursList: 'toursList',
            })
        },
    }
</script>

<style>
    .media {
        display: flex;
        align-items: start!important;
        justify-content: start!important;
        text-align: start;
        border: 1px solid black;
        border-radius: 10px;
        padding: 15px 20px;
    }
    .link-tour {
    }
    .link-tour:hover {
        background: rgba(0, 0, 0, 0.05);
    }
    .link-tour:active {
        background: rgba(0, 0, 0, 0.15);
    }
</style>