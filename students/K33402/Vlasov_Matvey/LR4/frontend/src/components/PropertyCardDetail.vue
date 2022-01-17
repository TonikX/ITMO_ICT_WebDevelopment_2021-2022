<template>
    <div class="card p-3" v-if="propertyItem.id">
        <b-row>
            <img class="col-md-4 mt-0 card-img-top" src="@/assets/img/property_image.jpg" >
            <div class="col-md-8 card-body">
                <p class="card-location"><b-icon icon="flag" font-scale="0.99" class="fa"></b-icon>{{ propertyItem.city }}</p>
                <p class="card-text"><span class="red-star">★</span> {{ grade }}
                    <span class="reviews">({{ reviewItems.length }} reviews)</span>
                </p>
                <p class="card-text">{{ propertyItem.title }}</p>
                <p class="card-text">{{ propertyItem.description }}</p>
                <p class="card-price"><span class="price">${{ Math.round(propertyItem.price) }} </span> / night</p>

                <property-booking-form :property-item="propertyItem" v-if="this.$store.state.isLogged" />
                <template v-else>
                    <b-alert show>
                        <router-link to="/login">Log in</router-link> to book this property
                    </b-alert>
                </template>
            </div>
        </b-row>
        <div class="pt-3">
            <review-card
                v-for="reviewItem in reviewItems"
                :key="reviewItem.id"
                :review-item="reviewItem"
                class=""
            />
        </div>
    </div>
</template>

<script>
import PropertyBookingForm from '@/components/PropertyBookingForm.vue'
import ReviewCard from '@/components/ReviewCard.vue'

export default {
    name: 'PropertyCardDetail',

    components: {
        PropertyBookingForm,
        ReviewCard
    },
    props: {
        propertyItemId: String
    },
    data: () => ({
        propertyItem: Object,
        reviewItems: [],
        grade: '-'
    }),
    created () {
        this.getPropertyItem()
    },
    methods: {
        async getPropertyItem () {
            const url = `http://127.0.0.1:8000/property/list/?id=${this.propertyItemId}`
            const response = await fetch(url, {
                method: 'GET'
            })

            const data = await response.json()
            if (data === undefined || data.length === 0) return
            this.propertyItem = data[0]
            this.getReviewInfo()
        },
        async getReviewInfo () {
            const url = `http://127.0.0.1:8000/review/list/?property=${this.propertyItem.id}`
            const response = await fetch(url, {
                method: 'GET'
            })

            const data = await response.json()
            if (data === undefined || data.length === 0) return

            this.reviewItems = data
            let sum = 0
            for (const i of Array(this.reviewItems.length).keys()) {
                sum += data[i].grade
            }
            this.grade = sum / this.reviewItems.length
            this.grade = +this.grade.toFixed(2)
        }
    }
}
</script>

<style scoped>
.card {
    background-color: var(--background-color-card);
}

.card-img-top {
    margin-top: 1rem;
}

.card-location {
    color: #0091ff;
}

.price {
    font-weight: bold;
}

.card-body p {
    line-height: 0.8rem;
}

p.card-text {
    line-height: 1.0rem;
}

.red-star {
    color: red;
}

.reviews {
    color: var(--color-main);
}

.fa {
    padding-right: 1.5rem;
    font-size: 1.5rem;
    width: 1rem;
}
</style>
