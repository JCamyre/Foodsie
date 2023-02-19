import React, { useEffect, useState } from "react";
import Card from "../components/Card";
import axios from "axios";
import ReactLoading from "react-loading";

// Maybe make it like the pinterest images, where it looks cooler.

function convertIDtoImageURL(id) {
  const imageFormat = `https://s3-media0.fl.yelpcdn.com/bphoto/${id}/o.jpg`;
  return imageFormat;
}

function Home() {
  const [foods, setFoods] = useState(false);
  const [likedFoods, setLikeFoods] = useState([]);
  const ids = [
    "--8pNvGp9ICBjJVck2OnTQ",
    "--Kofko5jy33_vPJOEt4Ow",
    "--S9xLJbQcfk74xKCkBAwA",
    "--WqMu3zPYVePmsxABqhAA",
    "--j4xVIdIlYpOmZbs7iszg",
    "--zScnI03KioBVMtcOK6oQ",
    "-0CCRlDxKDrooC9a3ZoF9A",
    "-0VVXIyqTCQUGVQ56lvnrw",
  ];
  useEffect(() => {
    async function getFood() {
      // an array of Promises waiting to be resolved
      // if we did axios.get().then(), then we are expecting it to be resolved alr, since we are returning
      let promises = ids.map((id) => {
        return axios.get(`http://127.0.0.1:8080/list?id=${id}`);
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

  console.log(likedFoods);
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
      <button>User clicks this when they are done liking images</button>
    </div>
  );
}

export default Home;
