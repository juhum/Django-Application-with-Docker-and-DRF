<template>
<div>
  <div class="home">
    Dashboard
  </div>
    <div class ="task">
    <h1>Hey checkout the latest task !</h1>
      <div v-if="latestTask">
        <h1>{{ latestTask.title }}</h1>
        <h2>{{ latestTask.description }}</h2>
        <h3>{{ latestTask.category_name }}</h3>
      </div>
    </div>
</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
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
  },
  methods: {
    getLatestTask() {
      axios
        .get('/api/v1/tasks/')
        .then(response => {
          if (response.data.length > 0) {
            this.latestTask = response.data[0];
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
