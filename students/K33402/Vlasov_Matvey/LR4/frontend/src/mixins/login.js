export default {
    data: () => ({
        error: ''
    }),
    methods: {
        async login () {
            const url = 'http://127.0.0.1:8000/auth/token/login/'

            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: this.username,
                    password: this.password
                })
            })

            const data = await response.json()
            const authToken = data.auth_token

            if (authToken !== undefined) {
                this.getData(authToken)
            } else {
                this.error = Object.values(data)[0][0].toString()
            }
        },
        async getData (authToken) {
            const url = 'http://127.0.0.1:8000/auth/users/me/'
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    Authorization: `Token ${authToken}`
                }
            })

            const myData = await response.json()
            this.getRole(myData.id)

            localStorage.setItem('authToken', authToken)
            localStorage.setItem('id', myData.id)
            localStorage.setItem('username', myData.username)
            localStorage.setItem('firstName', myData.first_name)
            localStorage.setItem('lastName', myData.last_name)

            this.$store.commit('isLoggedUpdate')
            this.$router.push('profile')
        },
        async getRole (id) {
            let role = 'tenant'
            const url = `http://127.0.0.1:8000/landlord/${id}`

            const response = await fetch(url, {
                method: 'GET'
            })

            const data = await response.json()
            if (data.user) role = 'landlord'
            localStorage.setItem('role', role)
            this.$store.commit('isLoggedUpdate')
        }
    }
}
