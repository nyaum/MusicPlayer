<template lang="ko">
    <div>
        <p>{{message}}</p>
        <input v-on:input="inpCount++">
        <p>{{inpCount}}</p>
    </div>
</template>
<script>
export default {
    data() {
        return {
            message : "Some Text",
            inpCount: 0
        }
    }
}
</script>
<style lang="ko">
    
</style>