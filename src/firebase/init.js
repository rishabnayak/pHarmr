import firebase from 'firebase'
import firestore from 'firebase/firestore'

  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyAA1m7SCChVP9z8FZfjlxebaBvN-WIq_ao",
    authDomain: "pharmr-2018.firebaseapp.com",
    databaseURL: "https://pharmr-2018.firebaseio.com",
    projectId: "pharmr-2018",
    storageBucket: "pharmr-2018.appspot.com",
    messagingSenderId: "272732475580"
  };
  const auth = firebase.initializeApp(config);
  auth.firestore().settings({timestampsInSnapshots: true});
  export default auth.firestore();
