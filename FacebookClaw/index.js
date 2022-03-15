import axios from "axios";
import fs from "fs";

let data_count = 0;

let startDate = new Date("2020, 1, 1");
let endDate = new Date("2020, 12, 31");

async function _fetchAPI(next) {
  await axios
    .get(next)
    .then((res) => {
      let data = res.data["data"];

      for (let i = 0; i < data.length; i++) {
        let bDate = new Date(data[i].created_time);

        if (bDate >= startDate && bDate <= endDate) {
          data_count += 1;

          console.log(data_count);
        }
      }

      let next_page = res.data["paging"].next;

      if (next_page) {
        _fetchAPI(next_page);
      }
    })
    .catch((error) => {
      console.log(error);
    });
}

function main() {
  const live_videos = "title,broadcast_start_time,permalink_url";
  const videos = "id,description,created_time";
  const fields = videos;
  const token =
    "EAAS9vQUwCg0BACyaQF0qzBtkaUs3pnKCf5duaT0mtQZB2W6r9OytPvEHXMN76D5YVWqLxHQsYfE5lLZAIZCtIZAzSeDSvHbzKWl334LVH0P2qp8vfN7Wbk43C6PiWdlkUo7ZAY70prD3vXYw9SOvxZAEo3MjRBUxm5YLUPilredbbm4WvvPkCZA5qBMeMN8NebBrZCe6om4NkixytV6AyuyV";
  const url = `https://graph.facebook.com/v12.0/shannews/posts?access_token=${token}&pretty=1&fields=${fields}&limit=250&before=QVFIUkZA3bXg1Q2djQk9GX0pXMTAyT09RSmFRRUJUeVBWc080TDRoVVltOW1YYjlRMzB3alFpRFdEMWpSZAUNrM0pHZAzJkeHR4WGdFbGtWZAHhnYUg5SHJ5SzVR`;
  const postField = "id,message,created_time,permalink_url";
  const postURL = `https://graph.facebook.com/v12.0/382785502558433/posts?access_token=${token}&fields=${postField}`;

  _fetchAPI(postURL);
}

main();
