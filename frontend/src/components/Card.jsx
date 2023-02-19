import React from "react";
import styled from "styled-components";
import { Link, useNavigate } from "react-router-dom";

// Maybe add hover stuff
const StyledCard = styled.div`
  width: 252px;
  height: 100%;
  background-color: transparent;
  padding: 10px;
  transition: ease-out 0.1s;
  &:hover {
    cursor: pointer;
    transform: scale(0.95);
  }
`;
const CardImage = styled.img`
  max-width: 100%;
  max-height: 100%;
  border-radius: 24px;
`;

function Card({ imageURL, id }) {
  const navigate = useNavigate();
  return (
    <StyledCard
      onClick={() => navigate(`/food/${id}`, { state: { imageURL: imageURL } })}
    >
      <CardImage src={imageURL} alt="Car" />
    </StyledCard>
  );
}

export default Card;
