import * as React from "react";
import Stack from "@mui/material/Stack";
import Paper from "@mui/material/Paper";
import { styled } from "@mui/material/styles";
import { useParams } from "react-router-dom";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import Typography from "@mui/material/Typography";
import Rating from "@mui/material/Rating";
import Box from "@mui/material/Box";

const Title = styled(Paper)(({ theme }) => ({
  width: "100vh",
  padding: theme.spacing(1),
  ...theme.typography.body2,
  textAlign: "center",
}));

const About = () => {
  const { _id } = useParams();
  const [movie, setMovie] = React.useState(null);

  React.useEffect(() => {
    // Define the fetch function to get movie details by id
    const fetchMovieDetails = async () => {
      try {
        const response = await fetch(`https://1b57cv9bpl.execute-api.us-west-2.amazonaws.com/Prod/movies/${_id}`);
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
    <div
      style={{
        height: "100vh",
        backgroundColor: "#BABABA",
        paddingLeft: "20px",
        paddingRight: "20px",
      }}
    >
      <Stack direction="row" spacing={2}>
        <Title variant="elevation">
          <h1>{movie.title}</h1>
          <p>{movie.plot}</p>
          {movie.tomatoes &&
          movie.tomatoes.viewer &&
          movie.tomatoes.viewer.rating ? (
            <Box>
              <Typography variant="body1">Rating:</Typography>
              <Rating
                value={movie.tomatoes.viewer.rating}
                readOnly
                precision={0.5}
              />
            </Box>
          ) : (
            <Typography variant="body2">No rating available</Typography>
          )}
        </Title>
      </Stack>
      <div style={{ marginTop: 20 }}>
        <Accordion>
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1-content"
            id="panel1-header"
          >
            Genres
          </AccordionSummary>
          <AccordionDetails>{movie.genres}</AccordionDetails>
        </Accordion>
        <Accordion>
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel2-content"
            id="panel2-header"
          >
            Directors
          </AccordionSummary>
          <AccordionDetails>{movie.directors}</AccordionDetails>
        </Accordion>
        <Accordion>
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel3-content"
            id="panel3-header"
          >
            Release Date
          </AccordionSummary>
          <AccordionDetails>{movie.released.$date}</AccordionDetails>
        </Accordion>
        <Accordion>
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel3-content"
            id="panel3-header"
          >
            Comments
          </AccordionSummary>
          <AccordionDetails>
            {
              <ul>
                {movie.comments.map((comment, index) => {
                  return (
                    <li key={index}>
                      {
                        <Typography variant="body2">
                          {!!comment.text
                            ? comment.text
                            : "No comments available"}
                        </Typography>
                      }
                    </li>
                  );
                })}
              </ul>
            }
          </AccordionDetails>
        </Accordion>
      </div>
    </div>
  );
};

export default About;
