<template>
    <div>
    <div style = "float:left" >
        <b-button block class="mybutton mb-2" @click="movelost()">주인으로 작성</b-button>
    </div>
    <div style = "float:right">
        <b-button block class="mybutton mb-2" @click="movefind()">발견자로 작성</b-button>
    </div>
    </div>
</template>

<script>
export default {
    name: "Selectnotice",

    methods:{
        movelost(){
            this.$router.push({path: "/articles_lost/create"});
        },
        movefind(){
            this.$router.push({path: "/articles_find/create"});
        }
    }

}
</script>

<style>

</style>