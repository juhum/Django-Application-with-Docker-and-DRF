<template>
<div>
  <nav class="navbar">
    <ul>
    <li><router-link to="/" class="navbar-item">Home</router-link></li>
    <li><router-link to="/tasks" class="navbar-item">Task</router-link></li>
    <li><router-link to="/categories" class="navbar-item">Category</router-link></li>
    </ul>
  </nav>
  <section>
  <router-view style/>
  </section>

  <footer class="footer">
    <p>test</p>
    </footer>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #333;
  color: #fff;
  background-color: black;

  a {
  color: #fff;
  text-decoration: none;

    &.router-link-exact-active {
      color: #42b983;
    }
  }

  a:hover{
    background-color: #555;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline;
    margin-right: 10px;
  }
}

section{
  padding: 50px;
  margin-bottom: 50px;
  min-height: 100vh;
}

.footer {
  position: absolute;
  left: 0;
  right: 0;
  text-align: center;
  background-color: #333;
  color: #fff;
}

</style>
