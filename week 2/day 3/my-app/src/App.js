import "./App.css";
import MoviesList from "./MoviesList";
import BasicSelect from "./UniqueYears";

function App() {
  return (
    <div id="hello world" style={{ backgroundColor: "#BABABA" }}>
      <div style={{ height: 40 }}></div>
      <h1 style={{ marginTop: 0, textAlign: "center" }}>Movie List</h1>
      <BasicSelect />
      <MoviesList />
    </div>
  );
}

export default App;
