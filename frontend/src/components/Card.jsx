import React, { useState } from "react";
import styled from "styled-components";
import { Link, useNavigate } from "react-router-dom";
import Heart from "react-heart";

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

// Whenever the card gets liked, make a post request to data

function Card({ imageURL, id, cardLiked }) {
  const navigate = useNavigate();
  const [liked, setLiked] = useState(false);

  return (
    <StyledCard>
      <Heart
        onClick={() => {
          setLiked(!liked);
        }}
        isActive={liked}
      />
      <CardImage
        onClick={() =>
          navigate(`/food/${id}`, { state: { imageURL: imageURL } })
        }
        src={imageURL}
        alt="Car"
      />
    </StyledCard>
  );
}

export default Card;
