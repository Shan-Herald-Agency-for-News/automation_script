import axios from "axios";
import fs from "fs";

const startDate = new Date("2021, 12, 31");
const endDate = new Date("2022, 11, 1");

const token = ""
let posts_count = 0;

async function _fetchAPI(next) {
  await axios
    .get(next)
    .then((res) => {
      let data = res.data["data"];

      
      for (let i = 0; i < data.length; i++) {
        let bDate = new Date(data[i].created_time);

        if (bDate >= startDate && bDate <= endDate) {
          posts_count += 1;

//          fs.appendFile("posts.txt", `\n + ${data[i].permalink_url} : ${data[i].created_time}`, function (err,data) {
//            if (err) {
//              return console.log(err);
//            }
//          });

        }
      }

      let next_page = res.data["paging"].next;

      if (next_page) {
        _fetchAPI(next_page);
      } else {
        console.log("Posts Count: " + posts_count);
        console.log("Last Date: " + res.data["data"][res.data["data"].length - 1].created_time);
        console.log("Finished ...");
      }

    })
    .catch((error) => {
      console.log(error);
    });
}

function main() {
//  const live_videos = "title,broadcast_start_time,permalink_url";
//  const videos = "id,description,created_time";
//  const fields = videos;
//  const url = `https://graph.facebook.com/v15.0/shannews/published_posts?access_token=${token}&pretty=1&fields=${fields}&limit=250&before=QVFIUkZA3bXg1Q2djQk9GX0pXMTAyT09RSmFRRUJUeVBWc080TDRoVVltOW1YYjlRMzB3alFpRFdEMWpSZAUNrM0pHZAzJkeHR4WGdFbGtWZAHhnYUg5SHJ5SzVR`;

  //count posts
  const token = shan_token;
  const postField = "id,created_time, permalink_url";
  const postURL = `https://graph.facebook.com/v15.0/shannews/posts?access_token=${token}&fields=${postField}&since=2021-12-31&limit=100`;
  const videosURL = `https://graph.facebook.com/v15.0/shannews/videos?access_token=${token}&fields=${postField}&since=2021-12-31&limit=100`;

 // shannews/published_posts?fields=id,created_time&summary=total_count&since=2022-01-01

  _fetchAPI(postURL);
  _fetchAPI(videosURL);
}

main();
