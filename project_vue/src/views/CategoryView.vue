<template>
  <div class="category-manager">
    <div class="category-manager__header">
      <h1>Categories</h1>
      <button v-if="$store.state.isAuthenticated" @click="showForm = !showForm">Add category</button>
    </div>

    <form v-if="showForm" @submit.prevent="addCategory" class="category-form">
      <input v-model="newCategory.name" placeholder="Category name" required>
      <button type="submit">Add category</button>
    </form>

    <div v-if="categoryToEdit" class="edit-category-form">
      <form @submit.prevent="saveCategory">
        <input v-model="categoryToEdit.name" placeholder="Category name" required>
        <button type="submit">Save category</button>
      </form>
    </div>

    <div class="category-list">
      <div v-for="category in categories" :key="category.id" class="category-item" @click="getTasksByCategory(category.id)">
        <button v-if="$store.state.isAuthenticated" @click="editCategory(category)">Edit</button>
        <button v-if="$store.state.isAuthenticated" @click="deleteCategory(category)">Delete</button>
        <h2>{{ category.name }}</h2>
        <div v-if="category.id === selectedCategoryId" class="tasks">
          <div v-for="task in tasksByCategory(category.id)" :key="task.id" class="task">
            <h3>{{ task.title }}</h3>
            <p>{{ task.description }}</p>
            <p>Status: {{ task.completed ? 'Completed' : 'Incomplete' }}</p>
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

<style scoped>
.category-manager {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.category-manager__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.category-form {
  margin-bottom: 20px;
}

.edit-category-form {
  margin-bottom: 20px;
}

.category-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}

.category-item button {
  margin-right: 10px;
}

.category-item h2 {
  margin: 0;
}

.tasks {
  margin-left: 20px;
}

.task {
  border: 1px solid #eee;
  padding: 5px;
  margin-top: 5px;
}

.task h3 {
  margin: 0;
}

.task p {
  margin: 5px 0;
}
.category-item:hover{
  cursor: pointer;
}
</style>