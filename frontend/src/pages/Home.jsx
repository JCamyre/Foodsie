import React, { useEffect, useState } from "react";
import Card from "../components/Card";
import axios from "axios";
import ReactLoading from "react-loading";
import * as qs from "qs";

// Maybe make it like the pinterest images, where it looks cooler.

function convertIDtoImageURL(id) {
  const imageFormat = `https://s3-media0.fl.yelpcdn.com/bphoto/${id}/o.jpg`;
  return imageFormat;
}

function Home() {
  const [foods, setFoods] = useState(false);
  const [likedFoods, setLikeFoods] = useState([]);

  useEffect(() => {
    async function getFood() {
      const ids = await axios
        .get("http://localhost:8080/init")
        .then((photoIds) => {
          return photoIds;
        });

      // an array of Promises waiting to be resolved
      // if we did axios.get().then(), then we are expecting it to be resolved alr, since we are returning
      let promises = ids["data"].map((id) => {
        return axios.get(`http://127.0.0.1:8080/food-list?id=${id}`);
      });
      return await Promise.all(promises).then((data) => {
        return data;
      });
    }

    getFood().then(async (res) => {
      const foods = res.map((food) => {
        return food["data"];
      });
      setFoods(foods);
    });
  }, []);

  function updateUserLikes() {
    axios.get("http://localhost:8080/finished", {
      params: {
        foods: JSON.stringify(likedFoods),
        id: "test-user",
      },
    });
  }

  return (
    <div style={{ padding: "50px", paddingTop: "25px" }}>
      <div
        style={{
          display: "flex",
          width: "100%",
          justifyContent: "center",
          flexWrap: "wrap",
        }}
      >
        {foods &&
          foods.map((imageObject, key) => {
            return (
              <Card
                key={key}
                imageURL={convertIDtoImageURL(imageObject["photo_id"])}
                id={imageObject["photo_id"]}
                caption={imageObject["caption"]}
                currentLikedFoods={likedFoods}
                likeSetter={setLikeFoods}
              />
            );
          })}
        {!foods && <ReactLoading type={"bubbles"} color={"black"} />}
      </div>
      <button
        onClick={() => {
          updateUserLikes();
        }}
      >
        User clicks this when they are done liking images
      </button>
    </div>
  );
}

export default Home;
