import "./App.css";
import React from "react";
import MoviesList from "./MoviesList";

const movielist = [
  {
    title: "The Great Train Robbery",
    description:
      "A group of bandits stage a brazen train hold-up, only to find a determined posse hot on their heels.",
    year: 1903,
    picture:
      "https://m.media-amazon.com/images/M/MV5BMTU3NjE5NzYtYTYyNS00MDVmLWIwYjgtMmYwYWIxZDYyNzU2XkEyXkFqcGdeQXVyNzQzNzQxNzI@._V1_SY1000_SX677_AL_.jpg",
  },
  {
    title: "A Corner in Wheat",
    description:
      "A greedy tycoon decides, on a whim, to corner the world market in wheat. This doubles the price of bread, forcing the grain's producers into charity lines and further into poverty.",
    year: 1909,
    picture:
      "https://m.media-amazon.com/images/M/MV5BYWFiMTIyMjEtY2M4ZC00NDlkLWFiMWUtMDdhNTVhMjM0YjU3XkEyXkFqcGdeQXVyMTMxMTY0OTQ@._V1_SY1000_SX677_AL_.jpg",
  },
  {
    title: "Gertie the Dinosaur",
    description:
      "The cartoonist, Winsor McCay, brings the Dinosaurus back to life in the figure of his latest creation, Gertie the Dinosaur.",
    year: 1914,
    picture:
      "https://m.media-amazon.com/images/M/MV5BMTAxNzM1MDI1OTheQTJeQWpwZ15BbWU4MDk1NjQ1ODAx._V1_SY1000_SX677_AL_.jpg",
  },
  {
    title: "In the Land of the Head Hunters",
    description:
      "Original advertising for the film describes it as a drama of primitive life on the shores of the North Pacific.",
    year: 1914,
    picture:
      "https://m.media-amazon.com/images/M/MV5BM2Q2NDNlOTEtYjBjMS00NGI3LWFkNjktNjE1YjBlMDExMzg5XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_SX677_AL_.jpg",
  },
  {
    title: "The Blue Bird",
    description:
      "Two peasant children, Mytyl and Tyltyl, are led by Berylune, a fairy, to search for the Blue Bird of Happiness.",
    year: 1918,
    picture:
      "https://m.media-amazon.com/images/M/MV5BMjNlMThmNzItMTZlMS00YzJkLTk1MzktYzIyMzllOGFmZmRlXkEyXkFqcGdeQXVyMzE0MjY5ODA@._V1_SY1000_SX677_AL_.jpg",
  },
  {
    title: "The Four Horsemen of the Apocalypse",
    description:
      "An extended family split up in France and Germany find themselves on opposing sides of the battlefield during World War I.",
    year: 1921,
    picture:
      "https://m.media-amazon.com/images/M/MV5BOTU1ODQyYTctODhkNy00YWRmLWE2YzYtMTQ5ZjA3OTNiN2QyXkEyXkFqcGdeQXVyMzE0MjY5ODA@._V1_SY1000_SX677_AL_.jpg",
  },
  {
    title: "The Big House",
    description:
      "A convict falls in love with his new cellmate's sister, only to become embroiled in a planned break-out which is certain to have lethal consequences.",
    year: 1930,
    picture:
      "https://m.media-amazon.com/images/M/MV5BNjBjMmU2NjQtOGJlYS00OTE4LWE4ZjYtNzlmMzJhYmE5MjA5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjUxODE0MDY@._V1_SY1000_SX677_AL_.jpg",
  },
  {
    title: "Crime Busters",
    description:
      "An attempted robbery turns to be an unexpected recruitment when two unemployed men mistakenly break into a police office instead of a store.",
    year: 1977,
    picture:
      "https://m.media-amazon.com/images/M/MV5BN2Q5MThlZTgtMWMyMi00NDIwLWE1NTMtNzFlOGRmM2QxMGY0XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_SY1000_SX677_AL_.jpg",
  },
  {
    title: "State and Main",
    description:
      "Having left New Hampshire over excessive demands by the locals, the cast and crew of \"The Old Mill\" moves their movie shoot to a small town in Vermont. However, they soon discover that The Old Mill burned down in 1960, the star can't keep his pants zipped, the starlet won't take her top off, and the locals aren't quite as easily conned as they appear.",
    year: 2000,
    picture:
      "https://m.media-amazon.com/images/M/MV5BZTVmZGRlMTgtN2I1Yi00YjE2LWFjMjctNDhiMWM4NTNmOGU2XkEyXkFqcGdeQXVyMTA0MjU0Ng@@._V1_SY1000_SX677_AL_.jpg",
  },
  {
    title: "Jurassic World",
    description:
      "A new theme park is built on the original site of Jurassic Park. Everything is going well until the park's newest attraction--a genetically modified giant stealth killing machine--escapes containment and goes on a killing spree.",
    year: 2015,
    picture:
      "https://m.media-amazon.com/images/M/MV5BNzQ3OTY4NjAtNzM5OS00N2ZhLWJlOWUtYzYwZjNmOWRiMzcyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX677_AL_.jpg",
  },
];

function App() {
  return (
    <div id="hello world" style={{ backgroundColor: "#BABABA" }}>
      <div style={{ height: 40 }}></div>
      <h1 style={{ marginTop: 0, textAlign: "center" }}>Movie List</h1>
      <MoviesList movies={movielist} daddy="taowenwei" />
    </div>
  );
}

export default App;

//    {f string  {  css instead of jsx}}
