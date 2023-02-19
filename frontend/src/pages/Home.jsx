import React from "react";
import Card from "../components/Card";

// Maybe make it like the pinterest images, where it looks cooler.

const Foods = [
  {
    imageURL:
      "https://i.pinimg.com/750x/f4/d1/9c/f4d19cecd5d24e19376ac78d30131c97.jpg",
    id: 17,
  },
  {
    imageURL:
      "https://i.pinimg.com/564x/a2/d8/65/a2d8651e48ef054f370cbd874c7320c1.jpg",
    id: 42,
  },
  {
    imageURL:
      "https://i.pinimg.com/564x/47/70/8b/47708b6ccad6e93880a17a9ab3204fc7.jpg",
    id: 73,
  },
  {
    imageURL:
      "https://i.pinimg.com/564x/69/84/d0/6984d0f7c6c6298ac2d4037d69455103.jpg",
    id: 84,
  },

  {
    imageURL:
      "https://i.pinimg.com/564x/47/70/8b/47708b6ccad6e93880a17a9ab3204fc7.jpg",
    id: 73,
  },
  {
    imageURL:
      "https://i.pinimg.com/564x/a2/d8/65/a2d8651e48ef054f370cbd874c7320c1.jpg",
    id: 42,
  },

  {
    imageURL:
      "https://i.pinimg.com/564x/69/84/d0/6984d0f7c6c6298ac2d4037d69455103.jpg",
    id: 84,
  },
  {
    imageURL:
      "https://i.pinimg.com/750x/f4/d1/9c/f4d19cecd5d24e19376ac78d30131c97.jpg",
    id: 17,
  },
];

function Home() {
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
