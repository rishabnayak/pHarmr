<template>
<main role="main">
    <section class="jumbotron text-center">
        <div class="container">
            <img class="img-fluid width: 100%; height: auto;" src="@/assets/pHarmr_logo.png" />
            <p class="lead text-muted">Automate your Hydroponics with pHarmr</p>
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
    doSomething() {
      var request = require('request');

      var options = {
        url: 'https://io.adafruit.com/api/v2/rishab2113/feeds/temperature/data',
        headers: {
          'X-AIO-Key': 'fa8007a47db04ca29386bdcca2f0c203',
          'Content-Type': 'application/json'
        }
      };

      function callback(error, response, body) {
        if (!error && response.statusCode == 200) {
          var feed = JSON.parse(body);
          console.log(feed);
        }
      }

      request(options, callback);
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
  async created() {}
}
</script>
