 <template>
<div>
  <div class="home">
    Categories:
  </div>
    <div class="category">
      <div v-for="category in Categories" v-bind:key="category.id">
        <h1>T: {{ category.name }}</h1>
      </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CategoryView',
  data() {
    return {
      Categories: []
    }
  },
  components: {

  },
  mounted() {
    this.getCategories();
  },
  methods: {
    getCategories() {
      axios
        .get('/api/v1/category/')
        .then(response => {
          this.Categories = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>