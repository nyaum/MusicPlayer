
<template>
    <h6>new Text</h6>
    <food-item v-for="x in foods" :food-name="x.name" :food-desc="x.desc" :is-favorite="x.favorite" :key="x"/>
    <hr>
    <h6>Some Text</h6>
    <test-item/>
    <test-item/>
    <test-item/>
    <test-item/>
</template>

<script>
  export default {
    data() {
      return {
        foods: [
          {
            name: 'text_1',
            desc: 'desc_1',
            favorite: true
          },
          {
            name: 'text_2',
            desc: 'desc_2',
            favorite: false
          },
          {
            name: 'text_3',
            desc: 'desc_3',
            favorite: true
          },
          {
            name: 'text_4',
            desc: 'desc_4',
            favorite: false
          },
        ]
      }
    },
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
