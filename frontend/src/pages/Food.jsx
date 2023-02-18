import React from "react";
import { useParams } from "react-router-dom";
import Card from "../components/Card";

function Food() {
  const { id } = useParams();
  return (
    <div>
      <h1>Card page for id: {id}</h1>
      <Card />
    </div>
  );
}

export default Food;
