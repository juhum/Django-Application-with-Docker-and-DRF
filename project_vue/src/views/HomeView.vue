<template>
<div>
  <div class="home">
    <h1>Hey checkout the latest task !</h1>
  </div>
    <div class ="task">
      <div v-if="latestTask">
        <h1>{{ latestTask.title }}</h1>
        <h2>{{ latestTask.description }}</h2>
        <h3>{{ latestTask.category_name }}</h3>
      </div>
      <div v-else>
        <p>No tasks available.</p>
      </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      latestTask: null
    }
  },
  mounted() {
    this.getLatestTask();
    document.title = "Home"
  },
  methods: {
    getLatestTask() {
      axios
        .get('/api/v1/tasks/')
        .then(response => {
          if (response.data.length > 0) {
            this.latestTask = response.data.slice(-1)[0];
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped>
.home-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.home {
  font: 100rem;
  padding: 10px;
  margin-bottom: 20px;
}

.task {
  border: 1px solid #ccc;
  padding: 20px;
}

.latest-task {
  border: 1px solid #aaa;
  padding: 10px;
  background-color: #f9f9f9;
}

.latest-task h1 {
  margin: 0 0 10px;
}

.latest-task h2 {
  margin: 0;
}

.latest-task p {
  margin: 5px 0;
}
</style>