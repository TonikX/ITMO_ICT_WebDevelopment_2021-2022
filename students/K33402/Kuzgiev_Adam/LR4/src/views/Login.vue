<template>
    <v-layout align-center justify-center>
        <v-flex xs12 sm10 md8>
            <v-card class="elevation-12">
                <v-form @submit.prevent="login(form)">
                    <v-toolbar dark color="primary">
                        <v-toolbar-title>Login form</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                            <v-text-field
                                    v-model="form.username"
                                    prepend-icon="mdi-account"
                                    name="login"
                                    label="Login"
                                    type="text"
                            ></v-text-field>
                            <v-text-field
                                    v-model="form.password"
                                    id="password"
                                    prepend-icon="mdi-lock"
                                    name="password"
                                    label="Password"
                                    type="password"
                            ></v-text-field>
                    </v-card-text>
                    <v-card-actions>
                        <router-link to="/registration">
                            <v-btn type="button" color="primary" elevation="2"
                                   outlined>
                                Если нет аккаунта, зарегестрируйтесь
                            </v-btn>
                        </router-link>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" type="submit">Login</v-btn>
                    </v-card-actions>
                </v-form>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
    export default {
        name: 'Login',
        data() {
            return {
                form: {
                    username: "",
                    password: "",
                }
            };
        },
        methods: {
            login(form) {
                console.log(form)
                this.$store.dispatch('LOGIN', form)
            }
        },
    }
</script>