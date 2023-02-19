import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";

const LogoButton = styled.img`
  transition: ease-out 0.1s;
  &:hover {
    transform: scale(0.95);
    cursor: point;
  }
`;

function Navbar() {
  return (
    <div style={{ display: "flex", height: "75px" }}>
      <Link to="/">
        <LogoButton
          src="https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_4:3/k%2FPhoto%2FRecipe%20Ramp%20Up%2F2022-07-Bison-Burger%2Fbison-burger-2"
          alt="Bison Burger"
          style={{ maxHeight: "100%", borderRadius: "24px" }}
        />
      </Link>
    </div>
  );
}

export default Navbar;
