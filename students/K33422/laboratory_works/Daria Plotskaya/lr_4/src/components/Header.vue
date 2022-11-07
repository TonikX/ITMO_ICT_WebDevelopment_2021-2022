<template>
    <b-container>
        <header>
            <b-navbar toggleable="lg">
                <b-navbar-brand tag="router-link" :to="{ path: '/' }">

                </b-navbar-brand>

                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav>
                        <b-nav-item>
                            <router-link class="link" to="/">
                                Home
                            </router-link>
                        </b-nav-item>
                        <b-nav-item>
                            <router-link class="link" :to="{name: 'SignIn'}">SignIn</router-link>
                        </b-nav-item>
                        <b-nav-item>
                            <router-link class="link" :to="{name: 'SignUp'}">SignUp</router-link>
                        </b-nav-item>
                    </b-navbar-nav>

                </b-collapse>
            </b-navbar>
        </header>
    </b-container>

</template>

<script>
    export default {
        name: "Header"
    }
</script>

<style scoped>
    .link {
        height: 100%;
        width: auto;
        margin-right: 20px;
        margin-left: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    a {
        color: blue!important;
    }
    a:hover {
        background-color: transparent!important;
        color: #000057 !important;
    }
    a:focus {
        background-color: transparent!important;
    }
</style>