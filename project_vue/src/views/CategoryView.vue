<template>
  <div>
    <div class="home">
      Categories:
      <button v-if="$store.state.isAuthenticated" @click="showForm = !showForm">Add category</button>
      <form v-if="showForm" @submit.prevent="addCategory">
        <input v-model="newCategory.name" placeholder="Category name" required>
        <button type="submit">Add category</button>
      </form>
      <form v-if="categoryToEdit" @submit.prevent="saveCategory">
        <input v-model="categoryToEdit.name" placeholder="Category name" required>
        <button type="submit">Save category</button>
      </form>
    </div>
    <div class="category">
      <div v-for="category in categories" :key="category.id">
        <button v-if="$store.state.isAuthenticated" @click="editCategory(category)">Edit</button>
        <button v-if="$store.state.isAuthenticated" @click="deleteCategory(category)">Delete</button>
        <h1>C: {{ category.name }}</h1>
        <div v-if="category.id === selectedCategoryId" class="tasks">
          <div v-for="task in tasksByCategory(category.id)" :key="task.id">
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
      categories: [],
      tasks: [],
      selectedCategoryId: null,
      newCategory: { name: '' },
      categoryToEdit: null,
      showForm: false
    };
  },
  mounted() {
    this.getCategories();
    document.title = "Categories";
  },
  methods: {
    getCategories() {
      axios.get('/api/v1/category/')
        .then(response => {
          this.categories = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    addCategory() {
      axios.post('/api/v1/category/', this.newCategory, {
          headers: {
            'Authorization': `token ${localStorage.token}`,
          }
        })
        .then(response => {
          this.categories.push(response.data);
          this.newCategory = { name: '' };
          this.showForm = false;
        })
        .catch(error => {
          console.error('Error creating category:', error);
        });
    },
    editCategory(category) {
      this.categoryToEdit = Object.assign({}, category);
    },
    saveCategory() {
      axios.put(`/api/v1/category/${this.categoryToEdit.id}/`, this.categoryToEdit, {
          headers: {
            'Authorization': `token ${localStorage.token}`,
          }
        })
        .then(response => {
          const index = this.categories.findIndex(cat => cat.id === this.categoryToEdit.id);
          this.categories.splice(index, 1, response.data);
          this.categoryToEdit = null;
        })
        .catch(error => {
          console.error('Error updating category:', error);
        });
    },
    deleteCategory(category) {
      axios.delete(`/api/v1/category/${category.id}/`, {
          headers: {
            'Authorization': `token ${localStorage.token}`,
          }
        })
        .then(() => {
          this.categories = this.categories.filter(cat => cat.id !== category.id);
          console.log('Category deleted successfully');
        })
        .catch(error => {
          console.error('Error deleting category:', error);
        });
    },
    getTasksByCategory(categoryId) {
      if (this.selectedCategoryId === categoryId) {
        this.selectedCategoryId = null;
        this.tasks = [];
      } else {
        this.selectedCategoryId = categoryId;
        axios.get(`/api/v1/tasks/category/${categoryId}/`)
          .then(response => {
            this.tasks = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
    tasksByCategory(categoryId) {
      return this.tasks.filter(task => task.category_id === categoryId);
    }
  }
};
</script>
