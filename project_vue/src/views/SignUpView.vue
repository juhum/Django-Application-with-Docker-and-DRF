<template>
    <div class="container">
        <h1>Sign Up</h1>
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

            <div class="field">
                <label>Confirm Password</label>
                <div class="control">
                    <input type="password" class="input" v-model="password2">
                </div>
            </div>

            <div class="notification" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <div class="field">
                <div class="control">
                    <button class="btn">Sign Up</button>
                </div>
            </div>

            <hr>
            <router-link to="/login">Already have an account ?</router-link>
        </form>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    name: "SignUpView",
    data (){
        return {
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    mounted(){
    document.title = "Sign Up"
    },
    methods: {
        submitForm(){
            this.errors = []

            if (this.username === ''){
                this.errors.push("Username is missing")
            }

            if (this.password === ''){
                this.errors.push("Password is too short")
            }

            if (this.password !== this.password2){
                this.errors.push("Passwords doesn\'t match")
            }

            if (!this.errors.length){
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                .post("/api/v1/users/", formData)
                .then(response =>{
                    this.registrationMessage = 'Registration successful!';
                    this.$router.push('/login')
                }).catch(error =>{
                    if (error.response){
                        for (const property in error.response.data) {   //FIX ERROS SHOWING
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                        console.log(JSON.stringify(error.response.data))
                    } else if(error.message) {
                        this.errors.push('Something went wrong. Please try again')
                        console.log(JSON.stringify(error))
                    }
                })
                
                
            }
        }
    }
}
</script>
