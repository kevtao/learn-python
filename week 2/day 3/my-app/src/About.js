import * as React from 'react';
import Stack from '@mui/material/Stack';
import Paper from '@mui/material/Paper';
import { styled } from '@mui/material/styles';
import { useParams } from "react-router-dom";

const DemoPaper = styled(Paper)(({ theme }) => ({
  width: '100vh',
  padding: theme.spacing(1),
  ...theme.typography.body2,
  textAlign: 'center',
}));

const About = () => {
  const { _id } = useParams();
  const [movie, setMovie] = React.useState(null);

  React.useEffect(() => {
    // Define the fetch function to get movie details by id
    const fetchMovieDetails = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/movies/${_id}`
        );
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setMovie(data);
      } catch (error) {
        console.error("Error fetching movie details:", error);
      }
    };

    if (!!_id) {
      fetchMovieDetails();
    }
  }, [_id]);

  if (!movie) {
    return <p>Loading...</p>;
  }

  return (
    <div style={{ height: '100vh', backgroundColor: "#BABABA", paddingLeft: '20px'}}>
    <Stack direction="row" spacing={2}>
      <DemoPaper variant="elevation"><h1>{movie.title}</h1></DemoPaper>
    </Stack>
      <p>{movie.plot}</p>
      <p>{movie.genres}</p>
      <p>{movie.directors}</p>
      <p>{movie.released}</p>
    </div>
  );
};

export default About;
