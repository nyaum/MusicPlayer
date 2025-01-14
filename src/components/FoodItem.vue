
<template>
    <div v-on:click="countClicks">
        <h2>{{ foodName }}</h2>
        <p>{{ foodDesc }}</p>
        <p v-show="isFavorite">True!</p>
        <button class="btn btn-outline-secondary" v-on:click="toggleFavorite">Toggle</button>
    </div>
</template>

<script>
    export default {
        props:['foodName', 'foodDesc', 'isFavorite'],
        data() {
            return {
                foodIsFavorite: this.isFavorite
            }
        },
        methods: {
            toggleFavorite(){
                this.foodIsFavorite = !this.foodIsFavorite;
            }
        }
    }
</script>

<style>
    #app > div {
        border: dashed black 1px;
        display: inline-block;
        margin: 10px;
        padding: 10px;
        background-color: lightgreen;
    }
</style>
  