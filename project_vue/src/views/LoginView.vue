<template>
    <div class="container">
        <h1>Login</h1>
        <form @submit.prevent="submitForm">
            <div class="field">
                <label>Username</label>
                <div class="control">
                    <input type="text" class="input" v-model="username">
                </div>
            </div>

            <div class="field">
                <label>Password</label>
                <div class="control">
                    <input type="password" class="input" v-model="password">
                </div>
            </div>

            <div class="notification" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <div class="field">
                <div class="control">
                    <button class="btn">Login</button>
                </div>
            </div>

            <hr>
            <router-link to="/signup">Create new account</router-link>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default{
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted(){
        document.title = "Login"
    },
 methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                this.$router.push('/')
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>