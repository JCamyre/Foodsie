import React from "react";
import { useParams, useLocation } from "react-router-dom";
import Card from "../components/Card";

function Food() {
  const { id } = useParams();
  // Once we have database, will prob not need to pass state, just access database from this page, using the ID as the thing we access
  const { state } = useLocation();
  const { imageURL } = state;
  return (
    <div>
      <h1>Card page for id: {id}</h1>
      <Card imageURL={imageURL} id={id} />
    </div>
  );
}

export default Food;
