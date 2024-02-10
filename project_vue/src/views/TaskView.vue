 <template>
<div>
  <div class="home">
    Tasks:
    <button @click="addTask(task)">Add task</button>
  </div>
    <div class ="task">
    <div v-for="task in Tasks" v-bind:key="task.id">
        <button @click="editTask(task)">Edit</button>
        <button @click="deleteTask(task)">Delete</button>
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
      Tasks: []
    }
  },
  components: {

  },
  mounted() {
    this.getTasks();
    document.title = "Tasks"
    console.log(this.$store.state.token)
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
    addTask(task){
        const newTask = {
    title: "ttnoauth",
    description: "dddddd222dddd",
    completed: false,
    category: 1
    // Other fields as needed
  };

axios.post('/api/v1/tasks/', newTask, {
  headers: {
    'Authorization': `token ${localStorage.token}`, // Replace `yourToken` with the actual token value
  }
})
.then(response => {
  // Update tasks list after successful creation
  this.Tasks.push(response.data);
  console.log(localStorage.token)
})
.catch(error => {
  console.error('Error creating task:', error);
});

    },
    editTask(task){

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