import React from "react";
import styled from "styled-components";

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

function Card() {
  return (
    <StyledCard onClick={() => console.log("yo")}>
      <CardImage
        src="https://i.pinimg.com/750x/f4/d1/9c/f4d19cecd5d24e19376ac78d30131c97.jpg"
        alt="Car"
      />
    </StyledCard>
  );
}

export default Card;
