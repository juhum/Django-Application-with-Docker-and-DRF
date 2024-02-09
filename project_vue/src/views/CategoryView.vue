<template>
  <div>
    <div class="home">
      Categories:
    </div>
    <div class="category">
      <div v-for="category in Categories" :key="category.id" @click="getTasksByCategory(category.id)">
        <h1>T: {{ category.name }}</h1>
        <div v-if="category.id === selectedCategoryId" class="tasks">
          <div v-for="task in Tasks" :key="task.id">
            <h3>T: {{ task.title }}</h3>
            <h3>D: {{ task.description }}</h3>
            <h3>{{ task.completed }}</h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CategoryView',
  data() {
    return {
      Categories: [],
      Tasks: [],
      selectedCategoryId: null
    };
  },
  mounted() {
    this.getCategories();
    document.title = "Categories";
  },
  methods: {
    getCategories() {
      axios
        .get('/api/v1/category/')
        .then(response => {
          this.Categories = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getTasksByCategory(categoryId) {
      if (this.selectedCategoryId === categoryId) {
        this.selectedCategoryId = null;
        this.Tasks = []; 
      } else {
        this.selectedCategoryId = categoryId;
        axios
          .get(`/api/v1/tasks/category/${categoryId}/`)
          .then(response => {
            this.Tasks = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  }
};
</script>

