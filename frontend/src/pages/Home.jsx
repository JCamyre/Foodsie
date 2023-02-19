import React, { useEffect } from "react";
import Card from "../components/Card";
import axios from "axios";
import { convertRoutesToDataRoutes } from "../../node_modules/@remix-run/router/utils";

// Maybe make it like the pinterest images, where it looks cooler.

function convertIDtoImageURL(id) {
  const imageFormat = `https://s3-media0.fl.yelpcdn.com/bphoto/${id}/o.jpg`;
  return imageFormat;
}

const Foods = [
  {
    imageURL: convertIDtoImageURL("--8pNvGp9ICBjJVck2OnTQ"),
    id: "--8pNvGp9ICBjJVck2OnTQ",
  },
  {
    imageURL: convertIDtoImageURL("--Kofko5jy33_vPJOEt4Ow"),
    id: "--Kofko5jy33_vPJOEt4Ow",
  },
  {
    imageURL: convertIDtoImageURL("--S9xLJbQcfk74xKCkBAwA"),
    id: "--S9xLJbQcfk74xKCkBAwA",
  },
  {
    imageURL: convertIDtoImageURL("--WqMu3zPYVePmsxABqhAA"),
    id: '--WqMu3zPYVePmsxABqhAA"',
  },

  {
    imageURL: convertIDtoImageURL("--j4xVIdIlYpOmZbs7iszg"),
    id: "--j4xVIdIlYpOmZbs7iszg",
  },
  {
    imageURL: convertIDtoImageURL("--zScnI03KioBVMtcOK6oQ"),
    id: "--zScnI03KioBVMtcOK6oQ",
  },

  {
    imageURL: convertIDtoImageURL("-0CCRlDxKDrooC9a3ZoF9A"),
    id: "-0CCRlDxKDrooC9a3ZoF9A",
  },
  {
    imageURL: convertIDtoImageURL("-0VVXIyqTCQUGVQ56lvnrw"),
    id: "-0VVXIyqTCQUGVQ56lvnrw",
  },
];

function Home() {
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8080/list?id=AVXPpWI14yRq6kHL3oecWg")
      .then((res) => {
        console.log(res["data"]);
      });
  }, []);
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
        {Foods.map((imageObject, key) => {
          return (
            <Card
              key={key}
              imageURL={imageObject["imageURL"]}
              id={imageObject["id"]}
            />
          );
        })}
      </div>
      <button>User clicks this when they are done liking images</button>
    </div>
  );
}

export default Home;
