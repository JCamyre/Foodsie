import React, { useEffect, useState } from "react";
import Card from "../components/Card";
import axios from "axios";
import ReactLoading from "react-loading";
import styled from "styled-components";
import { Link } from "react-router-dom";

// Maybe make it like the pinterest images, where it looks cooler.

function convertIDtoImageURL(id) {
  const imageFormat = `https://s3-media0.fl.yelpcdn.com/bphoto/${id}/o.jpg`;
  return imageFormat;
}

const GenerateRecs = styled.input`
  height: 100px;
  width: 200px;
  background-color: #967bb6;
  border-radius: 12px;
  color: #ffffff;
  transition: ease-out 0.1s;
  &:hover {
    cursor: pointer;
    transform: scale(0.95);
  }
`;

function Home() {
  const [foods, setFoods] = useState(false);
  const [likedFoods, setLikeFoods] = useState([]);
  const [cuisines, setCuisines] = useState("");

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

  async function updateUserLikes() {
    console.log(JSON.stringify(likedFoods));
    console.log(JSON.stringify(cuisines));
    await axios.get("http://localhost:8080/finished", {
      params: {
        foods: JSON.stringify(likedFoods),
        id: "test-user",
        c: JSON.stringify(cuisines),
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
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          paddingTop: "40px",
          paddingBottom: "40px",
        }}
      >
        <div
          style={{
            borderRadius: "24px",
            width: "80%",
            backgroundColor: "#ffffff",
            padding: "24px",
            fontSize: "30px",
            display: "block",
          }}
        >
          <form
            onSubmit={(e) => {
              e.preventDefault();
              updateUserLikes();
            }}
          >
            <label>
              Which cuisines do you want to try?
              <textarea
                id="cuisines"
                name="cuisines"
                type="text"
                value={cuisines}
                onChange={(event) => {
                  setCuisines(event.target.value);
                }}
              />
            </label>
            <br />
            <Link to="/recommendation/test-user">
              <GenerateRecs type="submit" value="Generate Recommendations!" />
            </Link>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Home;
