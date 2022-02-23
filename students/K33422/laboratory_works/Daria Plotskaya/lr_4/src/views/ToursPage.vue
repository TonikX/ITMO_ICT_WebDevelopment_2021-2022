<template>
    <main>
        <h2>Путевка в {{ tourElement.destination }}</h2>
        <b-container>
            <b-row>
                <Card :tourElement="tourElement"/>
                <Form />
                <Comment v-if="showComments" />
            </b-row>
            <div class="mt-5 mb-3">
                <b-carousel
                        id="carousel-1"
                        v-model="slide"
                        :interval="4000"
                        controls
                        indicators
                        background="#ababab"
                        img-width="1024"
                        img-height="480"
                        style="text-shadow: 1px 1px 2px #333;"
                        @sliding-start="onSlideStart"
                        @sliding-end="onSlideEnd"
                >
                    <b-carousel-slide
                            caption="First slide"
                            text="Nulla vitae elit libero, a pharetra augue mollis interdum."
                            img-src="https://picsum.photos/1024/480/?image=52"
                    ></b-carousel-slide>
                    <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
                        <h1>{{ tourElement.destination }}</h1>
                    </b-carousel-slide>
                    <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>
                    <b-carousel-slide>
                        <template #img>
                            <img
                                    class="d-block img-fluid w-100"
                                    width="1024"
                                    height="480"
                                    src="https://picsum.photos/1024/480/?image=55"
                                    alt="image slot"
                            >
                        </template>
                    </b-carousel-slide>
                </b-carousel>
            </div>
        </b-container>
    </main>
</template>

<script>
    import {mapGetters} from "vuex";
    import Card from "@/components/ToursPage/Card";
    import Comment from "@/components/ToursPage/Comment";
    import Form from "@/components/ToursPage/Form";

    export default {
        name: "ToursPage",
        components: {Form, Comment, Card},
        data() {
            return {
                slide: 0,
                sliding: null
            }
        },
        mounted() {
            this.$store.dispatch('toursElement', this.$route.params.id )
        },
        methods: {
            show(flag) {
                this.$store.commit('setShowComments', flag)
            },
            onSlideStart() {
                this.sliding = true
            },
            onSlideEnd() {
                this.sliding = false
            },
        },
        computed: {
            ...mapGetters({
                tourElement: 'tourElement',
                showComments: 'showComments',
            })
        },
    }
</script>

<style scoped>

</style>