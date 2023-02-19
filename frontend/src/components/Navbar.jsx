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
    <div
      style={{
        display: "flex",
        justifyContent: "flex-start",
        height: "75px",
        padding: "20px",
        backgroundColor: "#967BB6",
      }}
    >
      <Link to="/">
        <LogoButton
          src="/logo.png"
          alt="Logo"
          style={{ maxHeight: "100%", borderRadius: "24px" }}
        />
      </Link>
    </div>
  );
}

export default Navbar;
