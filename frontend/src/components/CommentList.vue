<template>
  <ul class="comments">
      <li v-for="comment in comments" :key="comment.id">
          <div class="comment-item">
            
              <comment-item :comment="comment" @edit="onEdit"/>
          </div>
      </li>

      <li v-if="comments.length <= 0">
          입력된 댓글이 없습니다.
      </li>
  </ul>
</template>

<script>
import CommentItem from './CommentItem.vue'

export default {
    name: 'CommentList',

    components: {CommentItem},

    props: {
        comments: {
            type: Array,
            default(){
                return [];
            }
        }
    },

    methods: {
        onEdit({ id,comment}){
            console.log(id,comment);
        }
    }
}
</script>

<style>

</style>