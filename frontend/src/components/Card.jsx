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

function Card({
  imageURL,
  id,
  cardLiked = false,
  caption,
  foodPage = false,
  currentLikedFoods = [],
  likeSetter,
}) {
  const navigate = useNavigate();
  const [liked, setLiked] = useState(cardLiked);

  return (
    <StyledCard>
      <CardImage
        // onClick={() => {
        //   if (!foodPage) {
        //     navigate(`/food/${id}`, {
        //       state: { imageURL: imageURL, liked: liked, caption: caption },
        //     });
        //   }
        // }}
        src={imageURL}
        alt={caption}
      />
      <Heart
        onClick={() => {
          if (liked) {
            // If we already liked this post, and we click heart again, we want to unlike
            // So remove this food from likedFoods.
            const index = currentLikedFoods.indexOf(id);
            console.log(currentLikedFoods[index], index);
            currentLikedFoods.splice(index, 1);
            likeSetter(currentLikedFoods);
          } else {
            likeSetter(currentLikedFoods.concat([id]));
          }
          setLiked(!liked);
        }}
        isActive={liked}
        style={{ height: "50px" }}
      />
    </StyledCard>
  );
}

export default Card;
