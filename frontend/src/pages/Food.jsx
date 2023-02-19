import React from "react";
import { useParams, useLocation } from "react-router-dom";
import Card from "../components/Card";

function Food() {
  const { id } = useParams();
  // Once we have database, will prob not need to pass state, just access database from this page, using the ID as the thing we access
  const { state } = useLocation();
  var imageURL;
  if (state) {
    var { imageURL } = state;
  }
  return (
    <div>
      {/* Obviously we will get food tags, title of dish, etc. from database */}
      <h1>Card page for id: {id}</h1>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <div
          style={{
            borderRadius: "24px",
            width: "80%",
            height: "400px",
            backgroundColor: "#ffffff",
          }}
        >
          <Card imageURL={imageURL} id={id} />
        </div>
      </div>
    </div>
  );
}

export default Food;
