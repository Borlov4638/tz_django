<template>
  <div>
    <h2>Загрузка изображения</h2>
    <form @submit.prevent="submitForm">
      <label for="description">Описание:</label>
      <input type="text" v-model="description" id="description" required>

      <label for="image">Изображение:</label>
      <input type="file" @change="handleImageChange" id="image" accept="image/*" required>

      <button type="submit">Отправить</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      description: '',
      base64Data: null,
    };
  },
  methods: {
    handleImageChange(event) {
      const fileReader = new FileReader();

      fileReader.onload = () => {
        this.base64Data = fileReader.result;
      };

      // Чтение файла в формате base64
      fileReader.readAsDataURL(event.target.files[0]);
    },
    async submitForm() {
      try {
        // Отправляем POST-запрос на сервер с данными формы
        const response = await axios.post('http://127.0.0.1:8000/images/', {
          description: this.description,
          base64_data: this.base64Data,
        }, {headers:{"Content-Type": 'application/json'}});

        // После успешной отправки сбрасываем значения полей формы
        this.description = '';
        this.base64Data = null;

        // Вызываем событие для сообщения родительскому компоненту об успешной отправке
        this.$emit('imageUploaded');

        console.log('Изображение успешно отправлено:', response.data);
      } catch (error) {
        console.error('Ошибка при отправке изображения:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Ваши стили формы здесь */
</style>
