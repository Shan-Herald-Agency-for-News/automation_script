import axios from "axios";
import fs from "fs";

const startDate = new Date("2021, 12, 31");
const endDate = new Date("2022, 11, 1");

//const shan_token = "EAAR6r9y6ZAckBADZBAhQsJblFZAxOOAebnVZCRzTZCHIwEorDPM1e7E8dzexB8FhoiS9z1ZBbJedZCKHhPP2sd6A7csq6c6nZCySOaXB1z7ZCmCHnTtcwuDsKdg2cL6tBfxFFgMHzjZAyzlAPODG279mutyV5xpx3a8q3NlM8PQF3p9fXPELQs3s07ZCEzBQfSnD8p0ZAPCRg953xCsdU5pGnQhZB"
//const bur_token = "EAAR6r9y6ZAckBACj9mH0RobBSRR6d7jbUuR9XIhzgk69ZCdvBAZA3ruo4p3PdIMFZCVo0ML12hjbxGtokfYYGZCYlHEmWN28I0uegukq241nI6AsjGxAKvbWn12X2UmZCyUerQZA9lsw4SZCZAsJDPtujluA8sj5CtdJ3laxWcJlg0hFCpcrTfGsRlNZA2yVIFHZBZB96ixgq34LQKXYKAinX279"
//const eng_token = "EAAR6r9y6ZAckBAJOzuTYcB7nuDPduwCAlBGeLYshnFB7pEnt6bD0SmtvD7nTJkAN6X3GHj9gVZAElHyZBQaLEsdz6XgwpkJLTUYG5dAgIeNCmoIC9ow1Q1KZBdcfZA09DLUZBLukC20bioAjn4SO4AYksZB6kYSLk5PZA7r4aMjw9jgRgc9CviUK5KNooqa9NS2Et4KtmLdA5iMZC8NmTDWMS"
//const tv_token = "EAAR6r9y6ZAckBAEuNldQqIG1ra2JsFpHSQG7HtiB4ZBBrpzyyWwYn5QZCeT8jECPZBlER1unyajVms3WGbtlMlKyWBZBZASu8qhND73147fEU5wNNKWRKDRgylotztpkNM84L998xKAPbXWlsfxPMYB80NvQF5oNXCTowpu1XSOaOkbZCLH9CnPkXxhQgZA8mj0ntigKUBFZAIx9MG6IcRB79"
//const radio_token = "EAAR6r9y6ZAckBAMcz8THcx7GWveZBojpkswd6FasprqZC0xZA0XlMtBmq5rZAKRMOMYANmCxXt76y545qPU5VhXRwoi7l7B9Bntaj1wGSKFJoqkiNcBir5c0JvYYkgGXA7cDVZAGQawHGZAiaDhCbpGelEi1qvEEa2RVARxGIkQuMPElXIXtO0DkbW808bELAHGCgYefe2KGyrZA1ZBaM5lQM"

const shan_token = ""
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
