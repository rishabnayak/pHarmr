<template>
<main role="main">
    <section class="jumbotron text-center">
          <div class="container">
                <p class="lead text-muted">Temp</p>
      <button class="btn btn-primary" @click="doSomething()">Refresh</button>
            </div>
      </section>

    
  <hr class="featurette-divider">

    <footer class="container">
        <p class="float-right"><a href="#">Back to top</a></p>
        <p>© 2018 pHarmr · <a>
                <router-link :to="{ name: 'privacy'}">Privacy</router-link>
              </a></p>
      </footer>
</main>
</template>
