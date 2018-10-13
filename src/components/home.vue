<template>
<main role="main">
  <section class="jumbotron text-center">
    <div class="container">
      <h1 class="jumbotron-heading">pHarmr</h1>
      <p class="lead text-muted">Automate your Hydroponics with pHarmr</p>
      <button class="btn btn-primary btn-lg btn-block col-md-3" @click="doSomething()">Click</button>
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
<script>
import firebase from 'firebase'
import firebaseui from 'firebaseui'
import db from '@/firebase/init.js'
export default {
  name: 'home',
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    doSomething(){
      var xhr = new XMLHttpRequest()
      xhr.open("GET", "https://pubsub.googleapis.com/v1/projects/pharmr-2018/topics/dht11",true)
      console.log(xhr.send())
    }
  },
  async mounted() {
    if (this.user) {
      if (this.user.uname == undefined) {
        this.$router.push({
          name: "editprofile"
        })
      } else {
        return
      }
    } else {
      return
    }
  },
  async created() {
  }
}
</script>
