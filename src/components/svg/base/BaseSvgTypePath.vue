<template lang="">
    <svg xmlns="http://www.w3.org/2000/svg" :width="width" :height="height" :viewBox="viewBox" :aria-labelledby="iconName">
        <title :id="iconName" :lang="en">{{iconName}}</title>
        <g :fill="iconColor">
            <slot />
        </g>
    </svg>
</template>
<script>
export default {
    props: {
        iconName : {
            type : String,
            default : ""
        },
        iconColor : {
            type : String,
            default : "currentColor"
        },
        width : {
            type : String,
            default : '20',
        },
        height : {
            type : String,
            default : '20',
        },
        viewBox : {
            type : String,
            default : "0 0 24 24",
        }
    }
}
</script>