 <template>
<div>
  <div class="home">
    Tasks:
        <button v-if="$store.state.isAuthenticated" @click="showForm = !showForm">Add task</button>
    <form v-if="showForm" @submit.prevent="addTask">
      <input v-model="newTask.title" placeholder="Task title" required>
      <input v-model="newTask.description" placeholder="Task description" required>
      <select v-model="newTask.category" required>
        <option disabled value="">Please select a category</option>
        <option v-for="category in categories" :value="category.id" :key="category.id">
          {{ category.name }}
        </option>
      </select>
      <input type="checkbox" id="completed" v-model="newTask.completed">
      <label for="completed">Completed</label>
      <button type="submit">Submit task</button>
    </form>
    <form v-if="taskToEdit" @submit.prevent="saveTask">
      <input v-model="taskToEdit.title" placeholder="Task title" required>
      <input v-model="taskToEdit.description" placeholder="Task description" required>
      <select v-model="taskToEdit.category" required>
        <option disabled value="">Please select a category</option>
        <option v-for="category in categories" :value="category.id" :key="category.id">
          {{ category.name }}
        </option>
      </select>
      <input type="checkbox" id="completed" v-model="taskToEdit.completed">
      <label for="completed">Completed</label>
      <button type="submit">Save task</button>
    </form>
  </div>
    <div class ="task">
    <div v-for="task in Tasks" v-bind:key="task.id">
      <button v-if="$store.state.isAuthenticated" @click="editTask(task)">Edit</button>
        <button v-if="$store.state.isAuthenticated" @click="deleteTask(task)">Delete</button>
      <h1>T: {{ task.title }}</h1>
      <h2>D: {{ task.description }}</h2>
      <h3>C: {{ task.category_name }}</h3>
      <h3> {{task.completed}}</h3>
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