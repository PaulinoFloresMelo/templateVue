<script setup>
  import Facebook from 'vue-material-design-icons/Facebook.vue'
  import Instagram from 'vue-material-design-icons/Instagram.vue'
  import Google from 'vue-material-design-icons/Google.vue'
  import LinkedIn from 'vue-material-design-icons/LinkedIn.vue'
  import Github from 'vue-material-design-icons/Github.vue'
</script>

<template>
  <div class="p-5 bg-primary text-white text-center">
    <h1>Universo</h1>
    <p>Te decimos qué es el Universo, cómo surgió y qué tan grande es. Todo ello con el apoyo de especialistas y agencias espaciales.</p>
  </div>
  
  <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <div class="container-fluid">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/cosmos">Cosmos</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/about">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/prueba">Prueba</a>
        </li>
      </ul>
    </div>
  </nav>
  
  <nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-bottom">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Footer </a>
    </div>
  </nav>
  
  <main>
    <RouterView />
  </main>

<footer class="bg-primary text-center text-white fixed-bottom">
    <!-- Grid container -->
    <div class="container p-4 pb-0">
        <!-- Section: Social media -->
        <section class="mb-4">
            <a data-mdb-button-init data-mdb-ripple-init class="btn btn-outline-light btn-floating m-1" href="https://www.facebook.com/" role="button"><Facebook/></a>
            <a data-mdb-button-init data-mdb-ripple-init class="btn btn-outline-light btn-floating m-1" href="https://www.instagram.com/" role="button"><Instagram/></a>
            <a data-mdb-button-init data-mdb-ripple-init class="btn btn-outline-light btn-floating m-1" href="https://www.google.com/" role="button"><Google/></a>
            <a data-mdb-button-init data-mdb-ripple-init class="btn btn-outline-light btn-floating m-1" href="https://www.linkedin.com/" role="button"><LinkedIn/></a>
            <a data-mdb-button-init data-mdb-ripple-init class="btn btn-outline-light btn-floating m-1" href="https://github.com/" role="button"><Github/></a>
        </section>
        <!-- Section: Social media -->
    </div>
    <!-- Grid container -->

    <!-- Copyright -->
    <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
        © 2020 Copyright:
        <a class="text-white" href="https://mdbootstrap.com/">MDBootstrap.com</a>
    </div>
    <!-- Copyright -->
</footer>
<!-- Footer -->
</template>
