<template>
    <div class="card p-3">
        <b-row>
            <img class="col-md-4 mt-0 card-img-top" src="@/assets/img/property_image.jpg" >
            <div class="col-md-8 card-body">
                <p class="card-location"><b-icon icon="flag" font-scale="0.99" class="fa"></b-icon>{{ bookingItem.property.city }}</p>
                <!-- <p class="card-rating"><span class="red-star">★</span> {{ propertyItem.review_score}}
                    <span class="reviews">({{ propertyItem.review_nr}} reviews)</span>
                </p> -->
                <p class="card-text">{{ bookingItem.property.title }}</p>
                <p class="card-text">Check in: {{ bookingItem.checkin }}</p>
                <p class="card-text">Check out: {{ bookingItem.checkout }}</p>
                <p class="card-text">Price: ${{ bookingItem.total_price }}</p>
                <p class="card-text">Status: {{ bookingItem.status }}</p>

                <button v-if="bookingItem.status !== 'CANCELLED'" class="btn btn-danger col-md-4" v-on:click="cancelBooking">Cancel booking</button>
            </div>
        </b-row>
    </div>
</template>

<script>
export default {
    name: 'BookingCardDetail',

    props: {
        bookingItem: Object
    },
    created () {
        console.log(this.bookingItem.status)
    },
    methods: {
        async cancelBooking () {
            console.log('cancelling booking...')
            const url = `http://127.0.0.1:8000/booking/update/${this.bookingItem.id}`

            const response = await fetch(url, {
                method: 'PATCH',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    status: 'CANCELLED'
                })
            })
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
