import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import styled from "styled-components";
import ReactLoading from "react-loading";

const IssueButton = styled.button`
  height: 100px;
  width: 200px;
  background-color: #967bb6;
  border-radius: 12px;
  color: #ffffff;
  transition: ease-out 0.1s;
  font-size: 18px;
  &:hover {
    cursor: pointer;
    transform: scale(0.95);
  }
`;

const Input = styled.input`
  height: 100px;
  width: 200px;
  background-color: #967bb6;
  border-radius: 12px;
  color: #ffffff;
  transition: ease-out 0.1s;
  &:hover {
    cursor: pointer;
    transform: scale(0.95);
  }
`;

function Recommendation() {
  const [recommendation, setRecommendation] = useState(null);
  const [notLikeFood, setNotLikeFood] = useState(false);
  const [notLikeFlavorProfile, setNotLikeFlavorProfile] = useState(false);
  const [badFoods, setBadFoods] = useState("");
  const [badFlavors, setBadFlavors] = useState("");

  const { uid } = useParams();

  useEffect(() => {
    axios
      .get("http://localhost:8080/genrecs", {
        params: {
          id: uid,
        },
      })
      .then((res) => {
        console.log("This is the new recommendation: ", res);
        const cum = res["data"].split("Answer: ");
        if (cum.length > 1) {
          setRecommendation(cum[1]);
        } else {
          setRecommendation(cum[0]);
        }
      });
  }, []);

  async function regen() {
    console.log("hello");
    setRecommendation(null);
    await axios
      .get("http://localhost:8080/regen", {
        params: {
          id: "test-user",
          dfl: badFoods,
          dfo: badFlavors,
        },
      })
      .then((res) => {
        console.log("New recommendation: ", res);
        setRecommendation(res["data"]);
      });
  }

  return (
    <div>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          padding: "60px",
          paddingBottom: "40px",
        }}
      >
        <div
          style={{
            borderRadius: "24px",
            width: "80%",
            backgroundColor: "#ffffff",
            padding: "24px",
            fontSize: "30px",
            display: "block",
            justifyContent: "center",
          }}
        >
          <h1 style={{ textAlign: "center" }}>Food Recommendations</h1>
          {recommendation ? (
            recommendation
          ) : (
            <ReactLoading type={"bubbles"} color={"black"} />
          )}
          <h1 style={{ textAlign: "center" }}>What was your issue?</h1>
          <div style={{ justifyContent: "center", display: "flex" }}>
            <IssueButton
              onClick={() => {
                setNotLikeFood(!notLikeFood);
                setNotLikeFlavorProfile(false);
              }}
            >
              Didn't like the foods?
            </IssueButton>
            <IssueButton
              onClick={() => {
                setNotLikeFlavorProfile(!notLikeFlavorProfile);
                setNotLikeFood(false);
              }}
            >
              Didn't like your flavor profile?
            </IssueButton>
            {notLikeFood && (
              <div style={{ display: "block" }}>
                <form
                  onSubmit={(e) => {
                    e.preventDefault();
                  }}
                >
                  <label style={{ alignItems: "center" }}>
                    Which foods didn't you like?
                    <textarea
                      id="badFoods"
                      name="badFoods"
                      type="text"
                      value={badFoods}
                      onChange={(event) => {
                        setBadFoods(event.target.value);
                      }}
                    />
                  </label>
                  <br />
                </form>
              </div>
            )}
            {notLikeFlavorProfile && (
              <form
                onSubmit={(e) => {
                  e.preventDefault();
                }}
              >
                <label>
                  Which flavors don't belong?
                  <textarea
                    id="badFlavors"
                    name="badFlavors"
                    type="text"
                    value={badFlavors}
                    onChange={(event) => {
                      setBadFlavors(event.target.value);
                    }}
                  />
                </label>
                <br />
              </form>
            )}
            <IssueButton onClick={() => regen()}>
              See new recommendations!
            </IssueButton>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Recommendation;
