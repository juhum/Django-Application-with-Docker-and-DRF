<template>
  <div class="task-manager">
    <div class="task-manager__header">
      <h1>Tasks</h1>
      <button v-if="$store.state.isAuthenticated" @click="showForm = !showForm">Add task</button>
    </div>

    <form v-if="showForm" @submit.prevent="addTask" class="task-form">
      <input v-model="newTask.title" placeholder="Task title" required>
      <input v-model="newTask.description" placeholder="Task description" required>
      <select v-model="newTask.category" required>
        <option disabled value="">Please select a category</option>
        <option v-for="category in categories" :value="category.id" :key="category.id">
          {{ category.name }}
        </option>
      </select>
      <label><input type="checkbox" v-model="newTask.completed"> Completed</label>
      <button type="submit">Submit task</button>
    </form>

    <div v-if="taskToEdit" class="edit-task-form">
      <form @submit.prevent="saveTask">
        <input v-model="taskToEdit.title" placeholder="Task title" required>
        <input v-model="taskToEdit.description" placeholder="Task description" required>
        <select v-model="taskToEdit.category" required>
          <option disabled value="">Please select a category</option>
          <option v-for="category in categories" :value="category.id" :key="category.id">
            {{ category.name }}
          </option>
        </select>
        <label><input type="checkbox" v-model="taskToEdit.completed"> Completed</label>
        <button type="submit">Save task</button>
      </form>
    </div>

    <div class="task-list">
      <div v-for="task in Tasks" :key="task.id" class="task-item">
        <button v-if="$store.state.isAuthenticated" @click="editTask(task)">Edit</button>
        <button v-if="$store.state.isAuthenticated" @click="deleteTask(task)">Delete</button>
        <h2>{{ task.title }}</h2>
        <p>{{ task.description }}</p>
        <p>Category: {{ task.category_name }}</p>
        <p>Status: {{ task.completed ? 'Completed' : 'Incomplete' }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TaskView',
  data() {
    return {
      Tasks: [],
      newTask: {
        title: '',
        description: '',
        category: '',
        completed: false
      },
      showForm: false,
      taskToEdit: null,
      categories: []
    }
  },
  components: {

  },
  mounted() {
    this.getTasks();
    document.title = "Tasks"
    this.getCategories();
  },
  methods: {
    getTasks() {
      axios
        .get('/api/v1/tasks/')
        .then(response => {
          this.Tasks = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getCategories() {
      axios
        .get('/api/v1/category/')
        .then(response => {
          this.categories = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
addTask(){
      axios.post('/api/v1/tasks/', this.newTask, {
        headers: {
          'Authorization': `token ${localStorage.token}`,
        }
      })
      .then(response => {
        this.Tasks.push(response.data);
        // Clear the form
        this.newTask = { title: '', description: '', category: '', completed: false };
        // Hide the form
        this.showForm = false;
      })
      .catch(error => {
        console.error('Error creating task:', error);
      });
    },
        editTask(task) {
      this.taskToEdit = Object.assign({}, task);
    },
    saveTask() {
      axios.put(`/api/v1/tasks/${this.taskToEdit.id}/`, this.taskToEdit, {
        headers: {
          'Authorization': `token ${localStorage.token}`,
        }
      })
      .then(response => {
        const index = this.Tasks.findIndex(task => task.id === this.taskToEdit.id);
        this.Tasks.splice(index, 1, response.data);
        this.taskToEdit = null;
      })
      .catch(error => {
        console.error('Error updating task:', error);
      });
    },
    deleteTask(task) {
      axios.delete(`/api/v1/tasks/${task.id}/`)
        .then(() => {
          this.Tasks = this.Tasks.filter(t => t.id !== task.id);
          console.log('Task deleted successfully');
        })
        .catch(error => {
          console.error('Error deleting task:', error);
        });
    }
  }
};
</script>


<style scoped>
.task-manager {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.task-manager__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.task-form {
  margin-bottom: 20px;
}

.edit-task-form {
  margin-bottom: 20px;
}

.task-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}

.task-item button {
  margin-right: 10px;
}

.task-item h2 {
  margin: 0;
}

.task-item p {
  margin: 5px 0;
}
</style>