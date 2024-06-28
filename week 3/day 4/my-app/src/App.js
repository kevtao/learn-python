import "./App.css";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import BasicSelect from "./UniqueYears";
import MoviesList from "./MoviesList";
import About from "./About";

function App() {
  return (
    <Router>
      <div id="hello world" style={{ backgroundColor: "#BABABA" }}>
        <div style={{ height: 40 }}></div>
        <Routes>
          <Route path="/" element={<HomeWithButton />} />
          <Route path="/detail/:_id" element={<About />} />
        </Routes>
      </div>
    </Router>
  );
}

const HomeWithButton = () => {
  return (
    <div>
      <h1 style={{ textAlign: "center" }}>Movie List</h1>
      <BasicSelect />
      <MoviesList />
      <div style={{ textAlign: "center", marginTop: "20px" }}></div>
    </div>
  );
};

export default App;
