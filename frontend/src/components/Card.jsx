import React from "react";
import styled from "styled-components";

const StyledCard = styled.div`
  width: 252px;
  height: 435px;
  background-color: transparent;
`;
const CardImage = styled.img`
  max-width: 100%;
  max-height: 100%;
  border-radius: 24px;
`;

function Card() {
  return (
    <StyledCard>
      <CardImage
        src="https://i.pinimg.com/750x/f4/d1/9c/f4d19cecd5d24e19376ac78d30131c97.jpg"
        alt="Car"
      />
    </StyledCard>
  );
}

export default Card;
