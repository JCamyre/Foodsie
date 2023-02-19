import React from "react";
import { useParams, useLocation } from "react-router-dom";
import Card from "../components/Card";

function Food() {
  const { id } = useParams();
  // Once we have database, will prob not need to pass state, just access database from this page, using the ID as the thing we access
  const { state } = useLocation();
  var imageURL;
  var liked;
  if (state) {
    var { imageURL, liked } = state;
  }
  return (
    <div>
      {/* Obviously we will get food tags, title of dish, etc. from database */}
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
          }}
        >
          <div
            style={{
              display: "flex",
              alignItems: "center",
            }}
          >
            <div style={{ width: "50%" }}>
              <Card imageURL={imageURL} id={id} cardLiked={liked} />
            </div>
            <div style={{ width: "50%", justifyContent: "flex-end" }}>
              <h1>Food: {id}</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Food;
