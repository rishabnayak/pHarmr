<template>
<main role="main">
  <div class="container">
    <div class="row">
      <div class="col-sm">
        <div class="jumbotron text-center">
          <p class="text-muted">Air Temperature</p>
          {{temp}}
        </div>
      </div>
      <div class="col-sm">
        <div class="jumbotron text-center">
          <p class="text-muted">Humidity</p>
          {{humidity}}
        </div>
      </div>
      <div class="col-sm">
        <div class="jumbotron text-center">
          <p class="text-muted">Water Temperature</p>
          {{utemp}}
        </div>
      </div>
    </div>
    <br>
    <div style="text-align: center;">
      <button class="btn btn-primary" @click="toggleLights()">Toggle Lights</button>
    </div>
  </div>

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
import axios from 'axios'
export default {
  name: 'dashboard',
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  data() {
    return {
      temp: null,
      humidity: null,
      utemp: null
    }
  },
  methods: {
    toggleLights() {
      axios.post('https://io.adafruit.com/api/v2/rishab2113/feeds/light/data', {
        "value": "1"
      }, {
        headers: {
          'X-AIO-Key': 'fa8007a47db04ca29386bdcca2f0c203',
          'Content-Type': 'application/json'
        }
      })
    },
    getTemp() {
      axios.get(
          'https://io.adafruit.com/api/v2/rishab2113/feeds/temperature/data/last', {
            headers: {
              'X-AIO-Key': 'fa8007a47db04ca29386bdcca2f0c203',
              'Content-Type': 'application/json'
            }
          }
        )
        .then((response) => {
          this.temp = response.data.value;
          setTimeout(() => {
            this.getTemp()
          }, 10000)
        });
    },
    getuTemp() {
      axios.get(
          'https://io.adafruit.com/api/v2/rishab2113/feeds/utemp/data/last', {
            headers: {
              'X-AIO-Key': 'fa8007a47db04ca29386bdcca2f0c203',
              'Content-Type': 'application/json'
            }
          }
        )
        .then((response) => {
          this.utemp = response.data.value;
          setTimeout(() => {
            this.getuTemp()
          }, 10000)
        });
    },
    getHumidity() {
      axios.get(
          'https://io.adafruit.com/api/v2/rishab2113/feeds/humidity/data/last', {
            headers: {
              'X-AIO-Key': 'fa8007a47db04ca29386bdcca2f0c203',
              'Content-Type': 'application/json'
            }
          }
        )
        .then((response) => {
          this.humidity = response.data.value;
          setTimeout(() => {
            this.getHumidity()
          }, 10000)
        });
    },
  },
  mounted() {
    this.getTemp()
    this.getHumidity()
    this.getuTemp()
  }
}
</script>
