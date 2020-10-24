<template>
  <b-container>
    <div style="height:300px;" class="d-none d-md-flex justify-content-between">
      <img class="" :src="animal.image_path" style="height: 300px;">
      <b-container class="">
        <div class="row">
          <div class="col-6">
            <p>보호지 정보</p>
            <p>이름: {{animal.careplace}}</p>
            <p>주소: {{animal.careaddress}}</p>
            <p>번호: {{animal.caretel}}</p>
            <p>발견날짜: {{animal.find_date}}</p>
            <p>발견장소: {{animal.find_place}}</p>
          </div>
          <div class="col-6">
            <p>특징</p>
            <p>종: {{animal.kind}}</p>
            <p>나이(추정): {{animal.age}}</p>
            <p>특징: {{animal.characteristic}}</p>
            <p>색: {{animal.color}}</p>
            <p>성별(중성화): {{animal.sex}}({{animal.neuter}})</p>
            <p>무게: {{animal.weight}}</p>
          </div>
        </div>
      </b-container>
    </div>
    <b-row>
      <img :src="animal.thumbnail" class="col-6 d-block d-md-none" style="height:300px;">
      <div class="col-6 d-block d-md-none">
        <p>종: {{animal.kind}}</p>
        <p>특징: {{animal.characteristic}}</p>
        <p>보호지 주소: {{animal.careaddress}}</p>
        <p>보호지 번호: {{animal.caretel}}</p>
        <p>발견 날짜/장소: {{animal.find_date}}/{{animal.find_place}}</p>
        <b-button v-b-modal="modalId(animal.desertionno)" variant="warning">상세정보보기</b-button>
        <b-modal :id="'modal'+animal.desertionno" title="상세정보">
          <div class="d-flex justify-content-between">
            <div>
              <p>보호지 정보</p>
              <p>이름: {{animal.careplace}}</p>
              <p>주소: {{animal.careaddress}}</p>
              <p>번호: {{animal.caretel}}</p>
              <p>발견날짜: {{animal.find_date}}</p>
              <p>발견장소: {{animal.find_place}}</p>
            </div>
            <div>
              <p>특징</p>
              <p>종: {{animal.kind}}</p>
              <p>나이(추정): {{animal.age}}</p>
              <p>특징: {{animal.characteristic}}</p>
              <p>색: {{animal.color}}</p>
              <p>성별(중성화): {{animal.sex}}({{animal.neuter}})</p>
              <p>무게: {{animal.weight}}</p>
            </div>
          </div>
        </b-modal>
      </div>
    </b-row>
  </b-container>
</template>

<script>
export default {
  props: {
    animal: Object
    // age:나이,careaddress:보호지주소,careplace:보호지이름,caretel:보호지번호,
    // characteristic:특징,color:색,find_date:발견날짜,find_place:발견장소,image_path:사진,
    // kind:종류,neuter:중성화여부,sex:성별,thumbnail:썸네일,weight:무게
  },
  methods: {
    modalId(i) {
      return 'modal'+i
    }
  }
}
</script>

<style>

</style>