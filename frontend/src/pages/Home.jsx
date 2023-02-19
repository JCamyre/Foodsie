import React, { useEffect } from "react";
import Card from "../components/Card";
import axios from "axios";

// Maybe make it like the pinterest images, where it looks cooler.

function convertIDtoImageURL(id) {
  const imageFormat = `https://s3-media0.fl.yelpcdn.com/bphoto/${id}/o.jpg`;
  return imageFormat;
}

const Foods = [
  {
    imageURL: convertIDtoImageURL("--8pNvGp9ICBjJVck2OnTQ"),
    id: "--8pNvGp9ICBjJVck2OnTQ",
    caption: "Food 1",
  },
  {
    imageURL: convertIDtoImageURL("--Kofko5jy33_vPJOEt4Ow"),
    id: "--Kofko5jy33_vPJOEt4Ow",
    caption: "Food 2",
  },
  {
    imageURL: convertIDtoImageURL("--S9xLJbQcfk74xKCkBAwA"),
    id: "--S9xLJbQcfk74xKCkBAwA",
    caption: "Food 3",
  },
  {
    imageURL: convertIDtoImageURL("--WqMu3zPYVePmsxABqhAA"),
    id: "--WqMu3zPYVePmsxABqhAA",
    caption: "Food 4",
  },

  {
    imageURL: convertIDtoImageURL("--j4xVIdIlYpOmZbs7iszg"),
    id: "--j4xVIdIlYpOmZbs7iszg",
    caption: "Food 5",
  },
  {
    imageURL: convertIDtoImageURL("--zScnI03KioBVMtcOK6oQ"),
    id: "--zScnI03KioBVMtcOK6oQ",
    caption: "Food 6",
  },

  {
    imageURL: convertIDtoImageURL("-0CCRlDxKDrooC9a3ZoF9A"),
    id: "-0CCRlDxKDrooC9a3ZoF9A",
    caption: "Food 7",
  },
  {
    imageURL: convertIDtoImageURL("-0VVXIyqTCQUGVQ56lvnrw"),
    id: "-0VVXIyqTCQUGVQ56lvnrw",
    caption: "Food 8",
  },
];

function Home() {
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
    const arr = ids.map((id) => {
      axios.get(`http://127.0.0.1:8080/list?id=${id}`).then((res) => {
        return res["data"];
      });
    });
    const users = await Promise.all(arr);
    console.log(users)
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
              caption={imageObject["caption"]}
            />
          );
        })}
      </div>
      <button>User clicks this when they are done liking images</button>
    </div>
  );
}

export default Home;
