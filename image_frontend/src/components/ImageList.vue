<template>
    <div>
      <ul>
        <li v-for="image in images" :key="image.id">
          {{ image.description }}
          <button @click="deleteImage(image.id)">Delete</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: {
      images: Array,
    },
    methods: {
      async deleteImage(imageId) {
        try {
          // Выполняем DELETE-запрос к API для удаления изображения по ID
          await axios.delete(`http://127.0.0.1:8000/images/${imageId}/`);
  
          // После успешного удаления вызываем событие @imageDeleted
          this.$emit('imageDeleted');
        } catch (error) {
          console.error(`Ошибка при удалении изображения с ID ${imageId}:`, error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 10px;
  }
  </style>
  