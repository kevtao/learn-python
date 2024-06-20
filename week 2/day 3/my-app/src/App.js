import "./App.css";
import React from "react";
import MoviesList from "./MoviesList";

const movielist = [
  {
    title: "The Great Train Robbery",
    description:
      "Among the earliest existing films in American cinema - notable as the …",
    year: 1903,
  },
  {
    title: "A Corner in Wheat",
    description:
      "A greedy tycoon decides, on a whim, to corner the world market in whea…",
    year: 1909,
  },
  {
    title: "Gertie the Dinosaur",
    description:
      "Winsor Z. McCay bets another cartoonist that he can animate a dinosaur…",
    year: 1914,
  },
  {
    title: "In the Land of the Head Hunters",
    description:
      "Original advertising for the film describes it as a drama of primitive…",
    year: 1914,
  },
  {
    title: "The Blue Bird",
    description:
      "Two peasant children, Mytyl and Tyltyl, are led by Berylune, a fairy, …",
    year: 1918,
  },
  {
    title: "The Four Horsemen of the Apocalypse",
    description:
      "An extended family split up in France and Germany find themselves on o…",
    year: 1921,
  },
  {
    title: "The Big House",
    description:
      "A convict falls in love with his new cellmate's sister, only to become…",
    year: 1930,
  },
  {
    title: "Crime Busters",
    description:
      "An attempted robbery turns to be an unexpected recruitment when two un…",
    year: 1977,
  },
  {
    title: "State and Main",
    description:
      "Having left New Hampshire over excessive demands by the locals, the ca…",
    year: 2000,
  },
  {
    title: "Jurassic World",
    description:
      "A new theme park is built on the original site of Jurassic Park. Every…",
    year: 2015,
  },
];

function App() {
  return (
    <div className="App">
      <h1>Movie List</h1>
      <MoviesList movies={movielist} daddy='taowenwei'/>
    </div>
  );
}

export default App;


