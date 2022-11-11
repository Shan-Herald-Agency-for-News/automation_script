import axios from "axios";
import fs from "fs";

const since = "2022-01-01";
const until = "2022-12-31";
const startDate = new Date(since);
const endDate = new Date(until);

const api_token = "";
let posts_count = 0;

async function _fetchAPI(next) {

  var twirlTimer = (function() {
    var P = ["\\", "|", "/", "-"];
    var x = 0;
    return setInterval(function() {
      process.stdout.write("\r" + P[x++]);
      x &= 3;
    }, 250);
  })();

  await axios
    .get(next)
    .then((res) => {
      let data = res.data["data"];

      
      for (let i = 0; i < data.length; i++) {
        let bDate = new Date(data[i]?.created_time);

        if (bDate >= startDate && bDate <= endDate) {
          posts_count += 1;

//          fs.appendFile("posts.txt", `\n + ${data[i].permalink_url} : ${data[i].created_time}`, function (err,data) {
//            if (err) {
//              return console.log(err);
//            }
//          });

        }
      }

      let next_page = res.data["paging"]?.next || null;

      if (next_page) {

        _fetchAPI(next_page);

        clearInterval(twirlTimer);
      } else {
        console.log("Posts Count: " + posts_count);
        console.log("Last Date: " + res.data["data"][res.data["data"].length - 1]?.created_time);
        console.log("Finished ...");
        clearInterval(twirlTimer);
      }

    })
    .catch((error) => {
      console.log(error);
      process.exit()
    });
}

function main() {

  //count posts
  const token = api_token;
  const postField = "id,created_time";
  const page = "shannewsenglish"

  console.log(`Fetch page: ${page}`);
  console.log(`DateTime Fetch: ${since} - ${until}\n`);

  // facebook endpoints
  const postURL = `https://graph.facebook.com/v15.0/${page}/published_posts?access_token=${token}&fields=${postField}&since=${since}&until=${until}&limit=100`;
  const videosURL = `https://graph.facebook.com/v15.0/${page}/videos?access_token=${token}&fields=${postField}&since=${since}&until=${until}&limit=100`;
  const liveVideosURL = `https://graph.facebook.com/v15.0/${page}/live_videos?access_token=${token}&fields=${postField}&since=${since}&until=${until}&limit=100`;

 // shannews/published_posts?fields=id,created_time&summary=total_count&since=2022-01-01

  _fetchAPI(postURL);
  _fetchAPI(videosURL);
  _fetchAPI(liveVideosURL);
}

main();
