
<template>
  <div id="app">
    <ImageForm @imageUploaded="loadImages" />
    <ImageList :images="images" @imageDeleted="loadImages" />
  </div>
</template>

<script>
import ImageForm from "@/components/ImageForm.vue";
import ImageList from "@/components/ImageList.vue";
import axios from "axios";

export default {
  components: {
    ImageForm,
    ImageList,
  },
  data() {
    return {
      images: [],
    };
  },
  methods: {
    async loadImages() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/images/");

        this.images = response.data;
      } catch (error) {
        console.error("Ошибка при загрузке изображений:", error);
      }
    },
  },
  mounted() {
    this.loadImages();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
