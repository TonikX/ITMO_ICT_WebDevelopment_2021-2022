<template>
    <main role="main">
        <b-container class="pb-4">
            <div class="pb-3" v-if="isLoaded == false">Loading...</div>
            <div class="pb-3" v-if="isNotFound == true">Results not found</div>
            <v-row v-for="index in 5" :key="index" v-else>
                <booking-card
                    v-for="bookingItem in bookingItems.slice((index - 1) * 3, Math.min((index - 1) * 3 + 3, bookingItems.length))"
                    :key="bookingItem.id"
                    :booking-item="bookingItem"
                    class=""
                />
            </v-row>
        </b-container>
    </main>
</template>

<script>
import BookingCard from '@/components/BookingCard.vue'

export default {
    name: 'Bookings',
    components: {
        BookingCard
    },

    data: () => ({
        bookingItems: [],
        isLoaded: false,
        isNotFound: false
    }),

    created () {
        this.getBookings()
    },

    methods: {
        async getBookings () {
            this.isLoaded = false

            const url = `http://127.0.0.1:8000/booking/list/?tenant=${this.$store.state.id}`

            const response = await fetch(url, {
                method: 'GET'
            })

            const data = await response.json()

            this.bookingItems = data.reverse()
            this.isNotFound = this.bookingItems === undefined || this.bookingItems.length === 0
            this.isLoaded = true
        }
    }
}
</script>
