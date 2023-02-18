import React from "react";
import styled from "styled-components";
import { Link } from "react-router-dom";

// Maybe add hover stuff
const StyledCard = styled.div`
  width: 252px;
  height: 435px;
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
  return (
    <StyledCard>
      <Link to={`/food/${id}`}>
        <CardImage src={imageURL} alt="Car" />
      </Link>
    </StyledCard>
  );
}

export default Card;
