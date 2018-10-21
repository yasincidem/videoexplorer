var admin = require("firebase-admin");
var axios = require("axios");
var serviceAccount = require("./serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://videos-df4a4.firebaseio.com"
});

axios.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UULXo7UDZvByw2ixzpQCufnA&key=AIzaSyAZGJ9zSpQuNzen5QYfuOS4mxOyrwT9hAM')
  .then( res => res.data)
  .then( res => {
    var ref = db.ref('name');
    console.log(res.items);
    ref.set(res['items'])
  })
  .catch((error) => {
    console.log(error);
  });

var db = admin.database();

// // ref.once('value', (snap) => {
// //   console.log(snap.val());
// // });
// list = ['adasda']
