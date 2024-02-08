 <template>
<div>
  <div class="home">
    Tasks:
  </div>
    <div class ="task">
    <div v-for="task in Tasks" v-bind:key="task.id">
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
    }
  }
};
</script>