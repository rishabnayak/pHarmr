<template>
  <main role="main">
    <section class="jumbotron text-center">
        <div class="container">
          <h1 class="jumbotron-heading">pHarmr</h1>
          <p class="lead text-muted">Automate your Hydroponics with pHarmr</p>
        </div>
      </section>


            <hr class="featurette-divider">

          <footer class="container">
            <p class="float-right"><a href="#">Back to top</a></p>
            <p>© 2018 pHarmr · <a><router-link :to="{ name: 'privacy'}">Privacy</router-link></a></p>
          </footer>
    </main>
</template>
<script>
import firebase from 'firebase'
import firebaseui from 'firebaseui'
import db from '@/firebase/init.js'
export default {
  name: 'home',
  computed: {
    user () {
      return this.$store.state.user
    }
  },
async mounted (){
  if (this.user) {
    if (this.user.uname == undefined) {
      this.$router.push({ name: "editprofile"})
    }
    else {
      return
    }
  }
  else {
    return
    }
  }
}
</script>
